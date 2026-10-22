#!/usr/bin/env python3
"""Keep Deep Cove Research's DeepResearch Bench rank current, from the official leaderboard.

Reads the official leaderboard CSV, finds our rows and computes (for deep-cove-research, and for the site our best-ranked
row of deep-cove-research-pro and deep-cove-research):
  rank  = 1 + number of rows with a higher overall_score (sorted by overall_score, descending)
  total = number of rows
  score = our overall_score
  date  = UTC date of the leaderboard file's last commit in the Hugging Face space
          (if that lookup fails: the published date when the numbers are unchanged, else today's UTC date)

Then updates, only where something changed:
  main      README.md: the section between <!-- leaderboard:start --> and <!-- leaderboard:end --> (added after the
            "## DeepResearch Bench" heading when absent), plus the rank in the tagline, the badge alt text and
            source note 1; assets/badges/leaderboard.svg
  gh-pages  (our best-ranked row) leaderboard.json; index.html: every <span data-lb="KEY"> / <sup data-lb="KEY"> value (in the page and in
            its English/French text dictionary) and the meta and og descriptions

Validation is strict: the CSV must have model and overall_score columns, every score must be a number, our row must
appear exactly once, 0 < score <= 100 and 1 <= rank <= total; index.html must hold every marked key. On any failure
nothing is written and the script exits non-zero. Python standard library only.
"""
import argparse
import csv
import datetime as dt
import io
import json
import math
import os
import re
import sys
import time
import urllib.request

SPACE = 'muset-ai/DeepResearch-Bench-Leaderboard'
BOARD_URL = 'https://huggingface.co/spaces/' + SPACE
CSV_PATH = 'data_gpt55/leaderboard.csv'
CSV_URL = BOARD_URL + '/raw/main/' + CSV_PATH
INFO_URL = 'https://huggingface.co/api/spaces/' + SPACE + '/paths-info/main'
MODEL = 'deep-cove-research'
# deepcove.tech shows our best-ranked entry; this repo's README and badge keep its own row (MODEL).
SITE_MODELS = ('deep-cove-research-pro', 'deep-cove-research')
UA = 'deep-cove-research-leaderboard-sync (+https://github.com/aldrinor/deep-cove-research)'

MON_EN = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
MON_FR = ('janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.')
PAGE_KEYS = ('rank', 'total', 'score', 'score-fr', 'date', 'date-fr', 'ord-fr')


class Fail(Exception):
    pass


def fetch(url, data=None, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={'User-Agent': UA, 'Accept': '*/*',
                                                                  **({'Content-Type': 'application/json'} if data else {})})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode('utf-8')
        except Exception as e:  # network errors, HTTP errors
            last = e
            if i + 1 < tries:
                time.sleep(5 * (i + 1))
    raise Fail(f'could not fetch {url}: {last}')


def standing(text, model=MODEL):
    """(rank, total, score) of `model` from the leaderboard CSV text."""
    rows = list(csv.DictReader(io.StringIO(text.lstrip('﻿'))))
    if not rows or 'model' not in rows[0] or 'overall_score' not in rows[0]:
        raise Fail('leaderboard CSV has no model / overall_score columns')
    scores, ours = [], []
    for row in rows:
        name, raw = (row.get('model') or '').strip(), (row.get('overall_score') or '').strip()
        try:
            v = float(raw)
        except ValueError:
            raise Fail(f'overall_score is not a number for {name!r}: {raw!r}')
        if not math.isfinite(v):
            raise Fail(f'overall_score is not finite for {name!r}')
        scores.append(v)
        if name == model:
            ours.append(v)
    if len(ours) != 1:
        raise Fail(f'expected exactly one {model!r} row, found {len(ours)}')
    score, total = ours[0], len(scores)
    rank = 1 + sum(1 for v in scores if v > score)
    if not (0 < score <= 100):
        raise Fail(f'score out of range: {score}')
    if not (1 <= rank <= total):
        raise Fail(f'rank {rank} not within 1..{total}')
    return rank, total, round(score, 2)


