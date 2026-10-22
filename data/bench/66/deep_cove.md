# Obsidian Plugins That Recreate Notion’s Table, Kanban, Calendar, and List Views

**The best standalone choices:** **Notion Bases** is the clearest single-plugin replacement for Notion’s four requested database views, while **Note Database** offers particularly rich editing and customization. Both explicitly provide Table, Board/Kanban, Calendar, and List views over Markdown-backed records. For users who prefer Obsidian’s native database system, **Core Bases plus Power Bases** is the strongest general-purpose combination because its views share one Base and ordinary note properties. [1] · Note Database [2] · [3]

**The main distinction:** Four visual layouts are useful only if they operate on the same records. Database Views and Rowbase are capable partial alternatives, but adding a separate calendar does not automatically make their database-file records and calendar notes synchronize.

| Option | Requested-view coverage | Source of truth | Best fit |
|---|---|---|---|
| Notion Bases | 4/4 in one community plugin | Markdown notes/frontmatter | Closest straightforward standalone match |
| Note Database | 4/4 in one community plugin | Markdown notes/frontmatter | Rich editing and configurable views |
| Core Bases + Power Bases | 4/4 in one Base | Notes plus `.base` configuration | Best general native-Bases stack |
| Core Bases + Kanban Action Planner | 4/4 using Core Table/List | Notes plus `.base` configuration | Planning, statuses, relationships |
| Newer Core Bases + TaskNotes | 4/4 using native Core Kanban | Notes plus `.base` configuration | Recurrence and external calendars |
| Database Views | 3/4: Table, Kanban, List | `.dbview` records | Simple database-style workspace |
| Rowbase | 3/4: Table, Kanban, List | `.rbase` records | Offline formulas and relations |
| Dataview | Three visual families; read-oriented | Indexed note metadata | Query dashboards and indexes |
| Full Calendar Remastered | Calendar specialist | Event notes or provider records | Recurrence and calendar integration |

**How the comparison proceeds:** First, establish what makes Notion’s views genuinely connected. Then compare the candidates’ coverage, their behavior in each requested view, and the practical consequences of storage, mobile support, maintenance, and collaboration. The comparison is dated September 13, 2026, with release-specific differences identified where they affect the recommendation.

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Turn any folder into a Notion-style database with Table, Board (Kanban), Gallery, List, Calendar, Timeline (Gantt), and Chart views — powered by plain Markdown and frontmatter. Your data stays yours, always. Now availa…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Local-first database views for Obsidian notes: table, board, gallery, list, chart, calendar, timeline, formulas, filters, and inline editing. Turn Markdown notes into editable, visual databases inside Obsidian. Eight v…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "Six extra views for Obsidian's core Bases plugin: a kanban board, a calendar, a Gantt-style timeline, a chart, an image gallery, and a much richer table. Your rows stay ordinary notes and the data stays in ordinary fro…"

## What needs to match Notion

### Four views must share one record set

**Notion’s essential advantage:** Table, Board, Calendar, and List are different presentations of database pages, not separate collections that users must reconcile. A page’s properties remain the same when the page appears in another view. Notion’s official documentation explicitly describes switching the same database among these layouts. [4]

| Notion view | What it represents | Important behavior |
|---|---|---|
| Table | Pages as rows; properties as columns | Property editing, sorting, calculations |
| Board/Kanban | Pages grouped by a property | Status-oriented organization and movement |
| Calendar | Pages positioned by a Date property | Monthly/weekly layouts and dated-page creation |
| List | Compact presentation of database pages | Minimal display with shared properties |

**View settings stay separate:** Each Notion view can have its own visible properties, filters, sorts, grouping, and sub-grouping. Advanced filters combine AND/OR conditions in groups nested up to three levels, and multiple sort priorities can be reordered. Changing a view’s organization does not require changing the records themselves. [4]

**Record edits propagate:** Notion makes the distinction especially clear for linked data sources: edits to pages, titles, and properties affect the original source, while filters, sorts, and groups belong to the linked presentation. That is the appropriate standard for an Obsidian replacement—not simply whether it can display a board beside a calendar. [5]

**A useful illustrative workflow:** An editorial database might show every draft in a Table, group those drafts by `status` on a Board, position them by `publish_date` on a Calendar, and present upcoming work as a compact List. Effective replication means that changing a draft’s status or publication date updates the underlying record used by the other views.

Section references:
[4] Notion database views <https://www.notion.com/help/views-filters-and-sorts> Excerpt: "Note: Table, Board, List & Timeline layouts will open pages in side peek by default. Gallery & Calendar layouts will open pages in center peek by default. Notion makes it easy to filter your database so it only displays the items that meet specific criteria.…"
[5] Notion linked data sources <https://www.notion.com/help/data-sources-and-linked-databases> Excerpt: "When interacting with a linked data source, the views, filters, sorts, and groups you create and delete will not affect the views on the original database. However, when you edit the data source’s title, properties, or pages those edits will be reflected in t…"

### Properties and editing matter as much as layouts

**Notion’s property baseline:** Its database fields include dates and date ranges, numbers, statuses, multi-selects, formulas, relations, and rollups. Formulas calculate values from other properties; relations connect database pages; rollups aggregate information from related pages. These capabilities determine whether a plugin can support a project tracker or CRM rather than merely a visual collection. [6]

**Calendar means dated records:** A Notion Calendar requires at least one Date property, supports monthly and weekly views, and creates a database page when an item is added on a date. A daily-note navigator or a calendar showing dots for matching files serves a different purpose. [7]

**Editing need not look identical:** Notion supports editing properties in a table, selecting multiple rows for property changes, and opening each record as a page containing free-form content. An Obsidian plugin can reproduce much of that experience through note properties and Markdown bodies, even if its controls differ. [8]

**The resulting standard:** Prefer a candidate with a shared record model, persistent property edits, and independent view settings. Consider recurrence, external calendars, complex relations, and simultaneous team editing as additional decision criteria rather than assuming that the phrase “Notion-like” includes them all.

Section references:
[6] Notion database properties <https://www.notion.com/help/database-properties> Excerpt: "Rollup View and aggregate information about properties from relation properties. Useful for summarizing interconnected da…"
[7] Notion calendar databases <https://www.notion.com/help/guides/calendar-view-databases> Excerpt: "Notion allows you to choose a monthly or weekly calendar view for your database, and you can decide how your database pag…"
[8] Notion Table view <https://www.notion.com/help/tables> Excerpt: "A table is the classic database view, but tables in Notion are more than just rows and columns. Each row opens up into it…"

## Overall capability matrix

**Read the support labels:** “Yes” means the candidate explicitly presents that database layout. “Core” means the layout comes from the enabled Core Bases plugin. “Query” is a rendered query result; “specialized” describes a narrower board or event presentation. A dash receives no coverage credit in this comparison, rather than making a claim about every possible custom extension.

### Standalone databases and shared-Bases combinations

| Candidate | Role | Table | Kanban/Board | Calendar | General List |
|---|---|---|---|---|---|
| Notion Bases [1] | Standalone community plugin | Yes | Yes | Yes | Yes |
| Note Database [2] | Standalone community plugin | Yes | Yes | Yes | Yes |
| Core Bases [9] | Official core functionality | Yes | Yes, newer releases | No documented standalone Calendar view. | Yes |
| Core + Power Bases [3] | Core plus community extension | Yes | Yes | Yes | Core |
| Core + Kanban Action Planner [10] | Core plus planning extension | Core | Yes | Yes | Core |
| Core + TaskNotes [11] | Core plus task/calendar extension | Core | Newer Core Kanban | Yes | Core |
| Database Views [12] | Standalone database-file plugin | Yes | Yes | Gallery view; no documented Calendar view. | Yes |
| Rowbase [13] | Standalone database-file plugin | Yes | Yes | Activity heatmap only; no standalone Calendar view. | Yes |

**Core Bases has changed:** Older comparisons describe Core Bases as Table-only, Table/Cards, or Table/Cards/List without Kanban. The official changelog snapshot through Desktop v1.14.4 explicitly includes native Kanban, with cards dragged between groups and groups reordered or hidden. Consequently, “Core Bases has no Kanban” is an outdated blanket statement. [9]

**This changes stack coverage:** Kanban Action Planner does not need to supply its own general Table or List editor for the *combination* to meet the four-view requirement: Core supplies those layouts. Similarly, TaskNotes can supply Calendar while newer Core Bases supplies Table, Kanban, and List. In both cases, the intended configuration uses the same note set and matching property names.

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Notion Bases is available in Obsidian's Communit…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Note Database table with active filters, grouped…"
[9] Obsidian changelog <https://obsidian.md/changelog/> Excerpt: "Includes all new features and bug fixes up to Ob…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "Need: Getting data in Stock Bases: Type into cel…"
[10] Kanban Action Planner scheduling <https://dsebastien.github.io/obsidian-kanban-action-planner/> Excerpt: "Kanban Action Planner Kanban Action Planner adds…"
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "TaskNotes provides two calendar-based views: the…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Search for Database Views in Obsidian's communit…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "- Dashboard — Habit tracking with streaks, compl…"

### Table, query, and legacy alternatives

| Candidate | Role | Table | Kanban/Board | Calendar | General List |
|---|---|---|---|---|---|
| DB Folder + Dataview [14] | Community table editor with dependency | Yes | No documented Kanban/Board view. | Date widgets | Not counted |
| DataLoom maintained fork [15] | Community table plugin | Yes | No documented Kanban/Board view. | No documented Calendar view. | No documented general List view. |
| Dataview [16] | Community query engine | Query | No documented Kanban/Board output. | Query dots | Query |
| Kanban + MetaEdit [17] | Board plus metadata bridge | Specialized | Yes | No documented Calendar view. | Stacked board |
| Projects [18] | Discontinued project plugin | Yes | Yes | Yes | Gallery view; no documented general List. |

**View counts can mislead:** Projects advertises four layouts, but they are Table, Board, Calendar, and **Gallery**, not the four requested here. Database Views also advertises four, but its fourth is Gallery rather than Calendar. DataLoom’s multiple tabs and embeds can have different filters and sorts while remaining presentations of the same **table layout**. [18] · Database Views inventory [12] · [15]

Section references:
[14] Obsidian Database Folder <https://rafaelgb.github.io/obsidian-db-folder/> Excerpt: "Using the search engine of the popular Datav…"
[15] DataLoom embeds <https://github.com/aykutkardas/obsidian-dataloom> Excerpt: "Editing table data still updates all views o…"
[16] Dataview Calendar output <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Excerpt: "This page provides information on how to wri…"
[17] MetaEdit synchronization recipe <https://metaedit.obsidian.guide/cookbook/kanban-status-sync/> Excerpt: "The Kanban Board Helper settings panel, show…"
[18] Projects view inventory <https://github.com/obsmd-projects/obsidian-projects> Excerpt: "- Switch between four different views: Table…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Your database lives in a single file and sup…"

### Specialists and presentation-focused extensions

