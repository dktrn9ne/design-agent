# L1brary Labs Design

This fork configures LangChain's Design Agent for L1brary Labs. The shared Deep Agents
assembly, rendering tools, gates, provider support and deployment paths are retained.
No deployment or change to the existing studio website is part of this setup.

## What is configured

- `instructions.md`: studio identity, evidence-based project claims and campaign routing.
- `brands/l1brary-labs/`: website-derived tokens, original logo images, offline SVG wrappers,
  portable open fonts, voice, graphic language and studio context. `sources.md` records
  provenance, checksums and pending brand review. Artwork is not licensed as CC0.
- `skills/studio-campaigns/`: launch sets, expo decks, booth graphics, merchandise concepts
  and product demos using existing rendering workflows.
- Default brand resolution: an operator's configured pack first, then the bundled studio
  pack, then the upstream sample. `design-agent demo` intentionally uses the upstream sample.
- Slack display name: `L1brary Labs Design`. No Slack account has been connected.

## Install and run

Requirements: Python 3.11+, uv and Docker with Linux containers for local sandbox runs.
On Windows use Docker Desktop's Linux container mode; WSL is an alternative for the CLI.

```bash
uv sync --frozen --all-extras --dev
uv run design-agent brand validate
uv run design-agent fonts verify
uv run design-agent doctor
uv run design-agent sandbox build
uv run design-agent demo
```

The demo uses a scripted model and no provider keys. It verifies the upstream rendering
path, not creative quality or the studio brand. The brand and manifest tests are offline:

```bash
uv run pytest -q tests/unit/test_studio_brand.py tests/unit/test_brand_schema.py
```

For real requests, copy `.env.example` to the ignored `.env` and set `ANTHROPIC_API_KEY`
securely in your editor. The default Anthropic model is inherited from upstream. Leave unused
keys empty. No credentials are bundled, created or reused by this customization.

```bash
uv run design-agent ask "Make a 1200x627 L1brary Labs launch card. Use the exact headline: Culture builds better tech."
uv run design-agent ask "Create a 6-slide 1920x1080 expo deck for L1brary Labs. Use the studio context and label research status."
uv run design-agent ask "Draft a booth banner and shirt concept for L1brary Labs. Vendor specifications are pending; mark both as concepts."
uv run design-agent ask "Storyboard a 30-second Cadence demo from my attached screenshots. Preserve the actual UI and flag unsupported claims."
```

Finals land in `workspace/out/<thread>/`; `--thread <id>` continues an existing request.
Use `workspace/brand/` with `DESIGN_AGENT_BRAND_PATH=workspace/brand` for a private pack.
`brand init` still initializes the original sample: do not run it to activate this studio pack.

## No-key studio preview on Windows

`examples/l1brary-launch/card.html` is an editable fixture, not an AI-generated result.
It exercises the real still renderer with the studio pack. With Node and Edge installed:

```powershell
npm.cmd ci --ignore-scripts --prefix sandbox/render
$env:DESIGN_AGENT_RENDER_DIR = (Resolve-Path sandbox/render).Path
$env:DESIGN_AGENT_BROWSER = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
node workspace/tools/brand-lint.mjs examples/l1brary-launch/card.html --root . --tokens brands/l1brary-labs/tokens.json --json
node workspace/tools/html2png.mjs ../examples/l1brary-launch/card.html --out out/studio-preview --name l1brary-launch --size 1200x627 --size 1080x1080 --size 1080x1350 --require-font Fraunces --require-font Inter
```

Outputs are under `workspace/out/studio-preview/`. This preview does not replace the Docker
demo or a live creative-agent evaluation. It calls no model or media provider.

## Providers and optional services

| Capability | Dependency |
| --- | --- |
| Scripted demo | Docker sandbox; no model key |
| Creative agent | Anthropic key by default; model usage is paid |
| Image generation | Optional OpenAI key; separate paid usage |
| Voice, music, effects | Optional ElevenLabs key; separate paid usage |
| Transcription | Optional Groq key |
| Managed deployment / sandbox | LangSmith account and key; hosting may be paid |
| Paper canvas | Optional Paper Desktop/bridge configuration |

See [models](models.md), [integrations](integrations.md), [self-hosting](self-hosting.md)
and [MDA deployment](deploy-mda.md). Set a job budget before live work; it is a soft
approval threshold, not a provider billing limit. Adding a key or building a sandbox does not
deploy the agent. Publishing a sandbox, connecting Slack and deploying remain separate actions.

## Brand review

The pack follows the public website observed October 29, 2026. It does not reproduce an
unprovided expo moodboard. Fraunces/Inter/Fragment Mono are explicit open-font substitutes
for Georgia/Arial/generic monospace. Square corners, spacing, strokes and logo minimums are
draft production defaults. Review those choices before publishing. Obtain vector masters,
reversed artwork and printer specifications before production merchandise or booth printing.

Upstream source: https://github.com/langchain-ai/design-agent, baseline
`9fd563be8be0f3a2c956599f8ed4672ae0d1f281`. Apache-2.0 license and notices are retained.