def best_standing(text, models=SITE_MODELS):
    """(model, rank, total, score) of the best-ranked of our rows that is on the board."""
    found = []
    for m in models:
        try:
            found.append((m,) + standing(text, m))
        except Fail as e:
            if 'found 0' not in str(e):
                raise
    if not found:
        raise Fail('none of our rows is on the board: ' + ', '.join(models))
    return min(found, key=lambda r: (r[1], -r[3]))


def board_date(info_url):
    """UTC date (YYYY-MM-DD) of the leaderboard file's last commit, or None when it cannot be read."""
    try:
        body = json.dumps({'paths': [CSV_PATH], 'expand': True}).encode()
        info = json.loads(fetch(info_url, data=body, tries=2))
        stamp = next(x for x in info if x.get('path') == CSV_PATH)['lastCommit']['date']
        when = dt.datetime.fromisoformat(stamp.replace('Z', '+00:00')).astimezone(dt.timezone.utc)
        if not (2025 <= when.year <= dt.datetime.now(dt.timezone.utc).year + 1):
            return None
        return when.date().isoformat()
    except Exception as e:
        print(f'note: leaderboard commit date unavailable ({e})')
        return None


def values(d):
    y, m, day = (int(x) for x in d['date'].split('-'))
    s = '%.2f' % d['score']
    return {'rank': str(d['rank']), 'total': str(d['total']), 'score': s, 'score-fr': s.replace('.', ','),
            'date': f'{day} {MON_EN[m - 1]} {y}', 'date-fr': f'{"1er" if day == 1 else day} {MON_FR[m - 1]} {y}',
            'ord-fr': 'er' if d['rank'] == 1 else 'e'}


# ---- gh-pages ----

MARK = re.compile(r'<(span|sup) data-lb=(\\?")([a-z-]+)\2>([^<]*)<(\\?/)\1>')
META = re.compile(r'(<meta (?:name="description"|property="og:description") content="[^"]*?#)\d+( on DeepResearch Bench)(?! II\b)')


def patch_page(html, d):
    v, seen = values(d), set()

    def put(m):
        tag, q, key, _, close = m.groups()
        if key not in v:
            raise Fail(f'unknown marked key in index.html: {key}')
        seen.add(key)
        return f'<{tag} data-lb={q}{key}{q}>{v[key]}<{close}{tag}>'

    out = MARK.sub(put, html)
    missing = [k for k in PAGE_KEYS if k not in seen]
    if missing:
        raise Fail(f'index.html has no marked value for: {", ".join(missing)}')
    out, n = META.subn(lambda m: m.group(1) + v['rank'] + m.group(2), out)
    if n == 0:
        raise Fail('index.html has no meta description with the rank')
    return out


def page_json(d):
    rec = {'model': d.get('model', MODEL), 'rank': d['rank'], 'total': d['total'], 'score': d['score'], 'date': d['date'],
           'leaderboard': BOARD_URL, 'source': CSV_URL}
    return json.dumps(rec, indent=2) + '\n'


# ---- main ----

START, END = '<!-- leaderboard:start -->', '<!-- leaderboard:end -->'


def readme_block(d):
    v = values(d)
    return (f'{START}\n\n**#{v["rank"]} of {v["total"]}** · **{v["score"]}** on the [official leaderboard]({BOARD_URL})'
            f'<sup>[1](#sources)</sup> · as of {v["date"]}\n\n{END}')


def patch_readme(text, d):
    v, block = values(d), readme_block(d)
    if START in text and END in text and text.index(START) < text.index(END):
        a, b = text.index(START), text.index(END) + len(END)
        text = text[:a] + block + text[b:]
    else:
        m = re.search(r'^## DeepResearch Bench[ \t]*\n', text, re.M)
        if m:
            text = text[:m.end()] + '\n' + block + '\n' + text[m.end():]
        else:
            text = text.rstrip('\n') + '\n\n' + block + '\n'
    # the same facts elsewhere in the README, when present
    text = re.sub(r'(?<![\w#])#\d+( on DeepResearch Bench)(?! II\b)', lambda m: '#' + v['rank'] + m.group(1), text)
    text = re.sub(r'(DeepResearch Bench leaderboard: #)\d+(, score )\d+\.\d+',
                  lambda m: m.group(1) + v['rank'] + m.group(2) + v['score'], text)
    text = re.sub(r'(\*\*DeepResearch Bench official leaderboard\.\*\* GPT-5\.5 judge, )\d{1,2} [A-Z][a-z]{2} \d{4}'
                  r'(\. Deep Cove Research )\d+\.\d+(, rank )\d+( of )\d+(\.)',
                  lambda m: m.group(1) + v['date'] + m.group(2) + v['score'] + m.group(3) + v['rank'] + m.group(4) + v['total'] + m.group(5),
                  text)
    return text