| Candidate | Role | Table | Kanban/Board | Calendar | General List |
|---|---|---|---|---|---|
| Full Calendar Remastered [19] | Community calendar specialist | No documented Table view. | No documented Kanban/Board view. | Yes | Event-specific |
| Full Calendar [20] | Original calendar plugin | No documented Table view. | No documented Kanban/Board view. | Yes | Event-source lists |
| Calendar [21] | Daily-note navigation widget | No documented Table view. | No documented Kanban/Board view. | Daily-note navigation | No documented general List view. |
| Property Kanban [22] | Frontmatter-driven board specialist | — | Yes | — | — |
| Extended Base [23] | Core Bases presentation extension | Yes | Static board | — | Yes |

**The shortlist is therefore clear:** Start with Notion Bases or Note Database for one community plugin, and Core plus Power Bases for a general shared-Bases solution. Choose the specialists when their particular behavior—recurrence, workflow automation, folder hierarchy, or Markdown-board editing—is more important than minimizing components.

Section references:
[19] Full Calendar Remastered overview <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/> Excerpt: "Full Calendar (Remastered) Plugin¶ Keep your calendar in your vault! This plugin integrates th…"
[20] Original Full Calendar <https://github.com/obsidian-community/obsidian-full-calendar> Excerpt: "Full Calendar can pull events from frontmatter on notes, or from event lists in daily notes. F…"
[21] Calendar plugin behavior <https://community.obsidian.md/plugins/calendar> Excerpt: "If you close the calendar widget (right-clicking on the panel nav and clicking close), you can…"
[22] Property Kanban <https://community.obsidian.md/plugins/property-kanban>
[23] Extended Base Board <https://community.obsidian.md/plugins/extended-base>

## The leading candidates and their tradeoffs

### Notion Bases: the clearest standalone replacement

**Why it leads:** Notion Bases explicitly names all four requested layouts within seven total views: Table, Board, Gallery, List, Calendar, Timeline, and Chart. It provides 18 column types, including Formula, Relation, Lookup, Rollup, Status, and media fields. Every row is a Markdown file and ordinary property values live in frontmatter. [1]

**Its setup is approachable:** A folder becomes a database through an `_database.md` configuration note. Schema and view settings are stored there, and embeds can display a chosen layout without duplicating the database. Separate notes can therefore show the same folder as a board, calendar, or table while preserving independent presentation settings. [1]

**Its strongest features combine well:** The editable spreadsheet, configurable status board, property-chip List, and date-based Calendar create a coherent daily workflow. Relations and lookups can connect Tasks to Projects, while rollups summarize linked records. This is substantially closer to Notion’s record model than assembling a table and an unrelated scheduling application. [24]

**Its main tradeoff is scope:** Choose it for a broad local database experience, not because seven layouts establish identical behavior to every Notion feature. For demanding scheduling, the decisive distinction is between moving dated records and managing recurring series; TaskNotes and Full Calendar Remastered explicitly address the latter. Notion Bases requires Obsidian 1.8.7 or later and states desktop/mobile support. [1]

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Turn any folder into a Notion-style database with Table, Board (Kanban), Gallery, List, Calendar, Timeline (Gantt), and Chart views — powered by plain Markdown and frontmatter. Your data stays yours, always. Now available in Obsidian's Community Plugins directory — install it directly in the app - 7 views — Table, Board (Kanban), Gallery, List, Calendar, Timeline (Gantt), Chart - 18 column types — Title, Text, Number, Select, Multi-sel…"
[24] Notion Bases database relationships <https://bgarciamoura.github.io/obsidian-notion-bases-plugin/>

### Note Database: particularly strong editing depth

**Why it challenges the leader:** Note Database supplies eight views over the same Markdown notes: the four requested layouts plus Gallery, Chart, Timeline, and Form. Each view retains its own filters, sorting, grouping, visible properties, title property, and layout. Its documentation is especially detailed about editing, summaries, relations, and embedded databases. [2]

**Its editing is unusually complete:** The Table supports range selection, copy/paste, fill operations, keyboard navigation, overflow-row creation, safe file renaming, and single-step undo. Field-aware editors cover text, numbers, currency, dates, checks, select/multi-select fields, statuses, and filenames. Six built-in starters provide preconfigured properties and views, reducing the work of beginning from a blank schema. [2]

**Its storage stays understandable:** The database is a Markdown file marked `db_view: true`; records and values remain in note frontmatter; relations are normal wikilinks. Formulas offer live previews and optional storage of their results in frontmatter. Its export options include CSV plus a Markdown ZIP. [2]

**Its important interaction distinction:** Embedded databases are read-only by default, although editing can be enabled in settings. Browsing, switching views, filtering, sorting, grouping, and exporting still work in that mode; an explicitly enabled background formula-storage task can also continue. Read-only presentation should therefore not be confused with disabling every database-level write. [2]

Section references:
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "files.A database never duplicates your notes — the eight views are just different lenses over the same Markdown, and each view keeps its own filters, sorting, grouping, visible properties, title property, and layout. Table view Board view Edit dense records, paste ranges, fill cells, group, sort, and navigate by keyboard. Move cards through stages, use subgroups, covers, colored options, and drag-and-drop. Gallery List Gallery view Lis…"

### Core Bases plus Power Bases: the strongest native generalist

**Why the combination works:** Power Bases registers six custom layouts, including a richer Table, Board, Calendar, Timeline, Chart, and Gallery, alongside Core views in the same Base. Rows remain ordinary notes; the `.base` file holds the view definition rather than a separate copy of row data. [3]

**Its advantage is continuity:** Formulas saved through Power Bases go into the Base’s own file and can appear in the built-in Table. A Board move explicitly writes the grouping property into the note. Table, Board, Calendar, and Core List can consequently operate through one native database definition rather than a synchronization bridge. [25]

**Its tradeoff is added machinery:** The extension requires Core Bases and Obsidian 1.10.2 or newer. It is maintained by one person, and some operations affect many real files: changing a property name across rows or computing reverse rollups is materially different from repainting visible cards. For existing Bases users, however, the shared engine makes this a more natural extension than migrating to a separate database-file format. [3]

Section references:
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "Six extra views for Obsidian's core Bases plugin: a kanban board, a calendar, a Gantt-style timeline, a chart, an image gallery, and a much richer table."
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "What you save goes into the base's own file, so the column shows up in the built-in Table view too, and there is nothing to lose if you stop using Power…"

### Database Views and Rowbase: strong three-view alternatives

**Database Views favors simplicity:** Its `.dbview` file contains records with switchable Table, Kanban, List, and Gallery layouts. Saved views are filtered presets with their own sort order and visible columns, and each record can open or create a linked Obsidian note. It suits a relatively compact database workspace where records need not be identical to note frontmatter. [12]

**Rowbase favors property depth:** Its `.rbase` format is human-readable CSV with JSON column metadata. The Table supports formulas, cross-database relations, rollups, typed filters, grouping, inline editing, and a 100-step undo/redo history. Kanban and List reuse that store, and the interface is designed for phones and tablets. [13]

**Their shared decision point:** Both are credible alternatives when Table, Kanban, and List dominate. Rowbase’s Timeline and activity heatmap do not substitute for a general date-property Calendar, and Database Views’ Gallery does not either. A calendar companion broadens the workspace visually, but a linked note is not automatically a synchronized copy of the database record.

Section references:
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Saved views let you create filtered presets with their own view type, sort order, and visible columns. They show up as tabs at the top of your database s…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "file — a human-readable CSV with JSON column metadata — that opens in a rich, interactive view with multiple layouts, formulas, relations, and more. Rowb…"

## Table views: editing, calculations, and persistence

### Compare the table engines first

**The strongest table choices:** Note Database, Notion Bases, Power Bases, and Rowbase provide the most substantial documented spreadsheet-style workflows among the leading candidates. DB Folder remains capable when an existing Dataview-backed table is the priority. Dataview itself is best understood as a query renderer rather than a native property editor.

| Note-backed editor | Property model | Filters and sorts | Grouping | Calculations | Persistence |
|---|---|---|---|---|---|
| Notion Bases | 18 schema types | Typed AND/OR; priority sorts | Board/Timeline groups | Formulas, relations, rollups | Note frontmatter |
| Note Database | Typed fields and file metadata | AND/OR/NOT sources; per-view rules | Groups and subgroups | Formulas, wikilink rollups | Note frontmatter |
| Core + Power Bases | Native properties plus 10 field types | Base filters; property sorting | Groups and subtotals | Base formulas, link rollups | Notes and `.base` formulas |
| DB Folder | YAML or inline fields | Nested AND/OR; multi-sort | Group filters/folder rules | JavaScript, relations, rollups | Source-note metadata |
| Projects | Note properties | Folder/tag/query source | Project-oriented | Basic property-grid workflow | Underlying notes |

**The other storage model:** Database Views, Rowbase, and DataLoom persist their table records in their own database files. That is not inherently worse—it can make structured data more self-contained—but it changes what another plugin can read directly.

| Engine | Fields or columns | Filters and sorts | Grouping | Calculations or links | Write target |
|---|---|---|---|---|---|
| Database Views | Text, number, select, note links | Filtered presets; saved sort | Collapsible sections | Linked notes/records | `.dbview` |
| Rowbase | 15 column types | Typed conditions; multi-sort | Any column | Formulas, relations, rollups | `.rbase` |
| DataLoom fork | Typed cells and note sources | Conditions, search, ascending/descending | Table row organization | Stored table values | Loom data |
| Dataview | Metadata and expressions | DQL filters and multi-sort | `GROUP BY` transformations | Calculated output | Read-oriented render |

The table behaviors above are described in the respective [1][2][25][26][27][12][13][15], and Dataview [16] documentation.

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Turn any folder into a Notion-style database with Table, Boar…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Local-first database views for Obsidian notes: table, board,…"
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "A yearly total is just (formula.mo_rent + formula.mo_dues) 12…"
[26] DB Folder <https://rafaelgb.github.io/obsidian-db-folder/features/Properties/> Excerpt: "You can add nested metadata by writing something like metadat…"
[27] Projects <https://acylation.github.io/obsidian-projects-docs/views/table> Excerpt: "Table view 101 Table view lays out your notes in a grid where…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Table is a spreadsheet-like grid where you can sort, reorder…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "Rowbase demo (table to kanban) - Table — Full-featured spread…"
[15] DataLoom embeds <https://github.com/aykutkardas/obsidian-dataloom> Excerpt: "--dataloom-cell-spacing-x: 12px; --dataloom-cell-spacing-y: 4…"
[16] Dataview Calendar output <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Excerpt: "Dataview offers multiple ways to write queries and the syntax…"

### Filtering, sorting, and grouping are different capabilities

**Notion Bases offers familiar controls:** Its filters use type-aware operators and AND/OR groups, while multi-column sorting has explicit priority. Release 1.13.0 also recognizes hand-written view-frontmatter filters, including array-valued `is_any_of` and `is_none_of` conditions and OR grouping. This is useful when views are configured or reused as text rather than exclusively through menus. [28]

