# Replicating Notion's Multi-View Databases in Obsidian (October 2026)

As of October 2026, the best way to replicate Notion's multi-view databases in Obsidian is the core **Bases** plugin. Since Obsidian 1.14 (public release October 5, 2026), it ships Table, List, Cards (gallery), Kanban and Map views over the same notes. Add one maintained community Bases view for **Calendar**, which is the only one of your four views still missing from core. Most of the older "Notion-in-Obsidian" plugins (DB Folder, Projects, DataLoom) are now archived. Choose among them only if you are already invested in one.

## TL;DR
- **Default stack: core Bases plus one calendar view plugin (e.g., Calendar Bases).** This covers Table, Kanban, Calendar and List over plain Markdown/YAML properties, with inline editing in tables and drag-to-update in Kanban and Calendar. A native Bases calendar view is listed as "Planned" on Obsidian's roadmap, so the calendar plugin is probably a stopgap.
- **If you want the most Notion-like single plugin, use Notion Bases or Make.md, but expect lock-in.** Both offer Table/Board/Calendar/List (and more) plus true relations and rollups. They keep view and schema config in their own files (`_database.md` for Notion Bases; Make.md's own database files) instead of core `.base` files, and each depends on a single maintainer.
- **Dataview is now a niche tool, not the default; DB Folder, Projects and DataLoom are dead.** Dataview's views are read-only and it has had no release since spring 2025. Datacore is still a 0.x beta aimed at JavaScript users. Use Dataview or Datacore for task roll-ups, inline queries and scripted views, not for your main database UI.

## Key Findings

### 1. Core Bases is now the foundation, and it has grown quickly
- **Timeline:**
  - 1.9 (May 2025, early beta): Bases debuted.\[1\] It became public in August 2025.\[2\]\[3\]
  - 1.10 (November 2025): added List and Map views, grouping, summaries and the **Bases API** that lets plugins add new view types.\[2\]\[3\]
  - 1.12 (February 2026): added search inside Bases.\[3\]
  - 1.14: added a native **Kanban** view and a new **Group** menu. The Group menu lets you choose a grouping property and reorder, hide or add groups in any view, and makes groups collapsible in table, cards and list layouts.\[4\] The 1.14.0 early-access (Catalyst) changelog is dated September 2, 2026, and the public 1.14 release followed on October 5, 2026.
- **Current view types:** the official help page lists Table, List, Cards ("gallery-like views with images"), Kanban and Map, and notes that "Additional layouts can be added by Community plugins."\[5\]
- **Roadmap:** "Calendar view for Bases — Display files as an interactive calendar" and "Bases support for Publish" are both listed as **Planned**, with no date.\[3\]
- **Data model:**
  - All data lives in your Markdown files and their YAML properties.\[5\]
  - A view definition is a `.base` YAML file or a code block embedded in a note.\[5\]
  - Several named views per base, each with its own filters, sorts, grouping, visible properties and result limit.\[6\]
  - Formulas, a function library and table summaries (sum, average, median, etc.).\[6\]
- **Notion migration:** the official Importer's Notion API mode (November 2025) converts Notion databases and formulas into Bases. However, "only the primary view for each database is imported" and linked data sources are not imported.\[7\]

### 2. Bases' Kanban view is useful but immature
- **How it works:** dragging a card to another column rewrites the grouped property in that note.\[8\] It works on desktop and mobile with no plugin to maintain.\[9\]
- **Limits in the official docs:** if you group by a formula or by a file property other than `file.folder`, "you can't move cards or columns, or create notes from the columns."\[8\]
- **Gaps from Mike Schmitz's review (Practical PKM, September 7, 2026, written against the early-access build):**
  - Grouping is limited to one property (no swimlanes).\[9\]
  - Cards are notes, not checkbox tasks.\[9\]
  - Empty columns disappeared and lost their position.\[9\]
  - Cards can't be manually reordered within a column.\[9\]
  - New notes from the board landed in the vault root instead of the filtered folder.\[9\]
- His verdict: "A board I can't order is just a status display."\[9\] Obsidian's roadmap lists, as launched in 1.14, the ability to "Create, hide, collapse, and manually reorder groups across all Bases views that support them," which should fix the empty-column problem. Manual card ordering is still missing.

### 3. Calendar is the remaining gap, filled by Bases-view plugins
Because the Bases API (1.10) lets plugins register view types, several calendar layouts now work over the same `.base` data:
- **Calendar Bases** (edrickleong) is built on FullCalendar. It supports drag-to-reschedule (writes back to frontmatter), multi-day events with optional end dates, desktop and mobile. The official community directory lists it at v0.2.8, last updated six months ago, and Obsidian Stats counts 124,101 downloads.
- **Other options:**
  - **Just Simple Calendar:** month and "infinite" week views, no external libraries.\[10\]
  - **Yabacavi:** day/week/month grid, drag to reschedule while keeping time and timezone.\[11\]
  - **Calendar Note View.**\[12\]
  - **Bases Calendar** (mtellin, BRAT-only). A fork describes itself as "100% vibe-coded software built for personal use", so avoid it for important data.\[13\]\[14\]
- **TaskNotes** and **Planner** bundle their own Bases-powered calendar views (see below).

### 4. Community Kanban views for Bases fill the native view's gaps
If the native Kanban's limits bother you, these Bases view plugins add the missing features:
- **Kanban Bases View** (xiwcx / I. Welch Canavan): v0.10.6, 32 releases, updated about three weeks ago. Swimlanes on a second property, saved column order, quick-add per column, column colours.\[15\]
- **Base Board** (mderazon): manual card order stored in a `kanban_order` property, and a floating editor modal.\[16\]
- **Bases Board** (flowing-abyss): Kanban plus gallery with row and column grouping.\[17\]
- **Kanban Action Planner** (dsebastien).\[18\]
- **Bases Kanban** (ewerx): a forum user noted "no activity since the day it was created, 7 months ago."\[19\] Avoid it.

## Details: Plugin-by-Plugin Assessment

### Core Bases
- **Views:** Table ✔, Kanban ✔ (1.14+), List ✔, Cards/gallery ✔, Map ✔ (needs Maps plugin). Calendar ✘ (planned; use a plugin).
- **Storage:** frontmatter/YAML properties only. It does not read inline `key:: value` fields or checkbox tasks inside a note body; tasks must be their own notes, or use a plugin such as Bases Task Rows.\[20\]
- **Editing:** inline cell editing in Table, drag-to-update in Kanban.
- **Filter, sort, group, formulas:** global and per-view filters with nested and/or/not, per-view sort and group, formulas, summaries, result limits, CSV export.
- **Relations and rollups:** no relation property type. You can approximate them with formulas:
  - `link.asFile()` / `file()` follow a link.\[21\]
  - `.properties` reads the linked note's properties.
  - `list.map()`, `list.filter()` and `list.reduce()` aggregate them.\[21\]
  - Example: `tasks.map(value.asFile().properties.hours).reduce(acc + value, 0)` sums hours across linked notes.
  - The `this` keyword lets an embedded base show "items related to this note" (e.g., `file.hasLink(this.file)`).\[6\]
  - **Caveats:** the docs warn that `file.backlinks` is "performance heavy" and that `file.backlinks` and `file.properties` do not "automatically refresh results when the vault is changed."\[6\] An Obsidian moderator likewise said "You will have to manually reload the table."\[22\] Links must be stored as real wikilinks or `.asFile()` errors out.\[23\]
- **Performance:**
  - There are no official benchmarks or row limits, and there is no native pagination (the community "Bases Paginator" plugin fills that gap).\[24\]
  - Forum reports are anecdotal and mixed. One user saw "10 FPS"-style scroll stutter on a Windows PC while the same base rendered perfectly on their phone.\[25\] Another saw lag with only about 50 files, which points to device or GPU issues rather than vault size.\[26\]
  - The 1.14 release "Fixed periodic input lag in large vaults caused by properties getting recomputed in the background."\[4\]
- **Mobile:** fully supported. On phones, Results, Sort, Group and Properties sit under a Display menu.\[27\]
- **Maintenance:** first-party and updated with every Obsidian release. This is its biggest advantage.
- **Learning curve:** low for tables and boards. Moderate for formulas, which use an expression language.

### Dataview / DataviewJS
- **Views:** TABLE, LIST, TASK, CALENDAR query outputs. No Kanban.
- **Storage:** frontmatter plus inline fields; tasks are queried from note bodies.
- **Editing:** read-only, apart from toggling task checkboxes. This is its main gap compared with Notion.
- **Strengths:** a query language with no Bases equivalent, inline queries inside sentences, vault-wide task roll-ups, and arbitrary JavaScript.\[28\]
- **Maintenance:** per Moritz Jung's Obsidian Stats version history, the latest release is 0.5.70 (beta) from 2025-04-07 and the last stable release is 0.5.68 from 2025-03-15, both cut by community maintainer @holroy. Development has stalled, though the plugin is not archived and still works on 1.14.4. It remains the most-installed data plugin, with 5,043,838 downloads per Obsidian Stats (the official directory rounds this to 5.1M).
- **Consensus:** "For dashboards in 2026, reach for Bases first" (dsebastien).\[28\] Keep Dataview for task roll-ups and scripting.

### Datacore
- **What it is:** the "work-in-progress" successor to Dataview from the same author. It promises 2–10x faster queries, React-based views and WYSIWYG editable tables.\[29\]
- **Status:** v0.1.29 (March 23, 2026), about 347k downloads, listed in the community directory, desktop and mobile.\[29\]\[30\]
- **Fit:** its docs say it is "in a power-user stage focused on javascript/typescript savvy users", with non-JS query views "coming in the future."\[31\] It has no built-in Kanban or Calendar views, so you build them in JSX. Not a Notion replacement for non-coders.

### DB Folder (Database Folder)
- **What it was:** a Notion-like table built on Dataview, with relations, rollups, formulas and inline editing.\[32\]
- **Status:** **archived July 28, 2025** and removed from the community list in September 2025.\[32\]\[33\] Some users stayed on it because "DBFolder does support relations."\[34\] There is no Kanban or Calendar view. Migrate off it.

### Projects (Marcus Olsson)
- **What it was:** the closest pre-Bases "one plugin" answer, with Table, Board, Calendar and Gallery views over notes.
- **Status:** **discontinued May 2025**, removed from the directory May 27, 2025, archived July 18, 2025. It can still be installed via BRAT.\[35\]\[36\]\[37\]
- **Fork:** "Projects Plus" (ParkPavel, October 2025) adds a rebuilt calendar, but its directory status was still pending in forum posts.\[38\] Treat it as experimental.

### Kanban (mgmeyers)
- **What it is:** a Kanban board stored in one Markdown file whose cards are list items.\[39\] It is not a view over your notes' properties, so it is not a database view.
- **Status:** v2.0.51, last updated about two years ago, moved to the community-archive organisation.\[40\] On January 12, 2026 the author wrote that he "no longer [has] the bandwidth to maintain the Kanban plugin."\[41\] It still works and suits lightweight checklist boards. For database-style boards, use Bases Kanban instead.

### Calendar (Liam Cain)
- **What it is:** a sidebar month calendar for navigating daily and weekly notes. It does not show database items by a date property.\[42\]
- **Status:** v1.5.10, last updated five years ago, 3.1M downloads. Maintained forks include Calendar Plus and Calendar Hub.\[42\]\[43\]\[44\] Not a Notion calendar view.

### Full Calendar / Full Calendar Remastered
- **Original Full Calendar:** archived August 1, 2026; last release 0.10.7 (April 2023).\[45\]\[46\]
- **Full Calendar Remastered:**
  - v0.13.6, about 50k downloads, active GitHub organisation.\[47\]
  - Pulls events from frontmatter notes, daily notes, ICS, two-way CalDAV and Google Calendar, **Bases**, Tasks and TaskNotes.\[47\]
  - The directory notes it "has not been manually reviewed by Obsidian staff." It was removed and re-added several times in May–June 2026,\[48\] and open issues include multi-day event truncation.\[49\]
  - Good for a personal schedule; less ideal as the calendar view of a database.

### Tasks
- **What it is:** checkbox tasks with dates, recurrence and priorities, queried into list views. Not a multi-view database.
- **Status:** actively maintained (v8.6.0, by Clare Macrae and Ilyas Landikov).\[50\]\[51\]
- **Pairing:** works with Full Calendar Remastered and the new **Bases Task Rows** plugin, which shows each checklist task as a row in a Bases view. That plugin is days old.\[20\]

### TaskNotes
- **What it is:** one note per task with YAML frontmatter. **All views are Bases views**: Task List, Kanban, Calendar, Agenda and Mini Calendar.\[50\]\[52\]\[53\]
- **Features:** recurrence, time tracking, Pomodoro, dependencies, Google/Outlook OAuth sync and ICS.\[53\]\[54\]\[55\]\[56\]
- **Status:** v4.13.x, requires Obsidian 1.12.2+.\[57\] Highly ranked in the plugin directory and actively updated.\[17\]
- **Fit:** the best "Notion task database" experience in Obsidian today, but task-specific.

### Notion Bases (bgarciamoura)
- **What it is:** a folder-based standalone database engine: "7 views" (Table, Board, Gallery, List, Calendar, Timeline/Gantt, Chart) and "18 column types," including Relation, Lookup and Rollup, plus spreadsheet-style formulas, subtasks, CSV import/export and embeds.\[58\]
- **Storage:** rows are `.md` files with frontmatter; schema and view config live in `_database.md`.\[58\]
- **Status:** v1.13.0. The official directory lists 27k downloads and 30 releases since it was created seven months ago, last updated last month. Desktop and mobile, GPL-3.0.
- **Caveats:** its README comparison claims core Bases has no Board/Kanban, which has been outdated since 1.14.\[58\] It does not use `.base` files, so its views do not carry over to core Bases.

### Make.md
- **What it is:** a broad "Spaces" organisation layer with lists, tables, calendars and boards, "two-way relations, formulas and rollups," and dashboards.\[59\]
- **Status:** v1.3.5, about 876k downloads, updated about three months ago.\[59\]
- **Caveats:** note metadata stays in frontmatter, but per ObsidianMate's documentation "layouts, formulas, and relations are stored in Make.md-specific database files" (the `.mdb` files). Disabling the plugin loses the views, and you must sync those files. Users report added complexity, and one lost their Spaces after a reload.\[60\]

### DataLoom
- **Status:** the original was archived March 9, 2025, removed May 2, 2025. The author's notice says "DataLoom is no longer maintained" and asks users to export to Markdown.\[61\]\[62\] Data lived in `.loom` files.\[63\] A fork (aykutkardas, v8.16.2, November 2025) exists.\[64\] Do not start new databases on it.

### Day Planner
- **What it is:** a daily timeline for time-blocking tasks. Not a database view.
- **Status:** actively maintained (v0.35.1, July 31, 2026).\[65\] Recent releases dropped the Dataview dependency.\[66\]

## Comparison Table

| Plugin | Table | Kanban | Calendar | List/Gallery | Storage | Editable in place | Relations/rollups | Maintenance (Oct 2026) | Best use |
|---|---|---|---|---|---|---|---|---|---|
| **Bases (core)** | ✔ | ✔ (1.14+) | ✘ (planned) | ✔ / ✔ | YAML properties + `.base` | Yes (table cells, Kanban drag) | Formula workaround only | First-party, active | Default foundation |
| Calendar Bases / other Bases calendar views | — | — | ✔ | — | Same as Bases | Drag to reschedule | Via Bases | Active (single devs) | Fill Bases' calendar gap |
| Kanban Bases View / Base Board | — | ✔ (swimlanes, manual order) | — | — | Same as Bases | Drag | Via Bases | Active | Power Kanban on Bases |
| TaskNotes | ✔ (task list) | ✔ | ✔ | ✔ | YAML, one note per task | Yes | Projects/dependencies | Active | Task/project management |
| Notion Bases | ✔ | ✔ | ✔ | ✔ / ✔ (+Timeline, Chart) | YAML + `_database.md` | Yes | **Native** relation/lookup/rollup | Active, young | Closest Notion clone |
| Make.md | ✔ | ✔ | ✔ | ✔ / ✔ | YAML + Make.md database files | Yes | **Native** | Active | All-in-one workspace |
| Dataview / DataviewJS | ✔ | ✘ (JS only) | ✔ (basic) | ✔ | YAML + inline fields | No (read-only) | Via queries | Stalled since 2025 | Queries, task roll-ups |
| Datacore | ✔ (editable) | JSX only | JSX only | ✔ | YAML + inline | Yes (tables) | Via code | 0.x beta | JS power users |
| DB Folder | ✔ | ✘ | ✘ | ✘ | YAML/inline via Dataview | Yes | Yes | **Archived Jul 2025** | Migrate away |
| Projects | ✔ | ✔ | ✔ | ✔ (gallery) | YAML | Yes | ✘ | **Archived Jul 2025** | Migrate away |
| Kanban (mgmeyers) | — | ✔ (board file) | — | — | Markdown list in one file | Yes | ✘ | Unmaintained | Simple checklist boards |
| Full Calendar Remastered | — | — | ✔ | ✔ (list) | Frontmatter/daily notes/ICS | Yes | ✘ | Active, unreviewed | Personal scheduling |
| Tasks | — | — | — | ✔ (query lists) | Inline checkboxes | Toggle/edit | ✘ | Active | Inline task tracking |
| DataLoom | ✔ | ✘ | ✘ | ✘ | `.loom` JSON | Yes | ✘ | **Archived Mar 2025** | Avoid |

## Common Combinations and Trade-offs
- **Bases + Calendar Bases (+ optionally Kanban Bases View).** This is the recommended stack: all four views over the same `.base` file and the same properties, one first-party core, and small add-ons that can be swapped out because they read standard Bases config. Trade-offs: relations and rollups are formula workarounds that don't auto-refresh, and calendar quality depends on a third-party developer until the native view ships.
- **Bases + TaskNotes.** Best for task and project databases: Kanban, Calendar, Agenda and List come preconfigured, with calendar sync. Trade-off: it requires the one-note-per-task model.
- **Notion Bases alone (or Make.md alone).** One plugin gives you every view plus real relations and rollups, which is the most Notion-like feel. Trade-offs: proprietary config files, a single maintainer, and no reuse of core Bases views. That is the same risk that stranded DB Folder and Projects users in 2025.
- **Dataview + DB Folder + Calendar/Kanban (legacy).** The classic 2022–2024 stack. Both DB Folder and Kanban are now unmaintained, so move these databases to Bases.
- **Projects alone (legacy).** It was elegant, but it is archived and BRAT-only. Migrate.
- **Bases + Dataview/Datacore.** Bases handles the editable UI; Dataview or Datacore handle task roll-ups, inline queries and scripted dashboards. This is a sensible hybrid for power users.

## Notion vs. Obsidian: Remaining Gaps
| Notion capability | Obsidian status (Oct 2026) |
|---|---|
| Multiple views of one database | **Matched** by Bases (multiple named views per `.base`) |
| Table, Board, List, Gallery | **Matched** natively (Table, Kanban, List, Cards) |
| Calendar view | **Plugin only**; native is "Planned" |
| Timeline/Gantt, Chart | Plugin only (Notion Bases, Planner, chart plugins) |
| Inline editing | Matched in Table and Kanban; cards and calendar views vary by plugin |
| Per-view filters, sorts, grouping | Matched; grouping limited to one property; manual card order missing natively |
| Formulas | Matched (expression language) |
| Relations/rollups | **Partial**: formula workaround in Bases; native only in Notion Bases, Make.md and the archived DB Folder |
| Database templates | No per-database template system found in Bases' docs; users rely on core Templates or Templater |
| Real-time collaboration, sharing, Publish | Not available; Bases on Publish is "Planned" |

## Recommendations
- **Migrating from Notion:**
  1. Import with the official Importer's **Notion (API)** mode so databases become `.base` files.\[67\]\[68\]
  2. Rebuild any secondary views manually; only the primary view is imported.\[7\]\[69\]
  3. Add **Calendar Bases** for date views and **Kanban Bases View** only if you need swimlanes or saved column order.
  4. Use **TaskNotes** for task databases.
  5. Choose **Notion Bases** only if relations and rollups are essential to your workflows and you accept the lock-in risk.
- **Minimal plugins:** use core Bases (Table, Kanban, List, Cards) plus exactly one calendar view plugin, and keep every field in YAML properties. When Obsidian ships its planned calendar view, you can drop the plugin with no data changes.
- **Comfortable with JS/queries:** use Bases as the editable front end. Use **Dataview** for task roll-ups and inline queries, accepting that it is stalled, or try **Datacore** for faster, editable, React-based custom views (Kanban/Calendar you build yourself). Use Bases formulas with `asFile().properties` for lookups.

## Caveats
- **Release timing:** Bases' Kanban view went public only on October 5, 2026.\[4\] Most reviews, including Practical PKM's, tested the early-access build, and some reported issues may already be fixed.\[9\]
- **Outdated comparisons:** third-party pages such as Notion Bases' README and older XDA articles still say core Bases lacks Kanban.\[58\]\[70\]
- **Download counts and update dates:** "last updated" values come from the Obsidian community directory and stats sites and change quickly.
- **Single-developer risk:** many Bases view plugins are new, single-developer projects; some are self-described as "vibe-coded."\[14\] Check the date of the last commit before relying on one.
- **Performance:** no official performance figures exist for Bases at scale. Test on your own vault, especially formulas that use `file.backlinks`.

## 資料來源

1. [Obsidian 1.9.0 Desktop (Early access) - Obsidian](https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/)
2. [AlternativeTo LogoAlternativeTo Logo Text](https://alternativeto.net/software/obsidian/news)
3. [Obsidian Roadmap](https://obsidian.md/roadmap/)
4. [Obsidian 1.14 Desktop (Public)](https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/)
5. [Introduction to Bases - Obsidian Help](https://obsidian.md/help/bases)
6. [Bases syntax - Obsidian Help](https://obsidian.md/help/bases/syntax)
7. [Import from Notion - Obsidian Help](https://obsidian.md/help/import/notion)
8. [Kanban view - Obsidian Help](https://obsidian.md/help/bases/views/kanban)
9. [An Honest Review of Obsidian's New Kanban View](https://practicalpkm.com/kanban-review/)
10. [Just Simple Calendar - Obsidian Plugin](https://community.obsidian.md/plugins/just-simple-calendar)
11. [Yabacavi - Obsidian Plugin](https://community.obsidian.md/plugins/yabacavi)
12. [Calendar Note View - Obsidian Plugin](https://community.obsidian.md/plugins/calendar-note-view)
13. [GitHub - mtellin/obsidian-bases-calendar: Calendar view for Obsidian Bases — multiple time views, Google Calendar colors, timed events, and drag-to-reschedule · GitHub](https://github.com/mtellin/obsidian-bases-calendar)
14. [GitHub - movanvuuren/obsidian-bases-calendar: Calendar view for Obsidian Bases — multiple time views, Google Calendar colors, timed events, and drag-to-reschedule · GitHub](https://github.com/movanvuuren/obsidian-bases-calendar)
15. [Kanban Bases View - Obsidian Plugin](https://community.obsidian.md/plugins/kanban-bases-view)
16. [GitHub - mderazon/obsidian-base-board: Kanban Plugin For Obsidian · GitHub](https://github.com/mderazon/obsidian-base-board)
17. [Obsidian plugins with #kanban - 23 plugins](https://www.obsidianstats.com/tags/kanban)
18. [How I Turned My Obsidian Notes Into Kanban Boards](https://www.dsebastien.net/how-i-turned-my-obsidian-notes-into-kanban-boards/)
19. [Bases Kanban Plugin - Plugins - Obsidian Forum](https://forum.obsidian.md/t/bases-kanban-plugin/109179)
20. [Bases Task Rows - Obsidian Plugin](https://community.obsidian.md/plugins/bases-task-rows)
21. [Functions - Obsidian Help](https://obsidian.md/help/bases/functions)
22. [Bases: Show property of a linked file as column - #6 by WhiteNoise - Help - Obsidian Forum](https://forum.obsidian.md/t/bases-show-property-of-a-linked-file-as-column/101636/6)
23. [Help with a Bases Filter (for Tasknotes Use) - Help - Obsidian Forum](https://forum.obsidian.md/t/help-with-a-bases-filter-for-tasknotes-use/108230)
24. [Bases Paginator - Obsidian Plugin](https://community.obsidian.md/plugins/bases-paginator)
25. [Obsidian Bases Low Performance](https://forum.obsidian.md/t/obsidian-bases-low-performance/107622)
26. [Bases is super slow and stuttery / laggy - Help - Obsidian Forum](https://forum.obsidian.md/t/bases-is-super-slow-and-stuttery-laggy/108428)
27. [Views - Obsidian Help](https://obsidian.md/help/bases/views)
28. [The Complete Guide to Dataview in Obsidian - Query Everything, Then Make It Last](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/)
29. [Datacore - Obsidian Plugin](https://community.obsidian.md/plugins/datacore)
30. [Datacore: High-Performance Obsidian Plugin for PKM Queries](https://dev.co/databases/open-source/datacore)
31. [Datacore](https://blacksmithgu.github.io/datacore/)
32. [GitHub - RafaelGB/obsidian-db-folder: Obsidian Plugin to Allow Notion like database based on folders · GitHub](https://github.com/RafaelGB/obsidian-db-folder)
33. [Obsidian Plugin Updates 2025-09-07 to 2025-09-13](https://www.obsidianstats.com/posts/2025-09-14-weekly-updates)
34. [Bases: Relations Between Notes From Other Bases (Relation Among Bases, Intersection) - Feature requests - Obsidian Forum](https://forum.obsidian.md/t/bases-relations-between-notes-from-other-bases-relation-among-bases-intersection/102421)
35. [GitHub - obsmd-projects/obsidian-projects: Plain text project planning in Obsidian · GitHub](https://github.com/obsmd-projects/obsidian-projects)
36. [Development for Projects plugin needed - Plugins ideas (Archival in progress) - Obsidian Forum](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089)
37. [Projects](https://www.moritzjung.dev/obsidian-stats/plugins/obsidian-projects/)
38. [Projects Plus plugin - Plugins - Obsidian Forum](https://forum.obsidian.md/t/projects-plus-plugin/106826)
39. [Obsidian Kanban Plugin: Track Projects In Your Notes](https://locul.ai/blog/obsidian-kanban-plugin)
40. [Kanban - Obsidian Plugin](https://community.obsidian.md/plugins/obsidian-kanban)
41. [obsidian-kanban/MAINTAINERS.md at main · community-archive/obsidian-kanban · GitHub](https://github.com/obsidian-community/obsidian-kanban/blob/main/MAINTAINERS.md)
42. [Calendar - Obsidian Plugin](https://community.obsidian.md/plugins/calendar)
43. [Calendar Hub - Obsidian Plugin](https://community.obsidian.md/plugins/calendar-hub)
44. [Calendar Plus - Obsidian Plugin](https://community.obsidian.md/plugins/calendar-plus)
45. [GitHub - community-archive/obsidian-full-calendar: Keep events and manage your calendar alongside all your other notes in your Obsidian Vault. · GitHub](https://github.com/obsidian-community/obsidian-full-calendar)
46. [Full Calendar](https://www.moritzjung.dev/obsidian-stats/plugins/obsidian-full-calendar/)
47. [Full Calendar Remastered - Obsidian Plugin](https://community.obsidian.md/plugins/full-calendar-remastered)
48. [Full Calendar Remastered](https://www.moritzjung.dev/obsidian-stats/plugins/full-calendar-remastered/)
49. [Issues · obsidian-full-calendar-remastered/plugin-full-calendar · GitHub](https://github.com/obsidian-full-calendar-remastered/plugin-full-calendar/issues)
50. [Best Obsidian plugin for task management in 2026](https://vaultpicks.net/best-obsidian-plugin-task-management/)
51. [Tasks - Obsidian Plugin](https://community.obsidian.md/plugins/obsidian-tasks-plugin)
52. [TaskNotes - Obsidian Plugin](https://community.obsidian.md/plugins/tasknotes)
53. [TaskNotes](https://www.obsidianstats.com/plugins/tasknotes)
54. [How I Manage All My Tasks Inside Obsidian with the TaskNotes Plugin](https://www.dsebastien.net/tasknotes-obsidian-plugin-task-management/)
55. [This Week in Obsidian #10](https://thisweekinobsidian.substack.com/p/this-week-in-obsidian-10)
56. [Integrations](https://tasknotes.dev/obsidian/features/integrations/)
57. [TaskNotes for Obsidian](https://tasknotes.dev/obsidian/)
58. [Notion Bases](https://community.obsidian.md/plugins/notion-bases)
59. [make.md - Obsidian Plugin](https://community.obsidian.md/plugins/make-md)
60. [Obsidian Make.md · Outliner Software](https://www.outlinersoftware.com/topics/viewt/10108/0/obsidian-makemd)
61. [DataLoom](https://www.moritzjung.dev/obsidian-stats/plugins/notion-like-tables/)
62. [GitHub - decaf-dev/obsidian-dataloom: Better Obsidian Tables Without The Hassle · GitHub](https://github.com/decaf-dev/obsidian-dataloom)
63. [decaf-dev/obsidian-dataloom](https://deepwiki.com/decaf-dev/obsidian-dataloom)
64. [GitHub - aykutkardas/obsidian-dataloom: Better Obsidian Tables Without The Hassle](https://github.com/aykutkardas/obsidian-dataloom)
65. [Day Planner](https://www.obsidianstats.com/plugins/obsidian-day-planner)
66. [Releases · ivan-lednev/obsidian-day-planner · GitHub](https://github.com/ivan-lednev/obsidian-day-planner/releases)
67. [Import from Notion](https://retypeapp.github.io/obsidian/import/notion/)
68. [Importing from External Systems](https://deepwiki.com/obsidianmd/obsidian-help/8.2-importing-from-external-systems)
69. [Notion to Obsidian Migration: API vs HTML Import Checklist](https://www.obsibrain.com/blog/notion-to-obsidian-migration-a-complete-guide-and-checklist/)
70. [4 Bases plugins you should be using](https://www.xda-developers.com/bases-plugins-you-should-be-using/)