def patch_badge(svg, d):
    v = values(d)
    svg = re.sub(r'(DeepResearch Bench: #)\d+( · )\d+\.\d+', lambda m: m.group(1) + v['rank'] + m.group(2) + v['score'], svg)
    return re.sub(r'(>#)\d+( · )\d+\.\d+(</text>)', lambda m: m.group(1) + v['rank'] + m.group(2) + v['score'] + m.group(3), svg)


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        return f.read()


def write(path, text):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--readme', help='README.md on main')
    ap.add_argument('--badge', help='assets/badges/leaderboard.svg on main')
    ap.add_argument('--site', help='gh-pages working tree (holds index.html)')
    ap.add_argument('--csv-url', default=CSV_URL)
    ap.add_argument('--info-url', default=INFO_URL)
    ap.add_argument('--message-file', help='write a commit message here when something changed')
    a = ap.parse_args()
    try:
        text = fetch(a.csv_url)
        rank, total, score = standing(text)
        site_model, s_rank, s_total, s_score = best_standing(text)
        published = None
        if a.site and os.path.exists(os.path.join(a.site, 'leaderboard.json')):
            try:
                published = json.loads(read(os.path.join(a.site, 'leaderboard.json')))
            except ValueError:
                published = None
        date = board_date(a.info_url)
        if date is None:
            same = published and (published.get('rank'), published.get('total'), published.get('score')) == (rank, total, score)
            date = published['date'] if same and re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(published.get('date'))) \
                else dt.datetime.now(dt.timezone.utc).date().isoformat()
        d = {'rank': rank, 'total': total, 'score': score, 'date': date}
        sd = {'model': site_model, 'rank': s_rank, 'total': s_total, 'score': s_score, 'date': date}
        print(f'leaderboard: {MODEL} rank {rank} of {total}, score {score:.2f}; site shows {site_model} rank {s_rank}, '
              f'score {s_score:.2f}; board date {date}')

        # build every new file in memory first; write only when all of them succeed
        plan = []
        if a.site:
            idx = os.path.join(a.site, 'index.html')
            if not os.path.exists(idx):
                raise Fail(f'{idx} not found')
            plan.append((idx, read(idx), patch_page(read(idx), sd)))
            lj = os.path.join(a.site, 'leaderboard.json')
            plan.append((lj, read(lj) if os.path.exists(lj) else None, page_json(sd)))
        if a.readme:
            plan.append((a.readme, read(a.readme), patch_readme(read(a.readme), d)))
        if a.badge and os.path.exists(a.badge):
            plan.append((a.badge, read(a.badge), patch_badge(read(a.badge), d)))
        for path, old, new in plan:  # re-running on the new text must change nothing
            if path.endswith('index.html') and patch_page(new, sd) != new or path.endswith('.md') and patch_readme(new, d) != new:
                raise Fail(f'update of {path} is not stable')
    except Fail as e:
        print(f'error: {e}; nothing changed', file=sys.stderr)
        return 1

    changed = [p for p, old, new in plan if old != new]
    for path, old, new in plan:
        if old != new:
            write(path, new)
    print('changed: ' + (', '.join(changed) if changed else 'nothing'))
    if a.message_file and changed:
        v = values(sd)
        with open(a.message_file, 'w', encoding='utf-8') as f:
            f.write(f'Update DeepResearch Bench rank: #{v["rank"]} of {v["total"]}, {v["score"]} (board of {v["date"]})\n\n'
                    f'Automatic update from the official leaderboard: {BOARD_URL}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
