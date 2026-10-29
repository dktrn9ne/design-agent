"""The studio defaults must reach the real sandbox manifest without network or model keys."""

from __future__ import annotations

import base64
import hashlib
import re
from pathlib import Path

from design_agent.brand.schema import load_brand_pack, render_tokens_css
from design_agent.config import Settings
from design_agent.workspace.manifest import build_manifest

ROOT = Path(__file__).resolve().parents[2]
STUDIO = ROOT / "brands/l1brary-labs"


def test_studio_pack_is_default_and_stages_original_assets_and_context() -> None:
    settings = Settings(_env_file=None)
    pack = load_brand_pack(settings.resolved_brand_path(ROOT), project_root=ROOT)
    assert pack.brand.name == "L1brary Labs"
    assert settings.slack_name == "L1brary Labs Design"
    assert (STUDIO / "tokens.css").read_text() == render_tokens_css(pack)
    manifest = build_manifest(ROOT, pack)
    paths = {str(asset.destination) for asset in manifest.assets}
    assert "/workspace/brand/studio-context.md" in paths
    assert "/workspace/brand/logos/lockup.svg" in paths
    assert "/workspace/brand/logos/mark.svg" in paths
    assert "/workspace/skills/studio-campaigns/SKILL.md" in paths
    assert not any(".env" in path for path in paths)


def test_operator_pack_takes_precedence(tmp_path: Path) -> None:
    override = tmp_path / "brand"
    override.mkdir()
    (override / "brand.toml").write_text("name = 'Operator pack'\n")
    assert Settings(brand_path=override, _env_file=None).resolved_brand_path(ROOT) == override


def test_logo_wrappers_embed_original_bytes_without_redrawing() -> None:
    for wrapper, original in (
        ("lockup.svg", "l1brary-labs-full.jpeg"),
        ("mark.svg", "l1brary-monogram-clean.png"),
    ):
        svg = (STUDIO / "logos" / wrapper).read_text()
        match = re.search(r"base64,([A-Za-z0-9+/=]+)", svg)
        assert match is not None
        data = (STUDIO / "logos" / original).read_bytes()
        assert base64.b64decode(match[1]) == data
        assert hashlib.sha256(data).hexdigest() in (STUDIO / "sources.md").read_text()
