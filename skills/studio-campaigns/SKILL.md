---
name: studio-campaigns
description: Coordinate studio launch campaigns, expo and convention decks, booth graphics, swag, merchandise and product demo assets across the existing stills and motion workflows.
---

# Studio campaigns

Use for a studio launch, event package, demo day or a coordinated set of product assets.
Read `/workspace/brand/studio-context.md`, `voice.md` and `graphic-language.md` first.
Brand facts stay in that pack; this skill supplies the production workflow.

1. Record the audience, one message, call to action, deadline and exact deliverables in
   `BRIEF.md`. Put each factual claim beside its source and date. A prototype must be
   labeled as one. Never turn an event organizer or technology provider into a client,
   investor, sponsor or commercial partner without evidence.
2. Inspect supplied logos, screenshots and event specifications. Missing product UI gets
   a labeled schematic, never an invented screen presented as a working product. For print,
   ask for the vendor's template, finished size, bleed, safe area and color requirements
   before a production export. Draft a clearly labeled concept while specifications are missing.
3. Make one coherent visual concept across the set. Use real artwork from the brand pack.
   Recompose each size: a booth headline must read from a distance; a deck must read from
   the back of the room; a shirt or sticker must work at its physical size. Keep garment,
   embroidery and ink restrictions explicit. Mockups are previews, not print-ready artwork.
4. Use `stills` for launch cards, one-pagers and static decks; `data-viz` for system diagrams;
   `storyboard` and `motion-direction` for product demos, then `hyperframes`. For a demo,
   show problem, real product action, evidence and the requested next step. Get storyboard
   approval before animation. Never imply verified results from an unverified simulation.
5. Write `artifact-contract.json` using the example in
   [brand-design](../brand-design/references/artifact-contract.example.json).
   Preserve editable compositions and a small source/claim ledger beside the outputs.
6. Run `node /workspace/tools/brand-lint.mjs <composition.html>`, render every deliverable,
   inspect every render with `look`, and run `artifact-contract.mjs` as described in
   `media-production`. Motion also requires `video-gate.mjs` and `hyperframes check`.
   Report missing tools as blocked checks. Fix clipping, missing fonts and broken assets.
7. Deliver requested files with `upload_files`, identifying draft concepts and any vendor
   preflight still needed. Nothing is sent to a printer, posted, purchased or deployed.