**Note Database separates source and presentation:** Source rules can combine folders, tags, properties, links, and expressions with AND, OR, and NOT. Each saved view then retains its own filtering, sorting, grouping, and visible fields. Active rule chips make the current conditions easier to inspect, while manual record order provides an alternative to purely property-driven sorting. [2]

**Power Bases keeps native selection:** The Base chooses which notes belong to the dataset, and Power views provide additional presentation and editing controls. Its Table offers per-column filtering and sorting, manual row order, and group subtotals; each Power view also has a type-to-filter box. This is particularly convenient when a user already has working Base definitions. [25]

**Rowbase has concrete typed filters:** Text fields support contains, starts-with, and empty checks; numbers support comparisons and ranges; dates support before, after, and between; select and checkbox conditions have their own operators. Multi-column sorts resolve ordering, while grouping by any column creates collapsible sections. It offers a clearer documented filtering model than a generic claim of “advanced filters.” [13]

**DB Folder is powerful but layered:** Ordinary filters combine with AND; nested group filters combine child rules with AND or OR. Named group-filter buttons and the overall filter toggle both affect activation. It also searches displayed metadata using normal text or regex and shows multi-sort priority beside column headers. A “group filter” is a logical condition group, however, not automatically the equivalent of Notion’s visual sub-grouping. [29]

**Database Views stays more compact:** Saved filtered presets, sort order, visible columns, and collapsible grouped sections cover common inventory or project views without requiring a query language. DataLoom similarly provides conditional filters, text search, and sorting, with independent preferences for each tab or embed. These are attractive simpler workflows when elaborate relational calculations are secondary. [12] · [15]

**Dataview changes the data shape:** Its `GROUP BY` does more than visually place records under headings: it produces one result row per group, with a collection of matching rows available for further calculation. `FLATTEN` can expand a multi-value field into multiple output rows. Commands execute in written order, so limiting results before sorting produces a different answer from sorting before limiting. [30]

