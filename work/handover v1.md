# Logo gap sourcing — handover v1

Written 23 September 2026 at the end of the client records Cowork session (handover v7 in isoc-client-database).
Repo: WillHardie/isoc-logo-library. Clone on the Mac at Desktop/Claude/isoc-logo-library; it pushes with the
keychain credentials. The Cowork container cannot use the GitHub token; move work in and out with git bundles
through the connected folder Desktop/Claude, as in isoc-client-database/pipeline/handover v7.md.

## Will's rulings, 23 September 2026

- Every client in the database is a logo wall and client list candidate. Thin data (no recent invoice, no
  Notable flag, no record, no Drive folder) is never a reason to leave a client out. The skill
  isoc-proposal-logos v1.5 carries this (`--min-score 0`); proposed to Will as a skill update the same day.
- Scope of sourcing: recognisable organisations only, judged on the brand, not on how much data ISOC holds.
  Individuals and tiny local firms get no logo and stay on named client lists.
- All the standing rulings in the isoc-proposal-logos skill apply: parent mark for units and country offices,
  successor mark for renamed or merged clients, coat of arms for ministries without a mark, spec PNG square
  400px minimum, at most two automated channels per logo, names that cannot be resolved go to Will.

## Input

`work/logo-gaps-v1.csv`: the 1,329 database rows (1,316 distinct match names) that library.py could not match
against the manifest on 23 September 2026, with sector, country, parent group, Notable flag and whether a history
record or Drive folder exists. The last three are context only, never a filter.

## The job, in order

1. **Alias pass (no sourcing).** For each gap, decide whether an existing logo already covers it under Will's
   rulings (spelling variants such as BEEAH and Bee'ah, parents such as UNDP Kosovo to the United Nations or UNDP,
   successors). Add the database names to that logo's `aliases` in manifest.csv. Rerun library.py to confirm.
2. **Triage the rest** into three lists: recognisable (source it), not recognisable or an individual (no logo),
   unsure (goes to Will as a tick-list page with checkboxes and a copy button, per his standing preference).
3. **Source** the recognisable list to spec, commit PNG (and SVG where the source is SVG) plus manifest rows.
   Two channels per logo; failures go on one list for Will at the end, not one by one.
4. **Check** the delivered files themselves: every new manifest row has a file, every file is square and at
   least 400px, and library.py now matches each sourced client.

## Not verified

- How many of the 1,316 are recognisable. An estimate before triage would be a guess.
- Whether a sourcing run this size needs the Workflow tool (subagents). Will has not opted into a workflow for
  this job; ask him before launching one.
