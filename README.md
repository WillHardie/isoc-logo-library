# ISOC logo library

Client logo assets for ISOC proposal pages. Seeded 13 August 2026 from the Skoda coaching proposal v2 (standard wall, 90 marks) and its automotive sector composite (13 marks, ~280px, regenerate at higher resolution if large print quality is ever needed).

Structure: logos/ holds square PNG marks that sit clean on white. manifest.csv maps file to display name, tags and source. Naming is kebab-case; suffixes such as -wordmark distinguish alternative marks for the same brand.

The repository also carries two non-logo asset folders, outside manifest.csv. badges/ holds the accreditation badge marks (BAC, CPD, KHDA, Pearson) and the composed badge strip used by the ISOC document shell. certificates/specimen-certificate.png (566 x 396) is the specimen certificate image referenced by the document assembly shell v4.3 certification section and the proposal-logos skill. Do not treat these as logo gaps and do not overwrite them.

Destination: GitHub repo isoc-logo-library, read by the proposal-logos skill via raw.githubusercontent.com. Additions go through the skill, which writes new square white-safe marks and updates the manifest.