Section references:
[28] Notion Bases v1.13.0 <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Excerpt: "What's New in v1.13.0 New Features Custom summary statistics — The table's record-count bar n…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Source rules can combine folders, tags, properties, links, and expressions with AND Freeze up…"
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "Power Bases adds six more views and reworks the table, all riding the native engine, so stock…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "- Filtering — Text (contains, starts with, is empty), Number ( , , between), Date (before, af…"
[29] DB Folder display controls <https://rafaelgb.github.io/obsidian-db-folder/features/Displaying%20data/> Excerpt: "You can also toggle the filter state by using the command DB Folder: Toggle filters You can a…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Saved views let you create filtered presets with their own view type, sort order, and visible…"
[15] DataLoom embeds <https://github.com/aykutkardas/obsidian-dataloom> Excerpt: "- Find what matters with filters, text search, and ascending or descending sorting. - Make ta…"
[30] Dataview data commands <https://s-blu.github.io/obsidian-dataview/queries/data-commands/> Excerpt: "Commands are processed in the order they are written, so the following sorts the results afte…"

### Formulas and relations are not interchangeable

**Formula support has several meanings:** Notion uses its own formula language; Notion Bases offers spreadsheet-style functions; Core/Power Bases uses the native expression engine; Note Database supplies computed properties with live previews; Rowbase evaluates cell expressions and cross-relation aggregates. A familiar function name does not make a formula portable between engines. [6] · Notion Bases formulas [1] · [13]

**Notion Bases eases some migration:** Release 1.13.0 accepts Notion-style names such as `dateBetween`, `dateSubtract`, `prop`, `length`, and `toNumber`. This reduces translation work for some expressions, but the practical test remains whether the expression references the same fields and receives the same types—not whether its spelling looks familiar. [28]

**Relations depend on their record model:** Notion relations connect database pages and can optionally expose a corresponding two-way relation. Note Database stores relations as wikilinks and calculates rollups from linked notes; Power Bases follows link properties in either direction; Rowbase relates rows across `.rbase` databases. Database Views’ note links provide useful navigation, but a link field alone should not be credited with every relation-picker or rollup behavior. [31] · Note Database relations [2] · [25]

**DB Folder is explicitly programmable:** Its formulas execute JavaScript when a row loads and can optionally persist results into note metadata. It exposes row values, footer collections, Dataview, rollup functions, and Luxon date operations. That contradicts a broad characterization of DB Folder as merely a basic metadata table; its real tradeoff is greater programming and configuration responsibility. [32]

**Core Bases is not calculation-free:** An older feature discussion describes cross-note access through `file()`, `Link.asFile()`, and `File.properties` in Obsidian 1.9.7, alongside refresh and performance considerations. The useful comparison is native expression-based lookup versus dedicated relation/rollup interfaces—not “Core has formulas but can never read another note.” [33]

Section references:
[6] Notion database properties <https://www.notion.com/help/database-properties> Excerpt: "Formula Perform calculations based on other properties using Not…"
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Feature: Column types Notion Bases: 18 Core Bases: 6 Feature: Fo…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "- Formulas — Safe expression evaluator with cell references and…"
[28] Notion Bases v1.13.0 <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Excerpt: "Notion formula names accepted — The formula engine now recognize…"
[31] Notion relations <https://www.notion.com/help/relations-and-rollups> Excerpt: "That’s because upon duplicating the Customers database, we conve…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Formulas: Formula editor Relations and Rollups: Linked notes and…"
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "Need: Safety net Stock Bases: Undo per note Power Bases: Every c…"
[32] DB Folder formulas <https://rafaelgb.github.io/obsidian-db-folder/features/Formulas/> Excerpt: "The formula is a javascript code that will be executed when the…"
[33] Bases cross-note lookup discussion <https://forum.obsidian.md/t/bases-formula-cross-note-lookup-rollup/101990>

### Inline editing only helps when its destination is clear

**Note-backed editors minimize duplication:** With Notion Bases, Note Database, Power Bases, and DB Folder, editing an ordinary stored property changes the note used by other metadata-aware tools. Computed values require a separate distinction: editing a formula definition is different from overwriting its output, and optional formula-result persistence determines whether another plugin sees a stored result.

**Database-file editors retain internal consistency:** Rowbase and Database Views keep their layouts connected through their own record store. Their note-linking facilities add context and navigation, but users should choose them because that database-file model fits—not assume that every cell edit also changes the linked note’s YAML.

**Dataview’s boundary is deliberate:** Standard TABLE and LIST outputs display indexed information rather than providing native persistent cell editing. Dataview’s TASK output can write task-checkbox changes, but that narrow interaction does not turn its table, list, or calendar into a general database editor. [34] · [35]

**Table takeaway:** Choose Note Database, Notion Bases, or Power Bases for editable note properties; choose Rowbase for a self-contained offline database; choose Dataview when asking flexible questions matters more than editing the answers in place.

Section references:
[34] Dataview interaction model <https://obsidian.rocks/dataview-in-obsidian-a-beginners-guide/> Excerpt: "Even though most of my task management happens with the Tasks plugin, there are a few unique task-based things that Dataview brings to the table. For instance, you can list out the ten oldest and incomplete tasks in your vault like this: GROUP BY file.link SORT rows.file.ctime ASC Edit Dataview Tables Inline Dataview is primarily a tool for viewing data, not for editing it. But wit…"
[35] Dataview task exception <https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/>

## Kanban views: moving cards versus changing records

### Compare the board mechanisms

**The strongest metadata-first boards:** Power Bases and Kanban Action Planner provide the clearest descriptions of what a drag operation writes. Property Kanban is another focused option with explicit two-dimensional property updates. The standalone database candidates provide more integrated overall coverage, while Obsidian Kanban offers a particularly direct Markdown-board experience.

| Board option | Cards and columns | Drag persistence | Organization | Main tradeoff |
|---|---|---|---|---|
| Notion Bases | Notes by select/status | Shared note-backed board | Configurable properties; hidden columns | Broad database rather than specialist planner |
| Note Database | Note cards with stages/covers | Shared Markdown records | Subgroups, colors, summaries | More configurable interaction surface |
| Power Bases | Notes by grouping property | Writes lane property and order | Swimlanes, WIP limits, lane rules | Core dependency; bulk file writes |
| Kanban Action Planner | Notes by defined statuses | Writes status, order, grouping | Typed queries, relationships, swimlanes | More schema/workflow setup |
| Database Views | `.dbview` records by select | Internal database board | Saved filtered views | Separate from note frontmatter |
| Rowbase | `.rbase` rows by select | Internal database board | Filters; inline card editing | Calendar requires another path |
| Kanban + MetaEdit | Markdown cards under headings | Debounced linked-note update | Nested lanes; metadata sorting | Naming-sensitive bridge |
| Property Kanban | Note cards by two fields | Writes lane and column fields | Parent/child links; quick actions | Board-focused component |

These mechanisms are described in Notion Bases [1], Note Database [2], Power Bases [25], Kanban Action Planner [10], Database Views [12], Rowbase [13], MetaEdit [36], and Property Kanban [22].

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Feature: Embed database in any note Notion Bases: Yes Core Bases…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "files.A database never duplicates your notes — the eight views a…"
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "Need: Kanban Stock Bases: Cards in a static grid Power Bases: Dr…"
[10] Kanban Action Planner scheduling <https://dsebastien.github.io/obsidian-kanban-action-planner/> Excerpt: "Kanban Action Planner adds a Kanban board view to Obsidian Bases."
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Create structured views of your data with kanban boards, tables,…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "Rowbase demo (table to kanban) - Table — Full-featured spreadshe…"
[36] MetaEdit helper rules <https://metaedit.obsidian.guide/guides/kanban-helper/> Excerpt: "Move a card between lanes on a Kanban board and the linked note’…"
[22] Property Kanban <https://community.obsidian.md/plugins/property-kanban>

### Integrated boards offer different kinds of control

**Power Board makes movement meaningful:** Each value of the chosen grouping property becomes a lane. Moving a card changes that property in the note; manual order is also stored as data. Adding a second property creates swimlanes, and crossing both dimensions sets both values. Lane rules can stamp other properties when a card enters a state, while WIP limits and numeric totals support workload management. [25]

**This is stronger than appearance:** A board that merely repositions a card can look convincing while leaving a Table’s `status` unchanged. Power’s explicit property write makes the relationship concrete: the card changes lane because its source value changes. Its touch interaction—hold to lift, then drag—also addresses a common mobile-board difficulty. [25]

**Kanban Action Planner prioritizes defined workflows:** Status columns are explicitly configured per view, note type, or global settings. Unknown values collect in an Unmapped column instead of silently creating a new workflow stage. Cards can display selected properties and Base formulas, use configurable titles and covers, and expose parent, sibling, child, and blocked-by relationships. [37]

**Its filtering is especially useful:** Saved queries such as `status:active OR due:overdue` and `parent:"PKM" -tag:archived` narrow both planning and scheduling views. Cards can be sorted by properties or formulas, while drag reordering writes a configurable numeric order field. Formula and file metadata can guide display and sorting, but writable status/order/grouping selectors use actual frontmatter properties. [37]

**Its precision adds setup work:** Explicit columns prevent typos from becoming unintended stages, but the intended statuses must first be defined. Property-based swimlanes are writable; note-type lanes are not interchangeable drag targets because type recognition comes from tags or folder rules. This distinction is valuable in a mixed goals/projects/tasks board, where changing a task’s status should not accidentally change what kind of note it is. [37]

**The standalone boards stay simpler:** Notion Bases groups cards by select or status, supports creating cards inside columns, exposes chosen properties, and can hide empty or no-value lanes. Its 1.13.0 release also keeps schema-less group values visible in their own columns. Note Database adds subgroups, cover controls, option colors, and grouped summaries. The contrast is preservation of existing values versus tightly declared workflow states. [28] · [2]

Section references:
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "Need: Kanban Stock Bases: Cards in a static grid Power Bases: Drag between lanes to change a property, manual order, swimlanes, WIP limits, lane rules, and lane totals Nee…"
[37] Kanban Action Planner configuration <https://dsebastien.github.io/obsidian-kanban-action-planner/configuration.html> Excerpt: "Note-type lanes are read-only, because a note’s type comes from its tags/folder, so cross-lane drags there are ignored. Relationships Each relationship role reads a link-p…"
[28] Notion Bases v1.13.0 <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Excerpt: "Select option autocomplete in source mode — When editing a database note's frontmatter directly in source mode, Obsidian now suggests valid select options for schema-defin…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Note Database table with active filters, grouped records, summaries, formulas, and file properties db_view: true records, properties, and relations also stay inside your v…"

### Native Core Kanban changes the minimum setup

**Core now covers basic boards:** The official changelog describes arranging notes in columns and dragging cards between groups. A user report about the 1.14 release distinguishes this cross-column property change from manual prioritization within a column: the reported ordering followed the view’s Sort settings rather than a persisted drag order. [9] · [38]

**That distinction guides the upgrade:** If property-sorted columns are enough, Core Kanban reduces the need for a community board extension. If repeatedly dragging work up and down to establish priority is central, Power Bases and Kanban Action Planner explicitly provide persistent manual-order behavior. Their value now lies in those deeper controls, not simply being able to display columns.

Section references:
[9] Obsidian changelog <https://obsidian.md/changelog/> Excerpt: "Organize your notes into columns and drag cards between groups. You can also reorder and hide groups in any Bases view using the new Group menu. Bring color to your notes with six highlight colors. in the editor now su…"
[38] Core manual-order discussion <https://forum.obsidian.md/t/bases-kanban-manual-card-ordering-within-a-column-drag-and-drop-persisted-to-a-property/119092>

### Markdown boards need a deliberate bridge

**Obsidian Kanban is genuinely useful:** Its v2 public-release notes describe Kanban, stacked vertical List, and Table presentations, native Markdown editing inside cards, inline Dataview metadata sorting, and Tasks integration. Nested sub-swimlanes can be represented with heading levels. This makes it attractive for lightweight planning directly in a Markdown board file. [39] · [40]

**MetaEdit connects lanes to notes:** Its helper follows the leading link of a top-level card and writes the nearest lane heading into an existing property on the linked note. Updates run approximately **five seconds after the final board change**, because continuing edits reset the debounce timer. Dataview can then regroup a dashboard from that updated property. [17]

**The bridge has exact requirements:** Property names are case-sensitive and must already exist. Only the leading card link identifies the target note; ambiguous links are skipped. Board configurations match the file basename, so renaming the board requires re-registering it. This is a workable board-to-metadata workflow, but not the same architecture as a board generated directly from note properties. [36]

**Two focused alternatives differ:** Property Kanban explicitly updates both lane and column frontmatter when cards cross its two-dimensional board. Extended Base offers attractive grouped cards and shared inline property editors, but its documentation explicitly says cards are not yet draggable; users change groups through the property pill or page panel. A visually convincing static Board is therefore partial Kanban functionality, not an equivalent drag workflow. [22] · [23]

**Board takeaway:** Use Power Bases for a general database board, Kanban Action Planner for structured planning, and Kanban plus MetaEdit when editable Markdown boards are the priority and its synchronization conventions fit.

Section references:
[39] Kanban v2 features <https://github.com/obsidian-community/obsidian-kanban/releases> Excerpt: "- There are now three ways to view a board: as a Kanban, as a stacked vertical list, and as a table. - Lanes can be collapsed."
[40] Nested lanes <https://community.obsidian.md/plugins/kanban> Excerpt: "H2 headings create top-level lanes, and H3+ headings create sub-lanes nested under the preceding H2. You can configure global…"
[17] MetaEdit synchronization recipe <https://metaedit.obsidian.guide/cookbook/kanban-status-sync/> Excerpt: "Build a project board where dragging a card is all it takes: about five seconds after you drop a card in a new lane, MetaEdit…"
[36] MetaEdit helper rules <https://metaedit.obsidian.guide/guides/kanban-helper/> Excerpt: "Move a card between lanes on a Kanban board and the linked note’s property updates to match. Drag Dune review from Drafting t…"
[22] Property Kanban <https://community.obsidian.md/plugins/property-kanban>
[23] Extended Base Board <https://community.obsidian.md/plugins/extended-base>

## Calendar views: database dates, recurrence, and external events

### Calendars inside the database candidates

**The closest basic matches:** Notion Bases, Note Database, Power Bases, and Kanban Action Planner all position note-backed records using date properties. They differ most in time-grid detail, date-range handling, and the distinction between scheduled dates and deadlines.

| Candidate | Calendar modes | Date model | Creation and movement | Best use |
|---|---|---|---|---|
| Notion Bases | Month; week in v1.13.0 release notes | Chosen date; optional end date | Dated-note creation; duration-preserving drag | General database scheduling |
| Note Database | Month, week, day | Date/datetime; all-day and multi-day | Drag and resize records | Detailed local database calendar |
| Power Bases | Month, week | Selected Date property | Create dated page; drag to reschedule | Calendar inside native Bases |
| Kanban Action Planner | Day, week, month, quarter, year | Scheduled date and deadline | Writes configured date properties | Planning work across horizons |

The modes and behaviors come from Notion Bases releases [28], Note Database [2], Power Calendar [3], and Kanban Action Planner [41].

**Notion Bases needs version context:** Its README describes a monthly date-field calendar with click-to-create pre-dated notes and a collapsible undated section. Release 1.13.0 additionally documents a week view with an optional end-date field: events use their actual duration, and dragging preserves that duration. Describing the plugin as permanently month-only would therefore understate the release behavior. [1] · [28]

**Note Database provides richer daily scheduling:** Month, week, and day views handle date and datetime records, with dragging and resizing. Its monthly overview includes all-day and multi-day records, while weekly layout exposes timed records. Search operates over visible event-card fields, and the database’s per-view filters and visible properties remain part of the same shared-note system. [2]

**Power Calendar favors a clear model:** Choose one Date property, display its pages in month or week mode, drag a chip to another date, or double-click a date to create an already-dated page. Timed records occupy hour rows in the weekly grid. This is well suited to meeting notes, publication schedules, and deadlines inside an existing Base. [3]

**Kanban Action Planner distinguishes two intentions:** Its calendar can plot scheduled work and deadlines together. Dragging writes the selected `date_scheduled` or `date_due` property, while Unplanned and No-deadline panels retain work that has not yet received those values. Filters carry across from the Board, so switching views does not require rebuilding the working subset. [10]

**Recurrence is a separate requirement:** Showing a record on a date, rescheduling it, or stretching a date range does not by itself define how repeated occurrences are generated, edited, or completed. For explicit recurring-series behavior, TaskNotes and Full Calendar Remastered provide the more developed mechanisms.

Section references:
[28] Notion Bases v1.13.0 <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Excerpt: "Calendar week view: event duration via end date field — You can now designate an end date field so calendar events span their real…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "files.A database never duplicates your notes — the eight views are just different lenses over the same Markdown, and each view keep…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "week mode lays timed pages out over hour rows, which is the shape meeting notes want. Drag a chip to another day to reschedule it,…"
[41] dsebastien/obsidian-kanban-action-planner <https://github.com/dsebastien/obsidian-kanban-action-planner> Excerpt: "a formula can prefer a local file over a URL), cropped or whole, as a banner or in a fixed shape such as 2:3 for posters, and as a…"
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Notion Bases offers 5 exclusive views that Core Bases doesn't have — Board, Gallery, Calendar, Timeline, and Chart — giving you the…"
[10] Kanban Action Planner scheduling <https://dsebastien.github.io/obsidian-kanban-action-planner/> Excerpt: "Switch a board to a calendar that plots scheduled dates and deadlines together. Drag a card onto a day to schedule it — or right-cl…"

### TaskNotes: strongest for recurring task schedules

**TaskNotes extends the same engine:** Its documented v4.12.0 Mini Calendar and Calendar View are Bases views stored in `.base` files. Mini Calendar can track a configurable date property on tasks or other dated notes, while Calendar View supports month, week, day, year, chronological List, and custom multi-day modes. The custom range is 2–10 days. [11]

**Filtering is part of the view:** Saved calendar configurations retain task-property filters, date ranges, tags, display options, and mode. Users can independently show scheduled dates, due dates, recurring items, timeblocks, ICS events, and time entries. This is more useful for execution-focused scheduling than a date grid with one undifferentiated category of records. [11]

**Recurrence has two distinct edits:** Dragging the solid-border next occurrence changes only the task’s `scheduled` value. Dragging a dashed pattern instance changes `DTSTART`, moving future pattern instances while leaving the independently scheduled next occurrence alone. This supports a realistic situation: doing this week’s recurring task early without permanently changing its normal weekday. [11]

**External calendars are writable:** TaskNotes documents bidirectional OAuth synchronization with Google Calendar and Microsoft Outlook, including rescheduling external events by drag-and-drop. Those integrations require account configuration, but they address a different problem from merely showing local notes by date. Scheduled-to-due span bars are a separate read-only calendar representation; their underlying dates remain the editing target. [11]

**Its best four-view configuration:** Combine TaskNotes Calendar with Table, List, and the native Kanban in newer Core Bases. This is a coherent note/Bases architecture when all views select the intended records and use the intended date fields. Power Bases remains the more general table-and-board enhancement; TaskNotes becomes preferable when recurrence, time-blocking, and external calendars dominate.

Section references:
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "- Span tasks between scheduled and due dates: Display tasks as multi-day bars spanning from their scheduled date to their due date (see below) Multiple saved calendar views can store different option sets (for example planning vs focus), avoiding repeated manual toggles. The All-day slot option is particularly useful when you have many all-day tasks on a single date, as hiding it can resolve scrolling issues and make the hourly time slots more accessible. When disabled, all-day events will not be displayed in time grid views, but they will still appear in month view. Mul…"

### Full Calendar Remastered: strongest calendar interoperability

**Its strength is provider breadth:** Full Calendar Remastered connects local event notes, Daily Notes, Google Calendar, CalDAV calendars, local/remote ICS, Outlook, Tasks, and TaskNotes integrations. The documentation identifies release 0.13.5 and describes refreshed mobile interaction, calendar workspaces, richer exports, and linked-note workflows. [19]

**Storage determines editing behavior:** Within the same plugin, Full Note, Daily Note, Bases, and remote providers have materially different capabilities. Choosing the right provider is therefore more important than simply enabling a Calendar view.

| FCR source | Underlying record | Editing behavior | Recurrence behavior | Practical role |
|---|---|---|---|---|
| Full Note | One event note with frontmatter | Create, edit, move, resize | Series and individual overrides | Detailed vault-native events |
| Daily Note | List item under a heading | Targeted Markdown-line edits | Recurring series excluded | Compact daily schedules |
| Obsidian Bases provider | Notes selected by `.base` filters | Read-only provider | Display-oriented aggregation | Calendar projection of a Base |
| ICS | Local file or remote feed | Read-only provider | Imported provider data | Calendar subscription |
| Google/CalDAV/Outlook | Remote provider records | Provider-specific writes | Provider-specific series rules | External calendar integration |

These source contracts are described in the FCR provider reference [42].

**Full Note is the database-like option:** Frontmatter is authoritative for event data, and each event has its own note with persistent identity and room for context. Dragging or resizing preserves descriptions, location, categories, and custom frontmatter. Moving one recurring occurrence creates an override while preserving the parent series and future dates. [43]

**Recurring series have explicit controls:** Daily, weekly, monthly, and yearly frequencies support intervals, selected weekdays, start/end repeat dates, and occurrence overrides. One source item represents the series rather than requiring a manually duplicated note for every occurrence. This is a substantial advantage when repeated meetings or recurring tasks matter. [44]

**Daily Notes trade power for compactness:** Events are list items with inline time fields or a strict DayPlanner-style prefix. The documented backend permits one active Daily Note calendar source, excludes recurring and multi-day single events, and rejects duplicate visible titles on the same date. Moves between Full Note calendars are supported, while moves involving Daily Note calendars are not. [45] · [43]

**Bases integration is not universal write-back:** FCR’s dedicated Obsidian Bases provider rejects creation, update, deletion, and recurring-instance override writes. That makes it useful for a filtered calendar projection of existing Base notes, but it should not be recommended as an editable Calendar extension equivalent to Power Calendar solely because both can read `.base` definitions. [42]

**Provider-specific rules override broad claims:** The detailed provider reference identifies an Outlook limitation for writing single recurring-instance overrides. It also distinguishes CalDAV task recurrence preservation from creating or changing those task recurrence rules. Consequently, “two-way calendar integration” should be interpreted for the actual provider and operation rather than as identical behavior across all sources. [42]

**Filters are more than colors:** FCR workspaces save visible sources, default creation calendars, event/task visibility, display modes, and time-grid options. Their `.base` filter integration supports nested AND, OR, and NOT conditions over file information and frontmatter, including property existence and numeric comparisons. This is effective calendar organization without implying a general relational database editor. [46]

Section references:
[19] Full Calendar Remastered overview <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/> Excerpt: "The latest release, 0.13.5, expands the planning surface with Availability Sharing, richer ICS Export filters, Event Linked Notes presets and faster open-or-create flows, a ref…"
[42] FCR Bases capability contract <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/architecture/calendars/provider-implementations/> Excerpt: ": These remain in use for creating new event notes and for deciding if a file should be renamed when a user edits title or date via the modal. They are intentionally not used f…"
[43] FCR event management <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/events/manage/> Excerpt: "- Recurring Instance Overrides: Moving a single occurrence of a recurring series creates an isolated single-event override, keeping the parent recurrence rule and all future da…"
[44] FCR recurrence model <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/events/recurring/> Excerpt: "- In the Repeats dropdown, select the frequency: Daily, Weekly, Monthly, or Yearly. - Daily: The event will repeat every day or every X days (e.g., every 3 days). - Weekly: Cho…"
[45] FCR Daily Note behavior <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/calendars/dailynote/> Excerpt: "Timed events can be written either with Dataview inline fields or in a strict DayPlanner-style prefix, depending on the format selected when you add the Daily Note calendar sou…"
[46] FCR workspaces and filtering <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/views/workspaces/> Excerpt: "- Visibility Protection: If the configured default calendar is excluded by the workspace's Visible Calendars list, Full Calendar safely skips it and falls back to the first vis…"

### Calendar names do not guarantee equivalent functionality

**The original Full Calendar remains distinct:** It reads events from note frontmatter or daily-note event lists and supports read-only ICS and CalDAV sources. Its documented core attraction is keeping event context in the vault. For a new workflow requiring richer provider operations and recurring-event control, Remastered offers the more developed feature description. [20]

**Dataview is a date index:** `CALENDAR file.cday` displays each matching page as a dot on its creation date; another date expression can select a different indexed field. It is useful for reviewing when notes were created, books finished, or records dated. It is not the same interaction as moving an appointment between time slots or editing a recurring series. [16]

**Calendar is a daily-note navigator:** Liam Cain’s Calendar plugin reads Daily Note settings, opens or creates daily notes, provides previews, and can navigate weekly notes. Its dots indicate writing volume or incomplete tasks, not arbitrary database events: by default, one solid dot represents 250 words, with a maximum of five. [21]

**DB Folder’s terminology needs care:** Its early changelog explicitly introduces Calendar as a **column type**, later changes the date-picker dependency, and discusses calendar-cell fixes. Other entries mention List editing. Those references should not be promoted into a complete date-grid Calendar or general database List without the corresponding layout behavior. Its strong supported use remains editable metadata tables. [47]

**Calendar takeaway:** Use a database candidate’s Calendar for dated records; choose TaskNotes for recurring task scheduling and writable Google/Microsoft integration; choose Full Calendar Remastered for a broad event/calendar hub with carefully selected providers.

Section references:
[20] Original Full Calendar <https://github.com/obsidian-community/obsidian-full-calendar> Excerpt: "Full Calendar can pull events from frontmatter on notes, or from event lists in daily notes. Full Calendar also support…"
[16] Dataview Calendar output <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Excerpt: "Renders a Calendar view where each page is represented as a dot on its creation date. CALENDAR file.cday Shows a table…"
[21] Calendar plugin behavior <https://community.obsidian.md/plugins/calendar> Excerpt: "Each solid dot represents 250 words in your daily note. So 4 dots means you've written a thousands words for that day!…"
[47] DB Folder changelog <https://rafaelgb.github.io/obsidian-db-folder/changelog/> Excerpt: "- Column settings that has a type without behavior section produce a console error no more and section tittle is not sh…"

## List views: compact databases versus specialized agendas

### Compare general-purpose List layouts

**The best general Lists:** Notion Bases, Note Database, Core Bases, Database Views, Rowbase, and Extended Base explicitly provide database List layouts. Dataview provides a highly useful query-generated list, but its editing model is different.

| Candidate | What the List shows | Grouping or hierarchy | Filtering and navigation | Editing approach |
|---|---|---|---|---|
| Notion Bases | Title plus property chips | Minimal record overview | Per-view filters, sorts, fields | Shared note/property layer |
| Note Database | Compact records and properties | Saved view grouping | Shared rules; title/link previews | Shared editors; embed setting |
| Core Bases family | Native note/property list | Native view organization | Base filters and note navigation | Core note/property workflow |
| Database Views | Compact grouped records | Collapsible sections | Saved presets; linked-note access | Database records; Table for dense edits |
| Rowbase | Compact grouped rows | Collapsible sections | Shared database controls; note links | `.rbase` property layer |
| Dataview | Page links plus one expression | Query-generated groups | DQL filters/sorts; file links | Read-oriented output |
| Extended Base | Title left; properties right | Actual folder nesting | Native Base controls; page panel | Inline property editing |

The List designs are described in Notion Bases [1], Note Database [2], Power/Core coexistence [3], Database Views [12], Rowbase [13], Dataview [16], and Extended Base [23].

**Notion Bases is close visually:** One title line with property chips resembles the minimal overview many users want from Notion List. Independent property visibility and sorting make it useful for a reading queue, contact directory, or upcoming-work view without showing a wide spreadsheet. The important benefit is that these remain the same notes used by the other layouts. [1]

**Note Database adds shared presentation rules:** Its List participates in the same saved-view model and shares option colors with Table, Board, and Gallery. Record titles, relations, internal links, and clickable file metadata can use Core Page Preview across layouts. This provides a more consistent browsing experience when a database mixes descriptive text, dates, and linked records. [2]

**Database-file Lists remain coherent internally:** Database Views and Rowbase offer compact rows under collapsible grouped sections. Database Views explicitly opens or creates a linked note from a record’s eye control; Rowbase supports opening/creating notes through title cells and storing note links in dedicated columns. These are practical navigation tools, but the record remains in its database file. [12] · [13]

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Notion Bases offers 5 exclusive views that Core Bases doesn't have — Board, Gallery, Calendar, Timeline, and Chart —…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "metadata and the core Page preview plugin for record titles, Relations, and internal links inside text..base files.A…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "Power Bases adds six more views and reworks the table, all riding the native engine, so stock and Power views live si…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "List shows a compact grouped view with collapsible sections. Gallery displays cards with cover images in a responsive…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "- List — Compact grouped rows with collapsible sections - Gallery — Card grid with cover images and clickable detail…"
[16] Dataview Calendar output <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Excerpt: "Dataview offers multiple ways to write queries and the syntax differs for each. This page provides information on how…"
[23] Extended Base Board <https://community.obsidian.md/plugins/extended-base>

### Grouping does not automatically create nested records

**Hierarchy has different meanings:** A list grouped by project, a folder tree, and a parent/child task structure solve different problems. Notion Bases documents hierarchical rows up to three levels through self-relations, but that should not be read as a promise that every flat List presentation exposes the same hierarchy. Collapsible groups likewise do not establish parent/child relationships between their records. [1]

**Extended Base is especially relevant here:** Its List keeps inline property editing and a Notion-style page panel while supporting actual parent/subfolder nesting when grouping by `file.folder`. Ordinary property values remain flat—even a value containing `/` is not automatically turned into a record hierarchy. This is a useful distinction for users who organize research or applications through real folders. [23]

**Its constraints are concrete:** Extended Base’s `file.*` and `formula.*` columns are read-only, and tag pills are intentionally read-only in its current editing design. The optional toolbar CSS snippet affects all Bases toolbars, not only Extended Base views. Choose it for its List/presentation experience, while using native or another extension’s Kanban and Calendar where appropriate. [23]

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "Subtasks Hierarchical rows with expand/collapse up to 3 levels via self-relations Filters Type-aware operators, AND/OR groups Sorts Multi-column with priority ordering Aggregation Sum, Average, Min, Max, Count — updates live Number formatting Prefix ($ , R$ ), suffix (% , kg ), decimals, thousands separator Column controls Pin, resize (drag), reorder (drag)…"
[23] Extended Base Board <https://community.obsidian.md/plugins/extended-base>

### Specialized lists should retain their meaning

| Specialized presentation | What its entries represent | Why it differs from a general database List |
|---|---|---|
| Kanban stacked List | Cards under board lanes | Retains board structure and card semantics |
| Kanban Action Planner Agenda | Overdue, Today, Upcoming work | Prioritized execution queue |
| TaskNotes Calendar List | Chronological calendar events | Date-driven event review |
| Full Calendar family lists | Calendar events or daily-note items | Event-source and scheduling semantics |

These distinctions follow the Kanban release notes [39], Kanban Action Planner Agenda [10], TaskNotes List mode [11], and FCR Daily Note documentation [45].

**Dataview is ideal for indexes:** Its LIST output returns matching page links with an optional expression beside each link. Filters, sorting, grouping, and limits can produce compact reading lists or maps of related notes without maintaining a separate record store. The native list remains a rendered answer; edits happen in the source note or through an additional editing component. [16]

**List takeaway:** Choose a shared database List when it is another working view of your records; choose Dataview for automatically generated indexes, and specialized agendas when the question is specifically “what should I do next?”

Section references:
[39] Kanban v2 features <https://github.com/obsidian-community/obsidian-kanban/releases> Excerpt: "Release list 6f754da Fix issues with da…"
[10] Kanban Action Planner scheduling <https://dsebastien.github.io/obsidian-kanban-action-planner/> Excerpt: "Kanban Action Planner Kanban Action Pla…"
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "TaskNotes also includes a dedicated Age…"
[45] FCR Daily Note behavior <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/calendars/dailynote/> Excerpt: "You must be using one of the supported…"
[16] Dataview Calendar output <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Excerpt: "You can output one field for each page…"

## Portability, setup, performance, and maintenance

### The storage model determines what survives

**Markdown ownership has practical value:** Notion Bases, Note Database, and the Bases extensions retain ordinary notes and frontmatter. If their custom interface disappears, the record content and stored properties remain readable. Their view definitions, formula syntax, and special display behavior still belong to a particular engine, so portable data does not mean universally portable database behavior.

| Storage approach | Representative candidates | What remains directly readable | What depends on the engine |
|---|---|---|---|
| Markdown notes/frontmatter | Notion Bases, Note Database | Records, bodies, stored properties | Views, formulas, rich editors |
| Notes plus `.base` definitions | Core, Power, KAP, TaskNotes | Notes and text-based configuration | Native/custom view execution |
| `.dbview` records | Database Views | Database file and linked notes | Database interpretation and layouts |
| CSV-based `.rbase` | Rowbase | Human-readable structured rows | Rich metadata/formula behavior |
| Loom database files | DataLoom | Loom data or exported tables | Loom rendering and interactions |
| Markdown board | Kanban + MetaEdit | Headings, cards, linked-note properties | Board UI and synchronization helper |
| Rendered queries | Dataview | Query text and original notes | Live query results |

The formats are described in the candidates’ [1][2][3][12][13][15][17], and Dataview rendering model [35] documentation.

**Rowbase offers unusually explicit portability:** Its CSV-based file can be opened with a text editor or spreadsheet, and it supports CSV/JSON export. It also states a fully offline runtime without accounts, telemetry, HTTP requests, WebSockets, or CDN assets. That makes it attractive for structured data ownership even though its database rows differ from ordinary Markdown note records. [13]

**DataLoom has an export route:** The original maintainer recommends exporting existing looms to raw Markdown, while the maintained fork supports CSV and Markdown import/export. That preserves table information, but a Markdown table is not a replacement for saved filters, typed editors, or synchronized multi-layout behavior. The original project also identified native search, backlink, and graph integration gaps; those historical architectural concerns should be distinguished from the maintained fork’s newer folder/frontmatter connections. [48] · [15]

**Dataview separates records from answers:** A dynamic query reads real notes, but its rendered result is not automatically written into the hosting note as ordinary Markdown. This matters when sharing an index outside Obsidian or expecting its generated links to behave like permanently stored links. An optional serialization workflow can materialize results, at the cost of maintaining snapshots rather than purely live output. [35]

**Notion exports have boundaries too:** Its documentation says CSV export converts relations into plain-text URLs, and re-importing that CSV does not recreate the relations. Thus, neither Notion’s integrated interface nor an Obsidian plugin’s export button eliminates migration work for connected data. [31]

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "- Subtasks — Hierarchical rows with exp…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Local-first database views for Obsidian…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "A yearly total is just (formula.mo_rent…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "A plugin for Obsidian that brings Notio…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "It remains human-readable and can be op…"
[15] DataLoom embeds <https://github.com/aykutkardas/obsidian-dataloom> Excerpt: "Existing looms keep their saved filters…"
[17] MetaEdit synchronization recipe <https://metaedit.obsidian.guide/cookbook/kanban-status-sync/> Excerpt: "Step 1: create the board Section titled…"
[35] Dataview task exception <https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/>
[48] Original DataLoom migration guidance <https://github.com/decaf-dev/obsidian-dataloom> Excerpt: "Please export any existing DataLoom fil…"
[31] Notion relations <https://www.notion.com/help/relations-and-rollups> Excerpt: "For now, you can't re-import that CSV b…"

### Setup effort follows the amount of structure

**The easiest complete starting points:** Notion Bases uses a folder-based database setup; Note Database offers starters and saved templates; Power Bases can create a ready-made Base from a folder or CSV import. These are more approachable for users migrating from Notion’s visual configuration than beginning with custom queries and synchronization scripts. [1] · Note Database starters [2] · [3]

**More customization requires more conventions:** Kanban Action Planner benefits from defined note types, statuses, date properties, and relationship roles. DB Folder requires Dataview and careful mapping between column IDs and stored metadata. Kanban plus MetaEdit adds board registration and linking rules, while TaskNotes and FCR add calendar-provider configuration when connecting external accounts.

**Shared files need shared field names:** KAP’s default scheduled-date property is `date_scheduled`, whereas TaskNotes’ recurrence interaction writes `scheduled`. Two plugins reading the same folder will not automatically treat those names as one field. Power Calendar’s selectable Date property makes such alignment straightforward, but schema agreement remains the reason the views cooperate—not merely their presence in the same vault. [37] · [11]

**Inline fields require particular attention:** Dataview and DB Folder can read Dataview-style inline metadata. The Bases migration guide instead uses YAML properties and recommends converting inline fields before moving that data into Bases. For an existing vault, data placement can therefore determine migration effort more strongly than the number of available layouts. [49]

Section references:
[1] Notion Bases <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Excerpt: "- Subtasks — Hierarchical rows with exp…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "Saved templates appear under My templat…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "Power Bases adds six more views and rew…"
[37] Kanban Action Planner configuration <https://dsebastien.github.io/obsidian-kanban-action-planner/configuration.html> Excerpt: "The WBS reuses the properties you alrea…"
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "- Span tasks between scheduled and due…"
[49] Dataview-to-Bases migration <https://practicalpkm.com/moving-to-obsidian-bases-from-dataview/> Excerpt: "Bases, on the other hand, uses YAML met…"

### Performance depends on the operation

**The most useful performance anchors:** The following figures describe different workloads. Their practical value is identifying expensive operations and query scope rather than constructing a speed ranking.

| Candidate | Reported anchor | Workload or mechanism | Practical implication |
|---|---|---|---|
| DB Folder | 3–8 seconds | Opening 3,000 dense Markdown files | Keep operational sources focused |
| Power Bases | 20,000-note daily-use claim | Batched rendering; no configured row cap | Rendering and bulk writes are different costs |
| Dataview | About 1–2 seconds extra mobile startup | One reviewer’s phone experience | Account for index/startup cost |
| Notion Bases | Wrapped rows bypass virtualization in v1.8.3 | Variable row-height rendering fix | Wrapping can change large-table behavior |
| TaskNotes | Virtual scrolling | Large event lists and long ranges | Designed to limit rendered event load |

Sources: DB Folder review, May 3, 2026 [50], Power Bases scale claim [3], Dataview mobile observation [51], Notion Bases rendering release [28], and TaskNotes scrolling [11].

**Rendering is not file mutation:** Power Bases explicitly notes that renaming or deleting a column rewrites one note per row, while reverse rollups sweep frontmatter. As a conditional operation-count example, a Base containing 20,000 rows could require **20,000 note rewrites** for a property rename: 20,000 rows × one note per row. That is a file-operation scenario, not an elapsed-time estimate. [3]

**Query scope affects Dataview:** Its official documentation warns that broad examples can take a long time or freeze Obsidian in extreme cases, recommending `FROM` restrictions. Positive folder/tag selection, modest result sets, and fewer queries on one dashboard reduce the amount of work requested. A large vault does not make every query slow, but an unbounded query can still be costly. [16]

**Full-text search is another workload:** The native metadata-oriented workflows should not be sold as interchangeable with searching every note body. Forum reports of custom Dataview or JavaScript body-text solutions demonstrate possible extensions, while the standard indexed-field model remains the relevant baseline here. The same discussion distinguishes Bases property filtering from native content search. [52]

Section references:
[50] DB Folder mobile review <https://notes-automate.com/posts/review-of-obsidian-db-folder-for-database-views/> Excerpt: "Review of Obsidian DB Folder for Databa…"
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "Two operations are honest exceptions, b…"
[51] Dataview vs Datacore vs Obsidian Bases <https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/> Excerpt: "It is one of the most downloaded plugin…"
[28] Notion Bases v1.13.0 <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Excerpt: "The plugin name is now consistently cap…"
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "- Default Configuration: Ships with 3 d…"
[16] Dataview Calendar output <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Excerpt: "Depending on the size of your vault, ex…"
[52] Metadata and body-content discussion <https://forum.obsidian.md/t/bases-display-access-and-or-filter-using-the-notes-content/101378> Excerpt: "Base views currently only allow filteri…"

### Maintenance and compatibility by candidate

**Release anchors need clear labels:** The tables below distinguish plugin releases from minimum **Obsidian application** versions. “Release-specific” and “device-conditional” are deployment positions, not numerical estimates of maintenance cadence or compatibility.

| Candidate | Maintenance position | Version anchor | Compatibility or dependency | Mobile position |
|---|---|---|---|---|
| Notion Bases [28] | Release history with feature/fix updates | Plugin 1.13.0 | Obsidian 1.8.7+ | Desktop/mobile stated |
| Note Database [2] | Release-channel local project | Release-specific | Core Page Preview for previews | Device-conditional |
| Core Bases [9] | First-party app development | Changelog through Desktop 1.14.4 | Bundled core functionality | Core-app support |
| Power Bases [53] | One-person maintained extension | Release snapshot 1.33.19 | Obsidian 1.10.2+; Core Bases | Mobile stated |
| Database Views [12] | PlantBasedStudio stewardship | Release-specific | `.dbview` engine | Device-conditional |
| Rowbase [13] | Community-store and beta routes | Release-specific | Optional BRAT beta route | Phone/tablet responsive |
| DB Folder [54] | Upstream archival reported July 2025 | Final manifest reported 3.5.1 | Dataview required | Historical mobile support |
| DataLoom fork [15] | Continued maintenance claimed | Fork release-specific | Distinct from archived original | Desktop/mobile stated |
| Dataview [35] | Mature; slower development | 0.5.68 stable; 0.5.70 beta reported | Community query engine | Mobile use with load tradeoff |

**Dataview deserves a balanced description:** A 2026 guide reports stable release 0.5.68 on March 15 and beta 0.5.70 on April 7, while describing slower development and continued functioning. That supports treating it as mature infrastructure with maintenance exposure, not automatically as broken or equivalent to an actively expanding database editor. [35]

**DB Folder’s history is not renewal:** Its official changelog documents substantial past work—relations, formulas, mobile improvements, and pagination. Obsidian Mate reports archival in July 2025 and final manifest 3.5.1. A long surviving feature history is compatible with an archived upstream project; it should not by itself be interpreted as a current development commitment. [47] · [54]

| Candidate | Maintenance position | Version anchor | Compatibility or dependency | Mobile position |
|---|---|---|---|---|
| Kanban + MetaEdit [17] | Kanban seeking maintainers | Kanban snapshot 2.0.51; MetaEdit 1.9.0 setup | Helper setup uses Obsidian 1.12.7+ | Desktop/mobile setup |
| Kanban Action Planner [10] | Explicitly in development | Milestone-based delivery | Obsidian 1.13+; Bases API | Desktop/mobile stated |
| TaskNotes [11] | Versioned calendar documentation | Applies to 4.12.0 | Core Bases; OAuth for remote sync | Device-conditional |
| Full Calendar Remastered [19] | Contributor-backed remastered fork | Documented 0.13.5 | Provider-specific capabilities | Refreshed mobile UX |
| Full Calendar [20] | Original plugin line; release-conditional | Release-specific | Note/daily-note/remote sources | Device-conditional |
| Calendar [21] | Daily-note tool; release-conditional | Obsidian floor 0.9.11 | Daily Note settings | Device-conditional |
| Property Kanban [22] | Community project; release-conditional | Release-specific | Frontmatter task-folder model | Device-conditional |
| Extended Base [23] | Lucy Roh’s GoodBases fork | 1.0.1 feature anchor | Obsidian 1.10.2+; Bases; manual install | Device-conditional |
| Projects [18] | Discontinued May 2025 | Removal notice July 18, 2025 | BRAT; Restricted mode off | Legacy deployment |

**Archived originals and forks differ:** Original DataLoom was archived on March 9, 2025. The aykutkardas fork explicitly claims continued development, recommends backups, and discloses a GitHub latest-release check as its sole network request. Historical blank-table reports against the original installation should not be treated as proof of the same failure in the maintained fork. [55] · Maintained fork policy [15] · [56]

**Projects is an existing-vault choice:** It historically offered a coherent editable project workspace and deliberately avoided plugin-specific additions to record notes. Nevertheless, the maintainer discontinued it in May 2025 and reported removal from the community list on July 18. Its Markdown portability is a reason migration can be manageable, not a reason to prefer it for a new four-view system. [18]

Section references:
[28] Notion Bases v1.13.0 <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Excerpt: "Existing install: Open Settings → Commu…"
[2] Note Database overview <https://community.obsidian.md/plugins/note-database> Excerpt: "metadata and the core Page preview plug…"
[9] Obsidian changelog <https://obsidian.md/changelog/> Excerpt: "Includes all new features and bug fixes…"
[53] Releases · obsidian-power-plugins/obsidian-power-bases · GitHub <https://github.com/obsidian-power-plugins/obsidian-power-bases/releases> Excerpt: "Release list See the README for what's…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "Create structured views of your data wi…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "Install it via BRAT with the repo Soula…"
[54] DB Folder archival report <https://obsidianmate.com/plugins/db-folder> Excerpt: "Its upstream repository was archived in…"
[15] DataLoom embeds <https://github.com/aykutkardas/obsidian-dataloom> Excerpt: "DataLoom is an Obsidian plugin for desk…"
[35] Dataview task exception <https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/>
[47] DB Folder changelog <https://rafaelgb.github.io/obsidian-db-folder/changelog/> Excerpt: "- FIx edit bug added with 1.1.0 ISSUE 47"
[17] MetaEdit synchronization recipe <https://metaedit.obsidian.guide/cookbook/kanban-status-sync/> Excerpt: "Section titled What you need - MetaEdit…"
[10] Kanban Action Planner scheduling <https://dsebastien.github.io/obsidian-kanban-action-planner/> Excerpt: "Kanban Action Planner adds a Kanban boa…"
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "Applies to TaskNotes 4.12.0 Calendar Vi…"
[19] Full Calendar Remastered overview <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/> Excerpt: "The latest release, 0.13.5, expands the…"
[20] Original Full Calendar <https://github.com/obsidian-community/obsidian-full-calendar> Excerpt: "Full Calendar also supports read-only I…"
[21] Calendar plugin behavior <https://community.obsidian.md/plugins/calendar> Excerpt: "currently requires Obsidian v0.9.11 or…"
[22] Property Kanban <https://community.obsidian.md/plugins/property-kanban>
[23] Extended Base Board <https://community.obsidian.md/plugins/extended-base>
[18] Projects view inventory <https://github.com/obsmd-projects/obsidian-projects> Excerpt: "Edit 2025-07-18: It's come to my attent…"
[55] Original archive <https://github.com/decaf-dev/obsidian-dataloom/releases> Excerpt: "This repository was archived by the own…"
[56] Historical issue <https://github.com/decaf-dev/obsidian-dataloom/issues/958> Excerpt: "This repository was archived by the own…"

### Mobile support and plugin interaction

**Mobile layout matters independently:** A plugin can run on a phone yet make a wide metadata grid awkward. The DB Folder review explicitly notes cumbersome wide tables, while Rowbase describes touch-friendly responsive targets and Power Board documents touch dragging. For phone-heavy work, compact Lists and calendars can be more useful than reproducing a desktop spreadsheet exactly. [50] · Rowbase mobile design [13] · [25]

**Shared properties create interaction risks:** Power lane rules, KAP automation, and another property editor can all write to notes. The practical concern is ownership of a property or transition: two independently configured rules may have different ideas about when to stamp a completion date or clear a deadline. Prefer one authoritative workflow rule for each such action rather than equating additional plugins with additional reliability.

**Styling is another shared surface:** Extended Base deliberately makes its toolbar restyling an optional snippet because the toolbar is Core UI, and enabling that snippet affects every Base toolbar. Its property editors also distinguish stored note fields from derived file/formula fields. These are concrete reasons to separate presentation customization from the database’s data model. [23]

Section references:
[50] DB Folder mobile review <https://notes-automate.com/posts/review-of-obsidian-db-folder-for-database-views/> Excerpt: "Read our complete review of Obsidian DB F…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "- Mobile responsive — Optimized for table…"
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "Six extra views for Obsidian's core Bases…"
[23] Extended Base Board <https://community.obsidian.md/plugins/extended-base>

## Collaboration and the limits of plugin stacks

### File synchronization is not simultaneous database editing

**Notion remains the team benchmark:** Its documentation states that multiple people can view and edit the same page or database simultaneously, with edits, comments, and suggestions appearing in real time. It also provides permissions that let people edit database content without changing properties, views, filters, or sorts. [57] · [58]

**Local files solve another problem:** The Obsidian candidates emphasize ownership, offline use, and integration with the vault. Those strengths can be decisive for personal work, but a shared folder and a change stamp are not equivalent to Notion’s coordinated editing and permission model. Power Bases’ optional frontmatter attribution records who changed something; it is not a concurrent-editing protocol. [25]

**Board files concentrate changes:** A Kanban discussion describes the difficulty of sharing a frequently changing Markdown board through Git in a small team. That is a user report, but it illustrates the mechanism: independent card changes can touch the same board file. Note-backed boards distribute record edits across notes, which changes the conflict surface without eliminating concurrent edits to the same note. [59]

**The practical judgment:** If simultaneous team editing, access control, and shared comments are central requirements, retaining Notion is the stronger documented choice. An Obsidian replacement is more compelling when personal ownership and local note integration outweigh that collaboration model.

Section references:
[57] Notion real-time collaboration <https://www.notion.com/help/collaborate-within-a-workspace> Excerpt: "There's no limit on the number of peopl…"
[58] Notion database permissions <https://www.notion.com/help/intro-to-databases> Excerpt: "access will still be able to create lin…"
[25] Power Bases formulas and write-back <https://www.obsidianstats.com/plugins/powerbases> Excerpt: "Power Bases adds ten more, the way Noti…"
[59] Kanban team-workflow discussion <https://github.com/community-archive/obsidian-kanban/discussions/558> Excerpt: "I checked out the Kanban board plugin a…"

### Evaluate combinations by their shared source

**The strongest combinations extend one engine:** Core plus Power Bases and Core plus KAP reuse Base-selected notes, while TaskNotes implements calendar views through Bases. These combinations have an architectural route to one record set. Matching filters, property names, and write ownership then determines whether the intended views behave coherently.

| Combination | Components enabled | Visual coverage | Record relationship | Judgment |
|---|---|---|---|---|
| Core + Power Bases | One core, one community plugin | 4/4 | Shared Base and note properties | Best general-purpose stack |
| Core + KAP | One core, one community plugin | 4/4 | Core Table/List; KAP Board/Calendar | Strongest planning alternative |
| Newer Core + TaskNotes | One core, one community plugin | 4/4 | Core layouts plus Bases Calendar | Strong recurrence-oriented option |
| Database Views + TaskNotes | Two community plugins plus Core | Four categories | `.dbview` plus note/Bases calendar | Complementary workspace |
| Rowbase + TaskNotes | Two community plugins plus Core | Four categories | `.rbase` plus note/Bases calendar | Property depth plus scheduling |
| Dataview + Kanban + MetaEdit | Three community plugins | Queries plus Board | Explicit lane-to-note bridge | Dashboard-first compromise |

The component relationships follow [3][10][11][12][13], and MetaEdit [17] documentation.

**Separate stores remain separate decisions:** Database Views plus TaskNotes is sensible when a user wants database records and a strong task calendar in one vault, but it should not be presented as switching the same record between four layouts. Rowbase plus TaskNotes has the same distinction. The calendar’s note record and the database’s row must have an explicit relationship before editing one can be expected to change the other.

**Read-oriented stacks have real value:** Dataview plus Kanban and MetaEdit can keep status-driven dashboards current after lane changes. It covers useful visual categories with portable Markdown, yet its Table and List are queries, its Calendar is a date-dot output, and the synchronization helper is board-driven. It is a good answer to “Can I build useful dashboards around a Markdown board?” rather than the closest answer to “Can I replace Notion’s editable multi-view database?”

**Stack takeaway:** Count shared records before counting plugins. Adding a calendar to a three-view database is only a full replacement when both operate on the intended record and property model.

Section references:
[3] Power Bases <https://community.obsidian.md/plugins/powerbases> Excerpt: "A yearly total is just (formula.mo_rent…"
[10] Kanban Action Planner scheduling <https://dsebastien.github.io/obsidian-kanban-action-planner/> Excerpt: "Define your columns by listing the stat…"
[11] TaskNotes calendar architecture <https://callumalpass.github.io/tasknotes/views/calendar-views/> Excerpt: "- Custom Days: Configurable multi-day v…"
[12] Database Views README <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Excerpt: "A plugin for Obsidian that brings Notio…"
[13] Rowbase README <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Excerpt: "Install from Obsidian Install with BRAT…"
[17] MetaEdit synchronization recipe <https://metaedit.obsidian.guide/cookbook/kanban-status-sync/> Excerpt: "Step 3: register the board in MetaEdit…"

## Which option should you choose?

**The best single-plugin recommendation:** Choose **Notion Bases** for the clearest documented combination of Table, draggable Board, Calendar, and general List in one community plugin. Its Markdown/frontmatter model, independent view settings, relations, rollups, and desktop/mobile statement make it the most straightforward overall match.

**The editing-focused alternative:** Choose **Note Database** when spreadsheet-style editing, grouped summaries, forms, configurable record presentation, and rich month/week/day calendars matter most. Its eight-view model and ordinary wikilink relations make it a serious alternative, not merely a secondary table plugin.

**The best complementary combination:** Choose **Core Bases plus Power Bases** when one native Base and ordinary note properties are priorities. It provides the most balanced extension across the requested views, particularly its richer Table and explicit Board/date write-back. The tradeoffs are dependence on the Core API, one-person maintenance, and file-intensive bulk operations.

| Your priority | Recommended path | Main advantage | Tradeoff to accept |
|---|---|---|---|
| One plugin with all four views | Notion Bases | Broad, coherent note-backed database | Calendar depth depends on release/use case |
| Rich standalone editing | Note Database | Range editing, summaries, forms, relations | More settings and embed-mode choices |
| Native Bases and general databases | Core + Power Bases | One Base; strong Table and Board | Extension maintenance and bulk writes |
| Status workflows and project hierarchy | Core + KAP | Explicit status/order/date writes | Defined schemas and development-stage change |
| Recurrence and Google/Microsoft calendars | Newer Core + TaskNotes | Bases calendar plus recurring-task controls | OAuth and task/date configuration |
| Offline formulas and relations | Rowbase | Rich `.rbase` computation and portability | Separate calendar architecture |
| Broad calendar-provider integration | Full Calendar Remastered | Recurrence and provider-specific event editing | Provider capabilities differ |
| Query dashboards over existing notes | Dataview, optionally Kanban/MetaEdit | Flexible metadata queries and Markdown boards | Read-oriented views and bridge conventions |
| Compact editable folder-organized Lists | Core + Extended Base | Inline properties and folder hierarchy | Static extension Board; manual installation |

**Evidence and measurement basis:** Coverage credits explicitly described layouts; query calendars and event-only lists are identified separately. Feature statements follow the cited documentation and release anchors, while performance figures are source-reported observations or maintainer claims rather than a common benchmark; the 20,000-write example is a conditional operation count. Continued maintenance, exact device behavior, and concurrent-write reliability depend on compatible releases, working mobile interactions, and the chosen file/provider synchronization path; cross-store synchronization is not inferred from note links alone.

**Final judgment:** For a personal Notion-style database in Obsidian, start with **Notion Bases**, **Note Database**, or **Core Bases plus Power Bases**. Choose a specialist stack only when its additional scheduling or workflow capabilities are worth the extra configuration—and keep one clearly defined source of truth for every record.

## References

[1] <https://github.com/bgarciamoura/obsidian-notion-bases-plugin> Notion Bases; Notion Bases feature inventory; Notion Bases storage and embeds; Notion Bases requirements; Notion Bases Calendar; Notion Bases List and multi-vi…
[2] <https://community.obsidian.md/plugins/note-database> Note Database overview; Note Database editing and starters; Note Database storage and export; Note Database embedded behavior; Note Database; Note Database rul…
[3] <https://community.obsidian.md/plugins/powerbases> Power Bases; Power Bases architecture; Power Bases requirements and maintenance; Power Calendar behavior; Power Bases setup; Power Bases file-intensive operati…
[4] <https://www.notion.com/help/views-filters-and-sorts> Notion database views; Notion filters, sorts, and groups
[5] <https://www.notion.com/help/data-sources-and-linked-databases> Notion linked data sources
[6] <https://www.notion.com/help/database-properties> Notion database properties; Notion formulas and properties
[7] <https://www.notion.com/help/guides/calendar-view-databases> Notion calendar databases
[8] <https://www.notion.com/help/tables> Notion Table view
[9] <https://obsidian.md/changelog/> Obsidian changelog; Core Kanban announcement
[10] <https://dsebastien.github.io/obsidian-kanban-action-planner/> Kanban Action Planner scheduling; KAP
[11] <https://callumalpass.github.io/tasknotes/views/calendar-views/> TaskNotes calendar architecture; TaskNotes filters and options; TaskNotes recurrence interactions; TaskNotes OAuth and span behavior; TaskNotes scheduled field…
[12] <https://github.com/PlantBasedStudio/obsidian-database-views/blob/main/README.md> Database Views README; Database Views; Database Views saved views; Database Views record navigation
[13] <https://github.com/Soulaymane01/Rowbase/blob/master/README.md> Rowbase README; Rowbase; Rowbase filtering and grouping; Rowbase computations; Rowbase title and note linking; Rowbase format; Rowbase offline and export policy
[14] <https://rafaelgb.github.io/obsidian-db-folder/>
[15] <https://github.com/aykutkardas/obsidian-dataloom> DataLoom embeds; DataLoom; DataLoom view preferences; Maintained fork
[16] <https://blacksmithgu.github.io/obsidian-dataview/queries/structure/> Dataview Calendar output; Dataview LIST and commands; Dataview query warning
[17] <https://metaedit.obsidian.guide/cookbook/kanban-status-sync/> MetaEdit synchronization recipe; MetaEdit workflow
[18] <https://github.com/obsmd-projects/obsidian-projects> Projects view inventory; Projects maintenance notice
[19] <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/> Full Calendar Remastered overview
[20] <https://github.com/obsidian-community/obsidian-full-calendar> Original Full Calendar
[21] <https://community.obsidian.md/plugins/calendar> Calendar plugin behavior
[22] <https://community.obsidian.md/plugins/property-kanban> Property Kanban
[23] <https://community.obsidian.md/plugins/extended-base> Extended Base Board; Extended Base folder grouping; Extended Base editing and styling; Extended Base integration boundaries
[24] <https://bgarciamoura.github.io/obsidian-notion-bases-plugin/> Notion Bases database relationships
[25] <https://www.obsidianstats.com/plugins/powerbases> Power Bases formulas and write-back; Power Bases; Power Table controls; Power rollups; Power Board behavior; Power Board mobile interaction; Power touch suppor…
[26] <https://rafaelgb.github.io/obsidian-db-folder/features/Properties/> DB Folder
[27] <https://acylation.github.io/obsidian-projects-docs/views/table> Projects
[28] <https://github.com/bgarciamoura/obsidian-notion-bases-plugin/releases> Notion Bases v1.13.0; Notion Bases formula aliases; Notion Bases board updates; Calendar duration update
[29] <https://rafaelgb.github.io/obsidian-db-folder/features/Displaying%20data/> DB Folder display controls
[30] <https://s-blu.github.io/obsidian-dataview/queries/data-commands/> Dataview data commands
[31] <https://www.notion.com/help/relations-and-rollups> Notion relations; Notion relation export behavior
[32] <https://rafaelgb.github.io/obsidian-db-folder/features/Formulas/> DB Folder formulas
[33] <https://forum.obsidian.md/t/bases-formula-cross-note-lookup-rollup/101990> Bases cross-note lookup discussion
[34] <https://obsidian.rocks/dataview-in-obsidian-a-beginners-guide/> Dataview interaction model
[35] <https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/> Dataview task exception; Dataview output portability; Dataview’s 2026 position
[36] <https://metaedit.obsidian.guide/guides/kanban-helper/> MetaEdit helper rules
[37] <https://dsebastien.github.io/obsidian-kanban-action-planner/configuration.html> Kanban Action Planner configuration; Kanban Action Planner filters and writable fields; Kanban Action Planner swimlanes; KAP date configuration
[38] <https://forum.obsidian.md/t/bases-kanban-manual-card-ordering-within-a-column-drag-and-drop-persisted-to-a-property/119092> Core manual-order discussion
[39] <https://github.com/obsidian-community/obsidian-kanban/releases> Kanban v2 features
[40] <https://community.obsidian.md/plugins/kanban> Nested lanes
[41] <https://github.com/dsebastien/obsidian-kanban-action-planner>
[42] <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/architecture/calendars/provider-implementations/> FCR Bases capability contract; FCR remote-provider behavior
[43] <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/events/manage/> FCR event management; Cross-calendar moves
[44] <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/events/recurring/> FCR recurrence model
[45] <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/calendars/dailynote/> FCR Daily Note behavior
[46] <https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar/user/views/workspaces/> FCR workspaces and filtering
[47] <https://rafaelgb.github.io/obsidian-db-folder/changelog/> DB Folder changelog
[48] <https://github.com/decaf-dev/obsidian-dataloom> Original DataLoom migration guidance
[49] <https://practicalpkm.com/moving-to-obsidian-bases-from-dataview/> Dataview-to-Bases migration
[50] <https://notes-automate.com/posts/review-of-obsidian-db-folder-for-database-views/> DB Folder mobile review
[51] <https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/>
[52] <https://forum.obsidian.md/t/bases-display-access-and-or-filter-using-the-notes-content/101378> Metadata and body-content discussion
[53] <https://github.com/obsidian-power-plugins/obsidian-power-bases/releases>
[54] <https://obsidianmate.com/plugins/db-folder> DB Folder archival report
[55] <https://github.com/decaf-dev/obsidian-dataloom/releases> Original archive
[56] <https://github.com/decaf-dev/obsidian-dataloom/issues/958> Historical issue
[57] <https://www.notion.com/help/collaborate-within-a-workspace> Notion real-time collaboration
[58] <https://www.notion.com/help/intro-to-databases> Notion database permissions
[59] <https://github.com/community-archive/obsidian-kanban/discussions/558> Kanban team-workflow discussion
