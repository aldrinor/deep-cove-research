# Multi-View Database Architectures in Obsidian: A Comparative Analysis of Notion-Equivalent Plugins

## The Paradigm Shift in Obsidian Database Emulation

Replicating Notion’s multi-view database functionality—specifically the ability to toggle seamlessly between Table, Kanban (Board), Calendar, and List layouts over a single underlying dataset—historically represented the primary architectural friction point for practitioners migrating to Obsidian [1](https://www.reddit.com/r/ObsidianMD/comments/14vybi9/how_well_can_you_replicate_notion_in_obsidian/). This tension stems from a fundamental divergence in data primitives. Notion operates as a cloud-first, block-based relational database where every database is an isolated, top-down container that begins empty and enforces a rigid schema across its child pages [2](https://fabric.so/comparison/notion-vs-obsidian). Conversely, Obsidian is built on a local-first, bottom-up directory of plain-text Markdown (`.md`) files, where metadata resides in YAML frontmatter (Properties) and relationships exist organically as wikilinks rather than structured foreign keys [2](https://fabric.so/comparison/notion-vs-obsidian).

Between mid-2025 and October 2026, the Obsidian database ecosystem underwent a structural consolidation driven by the release and rapid maturation of **Obsidian Bases** , a native core plugin [3](https://www.makeuseof.com/obsidian-bases-notion-database/). Launched in August 2025 (Obsidian v1.9) with Table and Cards layouts, Bases expanded in November 2025 (v1.10) to include List views, Map views, property grouping, table summaries, and a public **Bases API**  that enables third-party developers to register custom view layouts [9](https://obsidian.md/roadmap/). In October 2026 (v1.14), the core development team added a native Kanban view and manual group reordering directly to Bases [9](https://obsidian.md/roadmap/).

This native integration triggered an immediate shakeout among first-generation community database plugins. Pioneering tools that previously carried the burden of Notion emulation—most notably Marcus Olsson’s **Obsidian Projects**  (discontinued in May 2025), RafaelGB’s **DB Folder**  (archived in July 2025), and **DataLoom**  (archived)—ceased active development in their original repositories [11](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089). In their wake, the ecosystem bifurcated into two distinct architectural paradigms: a **Modular Native Stack**  anchored by Core Bases plus specialized API view extensions (such as **Extended Base**  and **Calendar Bases** ), and **Monolithic Workspace Suites**  (led by **Notion Suite** , **Projects Plus** , and **Make.md** ) that provide self-contained multi-view engines with advanced relational rollups and Gantt timelines [15](https://community.obsidian.md/plugins/obs-projects-plus).

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

Ecosystem Architecture · Oct 2026  Obsidian v1.14 Core & Community Solutions

### Modular Native Extensions and Monolithic Suites Replace First-Generation Database Plugins

#### 1. Dominant Ecosystem Paradigms (2026)

4 Primary Architectural Paths

Modular Core

##### Core Bases Stack

Bases v1.14 + Extended Base + Calendar Bases. Zero overhead, official indexer, pure Markdown.

4-View Ready: Complete

Monolithic Suite

##### Notion Suite

Complete 6-view reproduction in fenced code blocks. Relations, rollups, WIP limits, slash menu.

4-View Ready: All 6 Views

Project Hub

##### Projects Plus (v3.7)

Fork of Olsson's Projects. Dashboards, boards, tables, calendars, and galleries. Config in data.json.

4-View Ready: Omits List

Integrated OS

##### Make.md

Spaces & Context views (Table, Board, Calendar, Gallery). Relies on binary .mdb database files.

Storage: Binary .mdb

Filter:

Native / Full    Addon / API    Partial / Query    Missing    Deprecated

| Tool / Stack | Status | Table | Kanban | Calendar | List | Cards/Gal. | Timeline | Relations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bases Modular Stack REC  Bases v1.14 + Extended + Calendar | Active Core | Full | Full | Addon | Full | Full | — | Partial |
| Notion Suite Fenced code block (notion-db) | Active | Full | Full | Full | Full | Full | Full | Full |
| Make.md Spaces & Context Database | Active | Full | Full | Full | Full | Full | — | Binary |
| Core Bases (v1.14) Native Core Plugin (.base) | Active Core | Full | Full | — | Full | Full | — | Partial |
| Projects Plus (v3.7) Active Fork of Olsson's Projects | Active | Full | Full | Full | Omitted | Full | — | Full |
| Dataview DQL / DataviewJS Query Engine | Active | Query | — | Query | Query | — | — | Code |
| DataDeck Canonical CSV In-Place Editor | Active | Full | Full | Partial | — | Full | Full | — |
| Archived Gen-1 Tools Obsidian Projects & DB Folder | Archived | Legacy | Legacy | Legacy | — | Legacy | — | — |

Hover over any matrix badge to inspect technical implementation details and architectural tradeoffs.

Capabilities Inspector

#### 3. Data Persistence & Architecture Spectrum

Where Data and Views Live

100% Native Markdown Zero Lock-In

Bases Stack, Notion Suite, Dataview

Row data in note YAML. Views saved as `.base` files or fenced code blocks. Survives plugin removal.

Canonical Flat CSV Standard Format

DataDeck

Everything edits in-place inside clean canonical `.csv` files. Outlives plugins; diffs cleanly in Git.

JSON Sidecar Config Low Risk

Projects Plus (v3.7)

Record properties write to note frontmatter; custom views, dashboard blocks, and filters store in `data.json`.

Binary Sidecar (.mdb) High Lock-In

Make.md

Frontmatter stays intact, but view states, Spaces, and live formulas are trapped in binary `.mdb` files.

**Architectural Recommendation:**  For long-term longevity without binary lock-in, deploy the **Bases Modular Stack**  (Core Bases + Extended Base + Calendar Bases) or **Notion Suite** .

Verified Obsidian 1.14+

Comparison of Obsidian multi-view database solutions as of October 2026. While Core Bases (v1.14) natively handles Table, Kanban, List, Cards, and Map views, pairing it with Calendar Bases and Extended Base completes the four-view Notion paradigm without sacrificing native indexing speed. Among standalone plugins, Notion Suite and Make.md support all four views natively, whereas Projects Plus omits a compact List view in favor of multi-block Dashboards.

Data sources: [Projects Plus](https://community.obsidian.md/plugins/obs-projects-plus), [Make.md](https://obsidianmate.com/plugins/make-md), [Extended Base](https://community.obsidian.md/plugins/extended-base), [Obsidian Bases](https://obsidian.md/help/bases), [Bases Views](https://obsidian.md/help/bases/views), [Obsidian Roadmap](https://obsidian.md/roadmap/), [Obsidian Projects](https://github.com/marcusolsson/obsidian-projects), [DB Folder](https://github.com/RafaelGB/obsidian-db-folder), [DataDeck](https://community.obsidian.md/plugins/datadeck), [Dataview Guide](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/), [Calendar Bases](https://www.obsidianstats.com/plugins/calendar-bases), [Notion Suite](https://community.obsidian.md/plugins/notion-suite).

<!-- /figure 1 -->

To evaluate these solutions rigorously, an analysis must examine not only whether a plugin renders a Table, Kanban, Calendar, and List view, but also how it resolves the underlying architectural trade-offs between **data scope** , **view configuration persistence** , and **relational computation**  [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). The table below establishes the functional baseline across the primary active and legacy contenders in the Obsidian ecosystem.

| Plugin / Stack | Maintenance Status (Oct 2026) | Table View | Kanban (Board) View | Calendar View | List View | Secondary Views | Data & View Storage Model |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Obsidian Bases**  (Core v1.14) | Active (Official Core) [3](https://www.makeuseof.com/obsidian-bases-notion-database/) | Native (Editable) [3](https://www.makeuseof.com/obsidian-bases-notion-database/) | Native (Added v1.14) [9](https://obsidian.md/roadmap/) | Via API Plugin [10](https://obsidian.md/help/bases/views) | Native (Added v1.10) [9](https://obsidian.md/roadmap/) | Cards (Gallery), Map [6](https://obsidian.md/help/bases) | YAML frontmatter + `.base` file or `base` code block [6](https://obsidian.md/help/bases) |
| **Modular Bases Stack**  (*Bases + Extended Base + Calendar Bases* ) | Active (Core + Community API) [16](https://community.obsidian.md/plugins/extended-base) | Native + Notion Table [10](https://obsidian.md/help/bases/views) | Native + Notion Board [10](https://obsidian.md/help/bases/views) | Interactive (FullCalendar) [17](https://www.obsidianstats.com/plugins/calendar-bases) | Native + Notion List [10](https://obsidian.md/help/bases/views) | Cards, Map, Notion Feed [6](https://obsidian.md/help/bases) | YAML frontmatter + `.base` file [6](https://obsidian.md/help/bases) |
| **Notion Suite**  (`craigstfn`) | Active (v1.13+ required) [7](https://www.obsidianstats.com/plugins/notion-suite) | Native (Sub-items & Groups) [19](https://community.obsidian.md/plugins/notion-suite) | Native (Subgroups & WIP limits) [7](https://www.obsidianstats.com/plugins/notion-suite) | Native (Month Grid) [7](https://www.obsidianstats.com/plugins/notion-suite) | Native (Interactive To-Do) [7](https://www.obsidianstats.com/plugins/notion-suite) | Gallery, Timeline (Gantt), Charts [7](https://www.obsidianstats.com/plugins/notion-suite) | YAML frontmatter + `notion-db` code block [7](https://www.obsidianstats.com/plugins/notion-suite) |
| **Make.md**  (`make-md`) | Active (v1.0+) [24](https://community.obsidian.md/plugins/make-md) | Native (Context Table) [18](https://obsidianmate.com/plugins/make-md) | Native (Context Board) [18](https://obsidianmate.com/plugins/make-md) | Native (Context Calendar) [18](https://obsidianmate.com/plugins/make-md) | Native (Context List) [26](https://www.obsidianstats.com/plugins/make-md) | Gallery / Card, Flow Embeds [18](https://obsidianmate.com/plugins/make-md) | YAML frontmatter + Proprietary binary `.mdb` files [18](https://obsidianmate.com/plugins/make-md) |
| **Projects Plus**  (`Park Pavel`) | Active (Fork of Projects) [15](https://community.obsidian.md/plugins/obs-projects-plus) | Native (Dashboard Block) [15](https://community.obsidian.md/plugins/obs-projects-plus) | Native (Draggable Cards) [15](https://community.obsidian.md/plugins/obs-projects-plus) | Native (Year-to-Day) [15](https://community.obsidian.md/plugins/obs-projects-plus) | Unsupported [15](https://community.obsidian.md/plugins/obs-projects-plus) | Gallery, Dashboards, Charts [15](https://community.obsidian.md/plugins/obs-projects-plus) | YAML frontmatter + `.obsidian/.../data.json`[cite: 15] |
| **Dataview / Datacore**  (`blacksmithgu`) | Active / Beta (`v0.1.29`) [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) | Read-Only (DQL) / Editable (Datacore) [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) | Unsupported natively [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) | Read-Only Dot Grid (DQL) [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) | Read-Only (DQL) [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) | Task View [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) | Inline DQL / JS code blocks [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/) |
| **DataDeck**  (`SVM0N`) | Active (Beta / Community) [30](https://community.obsidian.md/plugins/datadeck) | Native (Spreadsheet) [30](https://community.obsidian.md/plugins/datadeck) | Native (Grouped Board) [30](https://community.obsidian.md/plugins/datadeck) | Habit Grid & Timeline only [30](https://community.obsidian.md/plugins/datadeck) | Unsupported (Uses Cards/Focus) [30](https://community.obsidian.md/plugins/datadeck) | Cards, Chart, Timeline, Budget, Travel Map [30](https://community.obsidian.md/plugins/datadeck) | Canonical `.csv` files + `csv-view` code block [30](https://community.obsidian.md/plugins/datadeck) |
| **Obsidian Projects**  (`Marcus Olsson`) | **Discontinued**  (May 2025) [11](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089) | Native [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev) | Native [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev) | Native [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev) | Unsupported [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev) | Gallery [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev) | YAML frontmatter + Plugin `data.json`[cite: 12, 15] |
| **DB Folder**  (`RafaelGB`) | **Archived**  (July 2025) [13](https://github.com/RafaelGB/obsidian-db-folder) | Native [13](https://github.com/RafaelGB/obsidian-db-folder) | Unsupported [32](https://forum.obsidian.md/t/replicate-notions-databases-with-relation-properties/52011) | Unsupported [32](https://forum.obsidian.md/t/replicate-notions-databases-with-relation-properties/52011) | Unsupported [32](https://forum.obsidian.md/t/replicate-notions-databases-with-relation-properties/52011) | None [32](https://forum.obsidian.md/t/replicate-notions-databases-with-relation-properties/52011) | YAML frontmatter + Custom Markdown code block [13](https://github.com/RafaelGB/obsidian-db-folder) |

## Tier 1: The Native Core Ecosystem and Bases API Extensions

### Obsidian Bases (Core Plugin)

The introduction of **Obsidian Bases**  fundamentally altered the calculus of database creation within Obsidian by moving query indexing, property editing, and view rendering into the application's core engine [3](https://www.makeuseof.com/obsidian-bases-notion-database/). Unlike Notion, where an architect creates an empty table and populates rows inside a siloed container, a Base defaults to treating the entire Obsidian vault as its data source [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). Practitioners narrow this vault-wide scope through a two-tier filtering architecture—applying global filters across the entire Base (such as restricting to a specific folder or tag) and local filters scoped to individual views—supporting nested `AND`, `OR`, and `NOT` boolean logic [10](https://obsidian.md/help/bases/views). Views are saved either as standalone `.base` files in the file explorer or embedded directly inside standard Markdown notes via `base` fenced code blocks [6](https://obsidian.md/help/bases).

As of Obsidian v1.14 (October 2026), Core Bases natively provides three of the four target Notion layouts alongside two visual layouts [6](https://obsidian.md/help/bases). The **Table View**  (introduced in v1.9) displays files as rows and YAML properties as live-editable columns, allowing users to toggle checkboxes in place, edit text and dates directly, reorder columns, group rows into collapsible sections, and compute column summaries (such as totals, averages, and counts) in a footer row [3](https://www.makeuseof.com/obsidian-bases-notion-database/). The **List View**  (added in v1.10) renders query results as a clean, low-friction list with bulleted or numbered markers, supporting multi-property sorting and collapsible group headings [6](https://obsidian.md/help/bases). The **Kanban View**  (added in v1.14) organizes files into side-by-side board columns based on any grouped property, supporting manual group creation, hiding, and drag-and-drop reordering across the board [6](https://obsidian.md/help/bases). Complementing these text and status layouts, Core Bases also includes a **Cards View**  (v1.9) for Gallery-style grids with cover images and a **Map View**  (v1.10) that plots note entries as pins on an interactive geographic map [6](https://obsidian.md/help/bases).

The primary advantage of Core Bases is raw execution speed and architectural permanence. Because it is engineered by the core Obsidian development team, it renders tables across thousands of notes nearly instantaneously—a workload where community query plugins like Dataview visibly lag or choke [3](https://www.makeuseof.com/obsidian-bases-notion-database/). Furthermore, it includes official Notion, Airtable, and CSV importers that automatically convert external database records into local Markdown files with mapped `.base` views [6](https://obsidian.md/help/bases). However, compared to Notion’s relational engine, vanilla Bases exhibits three notable weaknesses. First, it lacks a built-in month or week Calendar layout, relying instead on the v1.10 Bases API for community developers to supply calendar views [6](https://obsidian.md/help/bases). Second, because Obsidian notes exist in a flat file structure rather than isolated table schemas, Bases does not offer a point-and-click "Relation" or "Rollup" column type [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). Replicating bidirectional relations and rollups requires writing functional formula expressions—such as `file.backlinks.filter(value.asFile().properties.parent == file.name)`—coupled with `.map()` and `.reduce()` functions [8](https://www.reddit.com/r/ObsidianMD/comments/1olnsxv/q_bases_can_i_create_relations_between_tables/). While powerful, this syntax imposes a steeper technical barrier than Notion's visual relation picker, and multi-link outputs frequently render on a single cramped line [8](https://www.reddit.com/r/ObsidianMD/comments/1olnsxv/q_bases_can_i_create_relations_between_tables/). Third, clicking a note row in vanilla Bases overrides the active Base tab by default rather than opening a Notion-style side or center peek, requiring manual split-view configuration to keep the database visible while editing note body content [34](https://www.xda-developers.com/tested-obsidian-bases-against-notion-with-real-project-one-fell-apart/).

### Visual and Functional Bases Extensions: Extended Base, GoodBases, and Calendar Bases

Because Core Bases exposed a public view registration API in Obsidian v1.10, a vibrant ecosystem of modular plugins has emerged to patch every aesthetic and functional gap between vanilla Bases and Notion [6](https://obsidian.md/help/bases). Rather than building separate database engines, these plugins register as custom view types directly inside the native `.base` view switcher, inheriting native Bases filters, formulas, and sorting untouched [21](https://francescoumberto.github.io/GoodBases/).

Created by Umberto Francesco Carolini, **GoodBases**  introduced a `Notion-style table` view for Bases featuring Notion’s exact system font stack, hairline borders, row hover washes, resizable columns saved per view in the `.base` file, and a bottom `Calculate` row that adds `Count all` and percentage metrics absent from vanilla Bases [21](https://francescoumberto.github.io/GoodBases/). Crucially, it solved two major user experience complaints: it renders tags and list properties using Notion’s 9-color deterministic pill palette (complete with a custom per-value color picker and select editor), and it introduces a centered **Notion-style Page Panel**  (page peek) plus a hover-reveal `OPEN` button, allowing users to edit note titles, properties, and Live Preview Markdown bodies without leaving the database view [16](https://community.obsidian.md/plugins/extended-base).

**Extended Base**  (developed by Lucy Roh as an expanded fork of GoodBases v0.5.3, requiring Obsidian 1.10.2+) broadens this Notion aesthetic across four distinct Base layouts [16](https://community.obsidian.md/plugins/extended-base). Its **Notion Table**  layout retains all GoodBases table mechanics while adding double-click column header display renaming, searchable Lucide header icon pickers, per-column text wrapping toggles, and single-select versus multi-select pill pinning [16](https://community.obsidian.md/plugins/extended-base). Its **Notion List**  layout provides a compact vertical stacking where the note title occupies the top line and visible properties stack neatly underneath with icons, solving horizontal truncation on narrow panes [16](https://community.obsidian.md/plugins/extended-base). Its **Notion Board**  layout constructs a Kanban board from the Base's grouping configuration, complete with Notion-palette column header coloring, column width presets (`Small`, `Medium`, `Large`), a `No Status` bucket for unassigned notes, and per-column `+ New` card creation [16](https://community.obsidian.md/plugins/extended-base). While Extended Base's `Notion Board` excels visually and automatically flattens deeply nested subfolders into collapsible sections within top-level columns, it does not yet support drag-and-drop card movement between columns; practitioners requiring drag-and-drop Kanban within Bases must select the native v1.14 Kanban view or install **Kanban Bases View**  [9](https://obsidian.md/roadmap/). Finally, Extended Base adds a **Notion Feed**  view—a vertical stream of full note cards that embeds Obsidian’s live editor directly inside each card (capped at 5 cards by default for performance) for immediate long-form body editing inline—and introduces **folder-aware and nested collapsible grouping**  (`▼ / ▶`), where any group value containing `/` (or grouped by `file.folder`) automatically builds an indented hierarchical tree with cumulative descendant counts across Table and List views [16](https://community.obsidian.md/plugins/extended-base).

To supply the missing fourth view (Calendar) to Core Bases, three dedicated Bases API plugins integrate directly into the `.base` layout selector [17](https://www.obsidianstats.com/plugins/calendar-bases). **Calendar Bases**  (`edrickleong`, with over 123,000 downloads) is built on the **FullCalendar**  library and renders any filtered Base as an interactive calendar [17](https://www.obsidianstats.com/plugins/calendar-bases). It supports single-day and multi-day events mapped to configurable `startDate` and optional `endDate` YAML properties (accepting both `YYYY-MM-DD` and ISO datetime strings like `2025-10-15T10:00:00`), and supports **drag-and-drop rescheduling**  that automatically writes updated dates back to the note's YAML frontmatter [17](https://www.obsidianstats.com/plugins/calendar-bases). **Calendar Note View**  adds both a vault-wide Sidebar Calendar and a native **Bases Calendar**  view that strictly respects authoritative Base filters, sorting, and limits, rendering continuous multi-day event bars across weeks with stable horizontal lanes, Daily Notes indicators, and a compact `+` modal that invokes the public `BasesView.createFileForView()` API to instantiate pre-dated notes [41](https://community.obsidian.md/plugins/calendar-note-view). A third alternative, **Yabacavi**  (*Yet Another BAses CAlendar VIew* ), places notes as draggable cards across day, week, or month grids based on any specified date property [42](https://community.obsidian.md/plugins/yabacavi).

For practitioners who prefer the native Bases architecture but miss Notion's rollups and bulk operations, **Bases Toolbox**  adds a `Compute rollup into property` command that calculates `count`, `sum`, `average`, `min`, or `max` across linked or backlinked notes and writes the result into a real YAML property for native sorting, alongside revertible bulk property editing, conditional row and cell coloring, and find-and-replace history logs [44](https://community.obsidian.md/plugins/bases-toolbox). Similarly, **Table Rollup**  registers a custom Base view that extracts and merges Markdown tables or task lists located under identical headings (such as `Action items` or `Expenses`) across all notes filtered by the Base [45](https://community.obsidian.md/plugins/table-rollup).

## Tier 2: Standalone Multi-View Workspace Suites

For users who prefer a unified, all-in-one plugin that replicates Notion's exact container model, relational pickers, and multi-view switching without assembling modular extensions, three standalone suites dominate the ecosystem.

### Notion Suite

Released in September 2026 by developer `craigstfn` (requiring Obsidian v1.13.0+), **Notion Suite**  is purpose-built to replicate Notion's entire database and page-layout workflow while maintaining 100% plain-text Markdown purity [7](https://www.obsidianstats.com/plugins/notion-suite). Its conceptual mapping is explicit and transparent: a **Database**  is a standard vault folder, a **Row/Page**  is a `.md` note inside that folder, a **Property**  is a standard YAML frontmatter key, and a **View**  is a small `notion-db` fenced code block pasted into any note (or opened as a standalone full-tab database from the sidebar) [7](https://www.obsidianstats.com/plugins/notion-suite).

Notion Suite natively supports **six editable database views**  over the same folder data source [7](https://www.obsidianstats.com/plugins/notion-suite). Its **Table View**  provides a spreadsheet grid with inline cell editing, clickable headers for sorting and property hiding, multi-level nested filtering (up to 3 levels deep), foldable bands for `Group by` properties, footer metric calculations (`sum`, `average`, `percent checked`), and **hierarchical sub-item folding**  via twisty arrows [7](https://www.obsidianstats.com/plugins/notion-suite). Its **Board View (Kanban)**  enables drag-and-drop card management grouped by `select`, `status`, `multiselect`, or `checkbox` properties, exceeding standard Kanban plugins by supporting **horizontal subgrouping**  (e.g., grouping columns by `status` and splitting rows by `priority`), **WIP card limits**  (`limits: {Doing: 3}` with `soft`, `ask`, or `strict` enforcement modes), collapsible columns (`collapsed: [Done]`), and automatic date bucketing (`overdue`, `today`, `this week`, `later`) [7](https://www.obsidianstats.com/plugins/notion-suite). Its **Calendar View**  renders a full month grid mapped to any date property (`date: due`) with month-to-month navigation and a hover `+` button on every date cell to instantiate a note pre-populated with that date, while its **List View**  offers a compact, single-line-per-note layout that automatically transforms into an interactive, tickable to-do list whenever a checkbox property is displayed [7](https://www.obsidianstats.com/plugins/notion-suite). Additionally, Notion Suite includes a cover-image **Gallery View**  (supporting `small`, `medium`, and `large` card sizes sourced from frontmatter paths, file properties, or emojis) and a Gantt-style **Timeline View**  bounded by `start` and `end` date properties across `day`, `week`, or `month` scales [7](https://www.obsidianstats.com/plugins/notion-suite).

Notion Suite's standout strength is that it delivers Notion’s advanced relational and UI ergonomics without proprietary binary databases [19](https://community.obsidian.md/plugins/notion-suite). It natively supports 17+ property types—including GUI-configured **Relations**  (maintained as clean lists of note titles in YAML frontmatter), cross-database **Rollups** , a hand-written **Formula engine**  (`if`, `switch`, `dateBetween`, `formatDate`), auto-incrementing `uniqueid` fields with prefixes, and recurring task rules [19](https://community.obsidian.md/plugins/notion-suite). Clicking any row opens the note in a Notion-style **Side Peek**  pane beside the view rather than overwriting the active tab [7](https://www.obsidianstats.com/plugins/notion-suite). Furthermore, it includes a `/` slash command menu, local SVG charts, multi-column text layouts (`notion-columns` divided by `===`), toggle headings, breadcrumbs, and a dedicated Notion Markdown/CSV folder importer [7](https://www.obsidianstats.com/plugins/notion-suite). Its primary limitation is its folder-bound architecture and relative youth [19](https://community.obsidian.md/plugins/notion-suite). Because Notion Suite equates a database strictly with a vault folder, it is less suited than Core Bases or Projects Plus for aggregating notes scattered across disparate folders via tags or arbitrary queries [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). Additionally, as a late-2026 release, its community footprint is smaller than long-established tools, though its zero-lock-in YAML storage eliminates any risk of data loss if removed [7](https://www.obsidianstats.com/plugins/notion-suite).

### Make.md

**Make.md**  (with over 879,000 historical downloads and its v1.0+ architecture) approaches Notion replication not merely as a database plugin, but as a comprehensive UI and workspace overhaul layer on top of Obsidian [24](https://community.obsidian.md/plugins/make-md). It replaces or augments the native File Explorer with **Spaces**  (customizable collections and "Smart Spaces" that auto-populate notes based on metadata filters) and attaches **Context**  databases to folders, tags, or spaces [18](https://obsidianmate.com/plugins/make-md). Within any Space or Context, Make.md provides five core views that can be switched on the fly or embedded inline into notes as "Embedded Contexts": a spreadsheet **Table View**  mapping columns to YAML frontmatter properties, a **Board View (Kanban)**  with draggable card columns grouped by property values, a date-mapped **Calendar View** , compact customizable **List and Details Views**  for rapid scanning, and a visual **Gallery / Card View**  displaying note covers and metadata [18](https://obsidianmate.com/plugins/make-md). Beyond database views, Make.md integrates **Flow Blocks**  and **Flow Styler**  (derived in part from Hover Editor), which transform standard Markdown embeds into seamless, inline-editable Notion-like blocks, alongside visual customization via page banners, stickers, and colored folder icons [18](https://obsidianmate.com/plugins/make-md).

Make.md’s strength lies in its code-free, visual completeness: it supports two-way relational links between Contexts, live rollups, custom formulas, and workspace pinning without requiring query syntax [18](https://obsidianmate.com/plugins/make-md). However, Make.md suffers from a critical architectural vulnerability: **proprietary binary state storage**  [18](https://obsidianmate.com/plugins/make-md). While edits made to basic cell values in a Context table are written to standard YAML frontmatter in the underlying `.md` files, all organizational structures—including Space definitions, Context view layouts, column configurations, filters, sorting rules, formulas, and relation definitions—are stored in Make.md-specific binary `.mdb` database files inside the vault [18](https://obsidianmate.com/plugins/make-md). This hybrid model introduces severe operational trade-offs. Because formulas and rollups are computed live in memory and stored in `.mdb` files rather than written to Markdown, disabling Make.md causes all views, layouts, and computed values to vanish [18](https://obsidianmate.com/plugins/make-md). Furthermore, because `.mdb` files are binary databases that mutate frequently during normal navigation, they sync poorly across third-party cloud tools and generate unresolvable binary merge conflicts in Git-backed vaults—forcing technical users to explicitly add `.makemd/` and `*.mdb` to `.gitignore`, which in turn prevents view layouts from syncing across devices [18](https://obsidianmate.com/plugins/make-md). Finally, replacing the File Explorer and indexing large Contexts with numerous properties introduces noticeable startup lag and memory overhead, particularly on mobile devices, leading to documented user friction [18](https://obsidianmate.com/plugins/make-md).

### Projects Plus (Successor to Obsidian Projects)

For years, Marcus Olsson’s **Obsidian Projects**  was the gold-standard recommendation for users seeking Table, Kanban, Calendar, and Gallery views over folders or Dataview queries [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev). However, Olsson officially discontinued the plugin in May 2025 after moving away from Obsidian [11](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089). **Projects Plus**  (`obs-projects-plus`, currently at v3.7.0 and maintained by Park Pavel under the Apache 2.0 license) is the actively developed, feature-expanded successor built directly on Olsson’s codebase [15](https://community.obsidian.md/plugins/obs-projects-plus). Projects Plus ingests notes from four selectable sources—a **Folder** , a **Tag** , a **built-in filtered query** , or a **Dataview query** —and provides five interconnected view surfaces [15](https://community.obsidian.md/plugins/obs-projects-plus). Its **Table View**  operates as a configurable data block inside a Dashboard or view tab to compare records and edit YAML properties inline, while its **Board View (Kanban)**  offers status-grouped columns with draggable cards, board thumbnails, and resizable card frames [15](https://community.obsidian.md/plugins/obs-projects-plus). Its **Calendar View**  supports **year-to-day views**  for browsing meetings, deadlines, and multi-scale schedules based on date properties, and its **Gallery View**  renders a visual grid with configurable card layouts, cover images, and customizable card fields [15](https://community.obsidian.md/plugins/obs-projects-plus). As a major expansion over the original plugin, Projects Plus also introduces a **Dashboard and Charts View** , enabling users to combine record tables, summary metrics, multi-series charts (capable of plotting data across multiple projects on a second axis), and relation rollups on a single canvas [15](https://community.obsidian.md/plugins/obs-projects-plus).

Projects Plus retains its predecessor's celebrated **"Leave no trace"**  design philosophy [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev). It never pollutes Markdown notes with proprietary code blocks or plugin-specific frontmatter keys; it writes only standard YAML properties when a record is edited and stores all project definitions, view layouts, and formulas cleanly inside `.obsidian/plugins/obs-projects-plus/data.json` [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev). Additionally, Projects Plus directly resolved the two largest deficits of the original Obsidian Projects: it added **forward and reverse Rollups through Relations**  alongside a formula engine (with a formula debug panel), and it implemented **touch-first behavior on phones and tablets**  in v3.7.0, fixing the notorious mobile and iPad usability failures of Olsson's original version [15](https://community.obsidian.md/plugins/obs-projects-plus). The primary weakness of Projects Plus relative to the four-view Notion paradigm is that it **does not include a dedicated compact List view** , relying instead on Table, Board, Calendar, Gallery, and Dashboard views [15](https://community.obsidian.md/plugins/obs-projects-plus). Furthermore, because Projects Plus operates primarily inside its own workspace modal (`Show projects plus`) and stores view configurations in a monolithic `data.json` file rather than portable `.base` files or inline Markdown code blocks, it functions more like an isolated project management suite ("Jira offline") inside Obsidian than an inline document database [11](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089).

## Tier 3: Query Engines, Specialized Formats, and Legacy Alternatives

### Dataview and Datacore

No analysis of Obsidian databases is complete without addressing **Dataview**  and its work-in-progress successor, **Datacore**  (both authored by Michael Brenan / `blacksmithgu`) [56](https://www.obsidianstats.com/tags/front-matter). Dataview indexes YAML frontmatter, inline fields (`key:: value`), tags, links, and tasks, exposing them via the pipeline-based Dataview Query Language (DQL) and DataviewJS [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/). DQL natively supports four query outputs: `TABLE`, `LIST`, `TASK`, and `CALENDAR` [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/). While this covers three of the four target views (Table, List, Calendar), Dataview is fundamentally a **read-only rendering engine**  (with the sole exception of ticking task checkboxes) and lacks a native Kanban view [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/). Moreover, its `CALENDAR` query renders a minimal dot-matrix indicator grid requiring strict `typeof(due) = "date"` guards rather than a Notion-style card calendar where event titles are legible and draggable [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/). In 2026, architectural best practices dictate reaching for Core Bases first for interactive dashboards while reserving Dataview for inline sentence queries, task-level aggregations across daily notes, and arbitrary JavaScript computation [3](https://www.makeuseof.com/obsidian-bases-notion-database/).

Meanwhile, **Datacore**  (currently in public beta at `v0.1.29`) re-architects Dataview around a React-based UI with 2–10x faster indexing, background rate-limiting so vault startup incurs zero lag, section- and block-level query granularity (indexing Markdown sections, tasks, Canvas files, images, videos, and PDFs), and interactive WYSIWYG tables that support inline editing and pagination [29](https://www.obsidianstats.com/plugins/datacore). However, Datacore remains focused on programmatic queries and interactive tables and embeds rather than providing a turnkey, code-free Table, Kanban, Calendar, and List switcher for general users [29](https://www.obsidianstats.com/plugins/datacore).

### Format- and Domain-Specific Multi-View Engines

Several active plugins replicate Notion's multi-view paradigm for specialized data substrates or task-specific workflows. For practitioners managing high-density tabular datasets where creating thousands of individual `.md` files is undesirable, **DataDeck**  (`SVM0N`) turns standard `.csv` files directly into an 11-view interactive database encompassing `Table`, `Cards`, `Kanban`, `Chart`, `Dashboard`, `Tasks`, `Timeline`, `Budget`, `Stats`, `Focus`, and an interactive world choropleth `Travel` map [30](https://community.obsidian.md/plugins/datadeck). All inline edits write directly back to the canonical `.csv` file with zero lock-in, and views can be embedded in notes via `csv-view` code blocks [30](https://community.obsidian.md/plugins/datadeck). While DataDeck lacks a standard monthly event calendar (offering a GitHub-style habit calendar and a Gantt `Timeline` instead) and substitutes `Cards` and `Focus` modes for a compact `List` view, it is unmatched for spreadsheet-backed multi-view analysis [30](https://community.obsidian.md/plugins/datadeck). Conversely, if the primary objective of Notion emulation is project and task tracking, **Project Manager for Obsidian**  (`project-manager-enhanced`) provides `Table`, `Kanban`, and interactive `Gantt` (Timeline) views over plain Markdown/YAML files, complete with dependency arrows, cycle-detected smart scheduling (auto-shifting dependent task dates when a blocker moves), time logging, and multi-select batch actions [60](https://community.obsidian.md/plugins/project-manager-enhanced). Similarly, **TaskNotes**  pairs with Core Bases and dashboard plugins like **Hearth**  to render one-note-per-task vaults across Kanban, Calendar, Agenda, and Task List views with Google Calendar and Outlook time-blocking [61](https://community.obsidian.md/plugins/hearth).

### Deprecated First-Generation Plugins to Avoid in New Deployments

Because outdated tutorials from 2022–2024 continue to circulate, system architects designing vaults in late 2026 should explicitly avoid building new workflows around four legacy tools. First, Marcus Olsson's **Obsidian Projects**  (`marcusolsson/obsidian-projects`) was officially discontinued in May 2025; existing users should migrate directly to **Projects Plus**  (`obs-projects-plus`) or **Core Bases**  [11](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089). Second, RafaelGB's **DB Folder**  (`RafaelGB/obsidian-db-folder`) had its repository permanently archived as read-only on July 28, 2025; despite early roadmap aspirations for multiple views, it remained restricted to Table views and suffered from React-table cell-saving quirks [13](https://github.com/RafaelGB/obsidian-db-folder). Third, **DataLoom**  was archived in its original repository and relied on proprietary `.loom` JSON files rather than standard Markdown notes [14](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/); while a community maintenance fork exists, its developer explicitly restricted its scope to Table views only [65](https://www.reddit.com/r/ObsidianMD/comments/1us0xxv/update_dataloom_is_no_longer_deprecated_a_fork_is/). Fourth, **Metadata Menu**  (`mdelobelle`), while still useful for power users who desire `fileClass` schema definitions, required-field validation, and right-click context menu editing of frontmatter and inline fields, was originally engineered to feed Dataview prior to Obsidian shipping native Properties and Bases, and only surfaces a single `fileClass` table view rather than a multi-view Kanban or Calendar suite [66](https://mdelobelle.github.io/metadatamenu/).

## Architectural Trade-Offs: Persistence, Relational Mechanics, and Sync

Selecting the optimal multi-view solution requires evaluating how each architecture handles three deep structural mechanics: **data scope versus schema enforcement** , **relational rollup persistence** , and **multi-device synchronization integrity**  [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c).

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### Core Bases Leads in Speed and Sync Safety While Notion Suite and Projects Plus Bridge the Relational Gap

Architectural evaluation matrix comparing Obsidian's top four multi-view solutions across six critical engineering dimensions.

Evaluation Tiers:

**Tier 4:**  Optimal / Native    **Tier 3:**  Strong Implementation    **Tier 2:**  Workaround Required    **Tier 1:**  Limitation / Risk

Filter by Technical Dimension:

**Interactive Scorecard:**  Click any dimension above to highlight and isolate technical trade-offs across all 4 architectures simultaneously.

#### Modular Core Bases Stack

.base + YAML Frontmatter

Target: **Scalability Purists & Git Power Users**

1. Indexing Speed

T4

Instant native C++/TS core engine for thousands of notes

2. Git & Sync Safety

T4

100% diffable plain-text .base and note YAML files

3. UI/UX Fidelity

T3

Extended Base Notion views, pills, and Page Panel

4. Relations & Rollups

T2

Formula link scripts or Bases Toolbox batch calculations

5. Query Scope

T4

Native vault-wide filtering and folder-independent queries

6. Mobile Ergonomics

T3

Native Obsidian mobile speed; board drag-and-drop evolving

#### Notion Suite

YAML Frontmatter + notion-db

Target: **Notion Switchers & Visual Organizers**

1. Indexing Speed

T3

Fast local TS scanning; in-memory folder indexing

2. Git & Sync Safety

T4

Plain markdown notes with clean frontmatter property edits

3. UI/UX Fidelity

T4

Pixel-perfect Notion clone: Side Peek, / slash, 6 views

4. Relations & Rollups

T4

Point-and-click relations, formula parser, and rollups

5. Query Scope

T2

Folder-centric architecture (1 database = 1 vault folder)

6. Mobile Ergonomics

T3

Multi-column auto-collapse; smooth touch card dragging

#### Projects Plus

YAML Frontmatter + data.json

Target: **Dashboard Builders & Dataview Users**

1. Indexing Speed

T3

Obsidian API cached reads; smooth on large projects

2. Git & Sync Safety

T3

Note YAML is safe; view configs in data.json risk clashes

3. UI/UX Fidelity

T3

Polished Obsidian-native dashboards, boards, and galleries

4. Relations & Rollups

T4

Reverse backlinks rollups and multi-axis chart metrics

5. Query Scope

T4

Unrestricted queries via Folders, Tags, and Dataview

6. Mobile Ergonomics

T4

Dedicated touch-first behavior and resizable card frames

#### Make.md

Binary .mdb + YAML Frontmatter

Target: **All-in-One Notion-Style UI Explorers**

1. Indexing Speed

T2

Notable startup overhead on large Contexts & properties

2. Git & Sync Safety

T1

Binary .mdb breaks Git diffs; silent sync collisions

3. UI/UX Fidelity

T4

Full workspace reskin with Flow blocks and Context views

4. Relations & Rollups

T3

Live 2-way relations stored in .mdb; lost without plugin

5. Query Scope

T2

Bound to Spaces/Contexts; lacks vault schema enforcement

6. Mobile Ergonomics

T1

Heavy explorer injection causes noticeable startup lag

#### ⚡ System Schematic: The Binary Sidecar Trap vs. Plain-Text Permanence

Architecture Reality

✓ Plain-Text Permanence (.base & YAML)

**Core Bases, Notion Suite & Projects Plus:**  All notes, properties, and queries remain human-readable Markdown and structured YAML. Instant Git branching, zero conflict locks, total longevity even if plugins are removed.

⚠ The Binary Sidecar Trap (.mdb in Make.md)

**Make.md:**  Contexts, relations, and computed formulas reside in opaque binary `.mdb` files. Cannot be diffed in Git, risks catastrophic multi-device sync clobbers, and layout disappears if disabled.

Architectural trade-off comparison across the four leading multi-view solutions in Obsidian. The Modular Core Bases Stack achieves maximum marks for large-vault indexing speed and Git/Sync safety due to its native C++/TS core engine and plain-text *.base*  files, but trails Notion Suite and Projects Plus in point-and-click relational rollups. Make.md offers strong visual polish but incurs severe penalties in Git/Sync safety and mobile performance due to its binary *.mdb*  storage.

Data sources: [MakeUseOf (Obsidian Bases)](https://www.makeuseof.com/obsidian-bases-notion-database/), [Obsidian Extended Base](https://community.obsidian.md/plugins/extended-base), [Obsidian Notion Suite](https://community.obsidian.md/plugins/notion-suite), [Obsidian Projects Plus](https://community.obsidian.md/plugins/obs-projects-plus), [ObsidianMate (Make.md)](https://obsidianmate.com/plugins/make-md), [Bases Toolbox](https://community.obsidian.md/plugins/bases-toolbox), [Calendar Bases](https://www.obsidianstats.com/plugins/calendar-bases), [Medium (Obsidian Git Sync)](https://medium.com/@askar.zhakenov/obsidian-git-sync-on-android-with-termux-and-lfs-c5bb05e0f1cc).

<!-- /figure 2 -->

### Data Scope Versus Schema Enforcement

A critical second-order consequence of migrating from Notion to Obsidian is discovering that **Markdown files do not enforce a table schema**  [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). In Notion, every row in a database automatically inherits the exact columns and property types defined by the parent container [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). In Obsidian, because properties live in individual note YAML headers, two notes in the same folder can have mismatched property types or missing keys, which can produce inconsistent sorting results in schema-less plugins like Make.md [18](https://obsidianmate.com/plugins/make-md). **Core Bases**  embraces this bottom-up flexibility by treating the entire vault as a schema-less pool and filtering down [5](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c). When a user creates a new note via the `+ New` button inside a filtered Base view (or inside a **Calendar Note View**  or **Extended Base**  group), the view automatically populates the new note's frontmatter with the active filter or group properties so it remains visible in that view [16](https://community.obsidian.md/plugins/extended-base). Conversely, **Notion Suite**  and **Projects Plus**  counteract schema drift more aggressively: Notion Suite binds a schema definition to a specific folder and provides dedicated new-item forms and bulk property editors [19](https://community.obsidian.md/plugins/notion-suite), while Projects Plus lets users configure explicit project note templates that instantiate standardized frontmatter keys upon record creation [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev).

### Relational Integrity and Rollup Computation

Practitioners whose Notion workflows rely heavily on interconnected databases—such as linking `Projects` to `Tasks` and `Clients` with live completion percentage and budget rollups—face a sharp architectural fork in Obsidian [7](https://www.obsidianstats.com/plugins/notion-suite). In **Core Bases** , relational links are simply standard Obsidian wikilinks (`[[Project A]]`) stored inside text or list properties [8](https://www.reddit.com/r/ObsidianMD/comments/1olnsxv/q_bases_can_i_create_relations_between_tables/). While this keeps notes 100% native and visible in Obsidian's Graph View, aggregating values across linked notes requires chaining functional formulas (`file.backlinks.filter(...).map(...)`) combined with `.reduce()` [8](https://www.reddit.com/r/ObsidianMD/comments/1olnsxv/q_bases_can_i_create_relations_between_tables/), or running one-shot static calculations via **Bases Toolbox**  that write rollup results into frontmatter [44](https://community.obsidian.md/plugins/bases-toolbox). By contrast, in **Notion Suite**  and **Projects Plus** , relations and rollups are first-class GUI citizens [7](https://www.obsidianstats.com/plugins/notion-suite). Notion Suite maintains relations as an array of note titles in YAML frontmatter and computes live rollups (sums, counts, percent checked) across related database folders without requiring code [7](https://www.obsidianstats.com/plugins/notion-suite). Projects Plus similarly computes both forward rollups (through a relation property) and reverse rollups (automatically totaling records from other projects that link back to the active note) [15](https://community.obsidian.md/plugins/obs-projects-plus). In **Make.md** , two-way relations and rollups are computed live and managed inside its `.mdb` binary layer; unless a relation is explicitly mirrored to a frontmatter link, the relational graph remains trapped inside the plugin's proprietary database [18](https://obsidianmate.com/plugins/make-md).

### Multi-Device Synchronization, Git Version Control, and Mobile Ergonomics

For local-first practitioners, how a plugin persists view configurations directly dictates whether a vault can be safely synced via Obsidian Sync, iCloud, Syncthing, or Git [18](https://obsidianmate.com/plugins/make-md). Plugins that store view definitions in **native `.base` files or inline Markdown code blocks** —namely **Core Bases** , **Extended Base** , **Calendar Bases** , and **Notion Suite** —offer optimal Git and multi-device sync reliability because all view parameters are human-readable YAML/text lines that diff cleanly and sync instantaneously alongside `.md` notes [6](https://obsidian.md/help/bases). Plugins that rely on a **centralized plugin `data.json` file** —such as **Projects Plus** —keep Markdown notes completely free of view code blocks, but require syncing the `.obsidian/plugins/` configuration folder across devices and can trigger JSON merge conflicts if view settings are modified concurrently on multiple machines [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev). At the opposite extreme, **Make.md’s binary sidecar (`.mdb`) architecture**  introduces severe multi-device friction: binary `.mdb` files cannot be merged in Git, frequently conflict over cloud drives, and require explicit exclusion in `.gitignore` for stable version control [18](https://obsidianmate.com/plugins/make-md).

| Persistence Architecture | Representative Plugins | Git & Diff Friendliness | Cross-Device Sync Reliability | Removal / Degradation Behavior |
| --- | --- | --- | --- | --- |
| **Native `.base` / Inline Markdown Code Blocks** | **Core Bases** , **Extended Base** , **Calendar Bases** , **Notion Suite** | **Optimal:**  View configs are human-readable YAML/text blocks that diff cleanly line-by-line in Git [6](https://obsidian.md/help/bases). | **Optimal:**  Syncs instantaneously alongside standard `.md` files with zero binary corruption risk [6](https://obsidian.md/help/bases). | Notes and YAML remain 100% intact; inline code blocks remain readable as plain text parameters [6](https://obsidian.md/help/bases). |
| **Centralized Plugin `data.json`** | **Projects Plus**  (and legacy **Obsidian Projects** ) | **Moderate:**  All project views live in `.obsidian/plugins/obs-projects-plus/data.json`; concurrent edits can cause JSON merge conflicts [15](https://community.obsidian.md/plugins/obs-projects-plus). | **High (if `.obsidian` is synced):**  Requires enabling plugin settings sync across devices [15](https://community.obsidian.md/plugins/obs-projects-plus). | **Zero Trace:**  Notes contain zero code blocks or plugin artifacts; only standard YAML properties remain [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev). |
| **Proprietary Binary Sidecars (`.mdb`)** | **Make.md** | **Poor:**  Binary `.mdb` files cannot be merged in Git and must typically be added to `.gitignore` [18](https://obsidianmate.com/plugins/make-md). | **Fragile:**  Binary database files frequently conflict or desync over cloud drives and add mobile startup lag [18](https://obsidianmate.com/plugins/make-md). | Notes and raw YAML survive, but all Spaces, views, filters, relations, and live formula values are lost [18](https://obsidianmate.com/plugins/make-md). |

## Strategic Recommendations by Workflow Profile

Because no single plugin is universally optimal across every operational context, selecting the right architecture depends on which aspect of Notion’s database model is paramount to the target workflow. The decision matrix below maps specific functional requirements to the optimal Obsidian configuration.

| Primary Workflow Profile | Recommended Plugin Stack | Supported Views | Key Architectural Advantage | Primary Trade-Off to Accept |
| --- | --- | --- | --- | --- |
| **Long-Term Stability, Vault-Wide Speed & Notion Aesthetics** | **Core Bases (v1.14)**  + **Extended Base**  + **Calendar Bases**  (+ *Bases Toolbox* ) [10](https://obsidian.md/help/bases/views) | Table, Kanban, Calendar, List, Cards, Map, Feed [6](https://obsidian.md/help/bases) | Instantaneous native C++/TS indexing across thousands of notes; 100% plain-text `.base` storage; Page Panel peek & colored pills [3](https://www.makeuseof.com/obsidian-bases-notion-database/). | Cross-table relations and live rollups require functional formula syntax or one-shot toolbox commands [8](https://www.reddit.com/r/ObsidianMD/comments/1olnsxv/q_bases_can_i_create_relations_between_tables/). |
| **Turnkey 1:1 Notion Clone with GUI Relations & Slash Menu** | **Notion Suite**  (`craigstfn`) [19](https://community.obsidian.md/plugins/notion-suite) | Table, Board (Kanban), Calendar, List, Gallery, Timeline (Gantt) [7](https://www.obsidianstats.com/plugins/notion-suite) | Point-and-click two-way Relations, Rollups, sub-item folding, Kanban WIP limits/subgroups, Side Peek, and `/` menu in pure YAML [7](https://www.obsidianstats.com/plugins/notion-suite). | Databases are strictly folder-bound rather than vault-wide queries; newer ecosystem entrant (Sep 2026) [7](https://www.obsidianstats.com/plugins/notion-suite). |
| **Multi-Project Portfolios, Cross-Project Charts & Zero-Trace Notes** | **Projects Plus**  (`Park Pavel`) [15](https://community.obsidian.md/plugins/obs-projects-plus) | Table (Dashboard Block), Board, Calendar, Gallery, Chart Dashboards [15](https://community.obsidian.md/plugins/obs-projects-plus) | "Leave no trace" architecture keeps `.md` files completely clean; supports forward/reverse rollups, multi-project charts, and touch-first mobile UI [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev). | Lacks a compact List view; operates inside a dedicated workspace modal stored in `data.json` [15](https://community.obsidian.md/plugins/obs-projects-plus). |
| **High-Row Tabular Datasets Without Individual Note Clutter** | **DataDeck**  (`SVM0N`) [30](https://community.obsidian.md/plugins/datadeck) | Table, Kanban, Cards, Timeline, Chart, Dashboard, Budget, Travel Map [30](https://community.obsidian.md/plugins/datadeck) | Edits canonical `.csv` files directly in place without generating thousands of individual `.md` files [30](https://community.obsidian.md/plugins/datadeck). | Lacks a standard monthly event calendar and substitutes Cards/Focus for List view [30](https://community.obsidian.md/plugins/datadeck). |
| **Visual Workspace Overhaul & Inline Flow Editing** | **Make.md**  (`make-md`) [18](https://obsidianmate.com/plugins/make-md) | Table, Board, Calendar, List, Gallery [18](https://obsidianmate.com/plugins/make-md) | Code-free Spaces, banners, stickers, two-way relations, and inline Flow Block editing [18](https://obsidianmate.com/plugins/make-md). | Stores views, filters, and formulas in binary `.mdb` files that break Git diffs and add mobile startup overhead [18](https://obsidianmate.com/plugins/make-md). |

For the vast majority of practitioners seeking to replicate Notion’s Table, Kanban, Calendar, and List views in late 2026, deploying **Core Obsidian Bases (v1.14)**  paired with **Extended Base**  and **Calendar Bases**  represents the most resilient, high-performance architecture [3](https://www.makeuseof.com/obsidian-bases-notion-database/). This modular stack natively delivers all four required layouts—combining native and Notion-styled Tables, v1.14 drag-and-drop Kanban and Notion Boards, native and stacked Notion Lists, and FullCalendar drag-and-drop rescheduling—alongside Cards, Map, and Feed views [6](https://obsidian.md/help/bases). It guarantees instantaneous indexing over tens of thousands of files, 100% plain-text `.base` portability, and Notion-grade visual polish including colored value pills, collapsible folder trees, and a centered Page Panel peek view [3](https://www.makeuseof.com/obsidian-bases-notion-database/). Where static rollups or bulk property edits are required on top of this stack, adding **Bases Toolbox**  bridges the gap cleanly [44](https://community.obsidian.md/plugins/bases-toolbox).

Conversely, when a workflow is organized strictly around folder-based databases and demands turnkey point-and-click two-way **Relations** , cross-database **Rollups** , hierarchical **sub-items** , Kanban **WIP limits and subgrouping** , **Side Peek**  editing, and a `/` slash command menu without writing functional formulas, **Notion Suite**  provides all six views (**Table, Board, Calendar, List, Gallery, Timeline** ) out of the box while keeping every byte of data in plain Markdown frontmatter and `notion-db` blocks [7](https://www.obsidianstats.com/plugins/notion-suite). Finally, for practitioners managing dedicated client portfolios, editorial calendars, or cross-project financial dashboards who require their underlying `.md` files to remain completely free of embedded database code blocks for external sharing, **Projects Plus**  is the premier choice—provided a compact List view is not required—while **DataDeck**  and **Make.md**  should be reserved for specialized `.csv`-backed tables and single-device visual workspaces, respectively [12](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev).

## Sources used in the report

1. [How well can you replicate Notion in Obsidian? - Reddit](https://www.reddit.com/r/ObsidianMD/comments/14vybi9/how_well_can_you_replicate_notion_in_obsidian/)
2. [Notion vs Obsidian: which should you choose in 2026? - Fabric.so](https://fabric.so/comparison/notion-vs-obsidian)
3. [Obsidian finally fixed the one thing Notion always did better](https://www.makeuseof.com/obsidian-bases-notion-database/)
4. ["Best Obsidian Alternatives in 2026: 11 Note-Taking and Knowledge](https://resources.rework.com/tools/productivity/best-obsidian-alternatives)
5. [Are Obsidian Bases the Same as Notion Database? | by Moy - Medium](https://medium.com/@moyfoxther/are-obsidian-bases-the-same-as-notion-database-411c4136965c)
6. [Introduction to Bases - Obsidian Help](https://obsidian.md/help/bases)
7. [Notion Suite – Obsidian Plugin](https://www.obsidianstats.com/plugins/notion-suite)
8. [[Q] Bases - can I create relations between tables? : r/ObsidianMD](https://www.reddit.com/r/ObsidianMD/comments/1olnsxv/q_bases_can_i_create_relations_between_tables/)
9. [Obsidian Roadmap](https://obsidian.md/roadmap/)
10. [Views - Obsidian Help](https://obsidian.md/help/bases/views)
11. [Development for Projects plugin needed - Obsidian Forum](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089)
12. [obsmd-projects/obsidian-projects at marcusolsson.dev - GitHub](https://github.com/marcusolsson/obsidian-projects?ref=marcusolsson.dev)
13. [GitHub - RafaelGB/obsidian-db-folder: Obsidian Plugin to Allow](https://github.com/RafaelGB/obsidian-db-folder)
14. [The Complete Guide to Dataview in Obsidian - Query Everything](https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/)
15. [Projects Plus - Obsidian Plugin](https://community.obsidian.md/plugins/obs-projects-plus)
16. [Extended Base - Obsidian Plugin](https://community.obsidian.md/plugins/extended-base)
17. [Calendar Bases – Obsidian Plugin](https://www.obsidianstats.com/plugins/calendar-bases)
18. [Make.md for Obsidian: Features, Installation & Examples](https://obsidianmate.com/plugins/make-md)
19. [Notion Suite - Obsidian Plugin](https://community.obsidian.md/plugins/notion-suite)
20. [Calendar Bases - Obsidian Plugin](https://community.obsidian.md/plugins/calendar-bases)
21. [GoodBases — Notion-style tables for Obsidian Bases - GitHub Pages](https://francescoumberto.github.io/GoodBases/)
22. [Obsidian Plugin Updates 2026-09-13 to 2026-09-19 - Obsidian Stats](https://www.obsidianstats.com/posts/2026-09-20-weekly-updates)
23. [Obsidian plugins with #notion - 3 plugins](https://www.obsidianstats.com/tags/notion)
24. [make.md - Obsidian Plugin](https://community.obsidian.md/plugins/make-md)
25. [Make.md 1.0 is now available, organization and personalization for](https://www.reddit.com/r/ObsidianMD/comments/1hmdsf6/makemd_10_is_now_available_organization_and/)
26. [MAKE.md – Obsidian Plugin](https://www.obsidianstats.com/plugins/make-md)
27. [Make.md has been updated! : r/ObsidianMD - Reddit](https://www.reddit.com/r/ObsidianMD/comments/12nt6qv/makemd_has_been_updated/)
28. [obs-projects-plus/NOTICE at main - GitHub](https://github.com/ParkPavel/obs-projects-plus/blob/main/NOTICE)
29. [Datacore – Obsidian Plugin](https://www.obsidianstats.com/plugins/datacore)
30. [DataDeck - Obsidian Plugin](https://community.obsidian.md/plugins/datadeck)
31. [[FR] filters inside DB using data view · Issue #33 · RafaelGB ... - GitHub](https://github.com/RafaelGB/obsidian-db-folder/issues/33)
32. [Replicate Notion's 'databases', with relation properties? - Help](https://forum.obsidian.md/t/replicate-notions-databases-with-relation-properties/52011)
33. [What are the differences between various database plugins?](https://forum.obsidian.md/t/what-are-the-differences-between-various-database-plugins/39406)
34. [I tested Obsidian Bases against Notion with a real project, and one](https://www.xda-developers.com/tested-obsidian-bases-against-notion-with-real-project-one-fell-apart/)
35. [Bases Paginator - Obsidian Plugin](https://community.obsidian.md/plugins/bases-paginator)
36. [PSA: Some Clarity on Bases : r/ObsidianMD - Reddit](https://www.reddit.com/r/ObsidianMD/comments/1mvfoys/psa_some_clarity_on_bases/)
37. [Self-hosted Notion alternatives, compared - SSD Nodes](https://www.ssdnodes.com/learn/self-hosted-notion-alternatives)
38. [Would Bases have Bidirectional Relations? : r/ObsidianMD - Reddit](https://www.reddit.com/r/ObsidianMD/comments/1lsqs2b/would_bases_have_bidirectional_relations/)
39. [Using Bases for relational data. (aka my Obsidian dreams have](https://www.reddit.com/r/ObsidianMD/comments/1miupny/using_bases_for_relational_data_aka_my_obsidian/)
40. [I built a Bases view that makes your tables look exactly like Notion](https://www.reddit.com/r/ObsidianMD/comments/1u2zfuu/i_built_a_bases_view_that_makes_your_tables_look/)
41. [Calendar Note View - Obsidian Plugin](https://community.obsidian.md/plugins/calendar-note-view)
42. [Yabacavi - Obsidian Plugin](https://community.obsidian.md/plugins/yabacavi)
43. [GitHub - edrickleong/obsidian-calendar-bases](https://github.com/edrickleong/obsidian-calendar-bases)
44. [Bases Toolbox - Obsidian Plugin](https://community.obsidian.md/plugins/bases-toolbox)
45. [Table Rollup - Obsidian Plugin](https://community.obsidian.md/plugins/table-rollup)
46. [Best Obsidian Plugins (2026) - Must-Have Community & AI Plugins](https://obsidianmate.com/plugins)
47. [Getting Started - make.md](https://www.make.md/docs/Getting%20Started)
48. [3 Obsidian plugins that actually changed how I work](https://www.xda-developers.com/obsidian-plugins-that-actually-changed-how-i-work/)
49. [Obsidian Git Sync on Android with Termux and LFS - Medium](https://medium.com/@askar.zhakenov/obsidian-git-sync-on-android-with-termux-and-lfs-c5bb05e0f1cc)
50. [Notebook Navigator 3.1 brings Scrivener-style sidebars to Obsidian!](https://www.reddit.com/r/ObsidianMD/comments/1tz3qlq/notebook_navigator_31_brings_scrivenerstyle/)
51. [Obsidian needs a proper database feature : r/ObsidianMD - Reddit](https://www.reddit.com/r/ObsidianMD/comments/1gzghto/obsidian_needs_a_proper_database_feature/)
52. [obsidian-projects vs obsidian-kanban - compare differences and](https://www.libhunt.com/compare-obsidian-projects-vs-obsidian-kanban)
53. [Best Kanban Plugin for Obsidian : r/ObsidianMD - Reddit](https://www.reddit.com/r/ObsidianMD/comments/1b8sdnh/best_kanban_plugin_for_obsidian/)
54. [Projects Plus – Obsidian Plugin · Obsidian Stats](https://www.obsidianstats.com/plugins/obs-projects-plus)
55. [Mindset around community plugins and obsidian/markdown as a](https://www.reddit.com/r/ObsidianMD/comments/1bp0dn9/mindset_around_community_plugins_and/)
56. [Obsidian plugins with #front-matter - 50 plugins](https://www.obsidianstats.com/tags/front-matter)
57. [GitHub - blacksmithgu/datacore: Work-in-progress successor to](https://github.com/blacksmithgu/datacore)
58. [Tres Brenan blacksmithgu - GitHub](https://github.com/blacksmithgu)
59. [ROADMAP.md - blacksmithgu/datacore - GitHub](https://github.com/blacksmithgu/datacore/blob/master/ROADMAP.md)
60. [Project Manager Enhanced - Obsidian Community Plugins](https://community.obsidian.md/plugins/project-manager-enhanced)
61. [Hearth - Obsidian Plugin](https://community.obsidian.md/plugins/hearth)
62. [Manage Everything in Obsidian with TaskNotes - YouTube](https://www.youtube.com/watch?v=2dEQ1ES8_6A)
63. [Bases x TaskNotes (update 3.23.0) : r/ObsidianMD - Reddit](https://www.reddit.com/r/ObsidianMD/comments/1nblri0/bases_x_tasknotes_update_3230/)
64. [How to Create a Habit Tracker in Obsidian That You'll Actually Use](https://www.reddit.com/r/ObsidianMD/comments/w6zf6r/how_to_create_a_habit_tracker_in_obsidian_that/)
65. [Update: DataLoom is no longer deprecated, a fork is maintaining it](https://www.reddit.com/r/ObsidianMD/comments/1us0xxv/update_dataloom_is_no_longer_deprecated_a_fork_is/)
66. [Metadata Menu](https://mdelobelle.github.io/metadatamenu/)
67. [Fileclass - Obsidian Plugin](https://community.obsidian.md/plugins/fileclass)
68. [Metadata Menu - Obsidian Plugin](https://community.obsidian.md/plugins/metadata-menu)
69. [Obsidian vs Notion: Which tool is right for you? - Slite](https://slite.com/learn/obsidian-vs-notion)
