#!/usr/bin/env python3
"""Validate a local Minecraft Java 26.3 source tree before attempting a Web port.
No proprietary files are uploaded or committed by this utility.
"""
from pathlib import Path
import argparse
import sys

def check(root: Path) -> int:
    root = root.expanduser().resolve()
    candidates = [
        root / "src" / "main" / "java",
        root / "java",
    ]
    source = next((p for p in candidates if p.is_dir()), None)
    if source is None:
        print("MISSING: Java source. Expected src/main/java/ or java/", file=sys.stderr)
        return 2
    java_files = list(source.rglob("*.java"))
    resources = [root / "src" / "main" / "resources", root / "resources"]
    assets = next((p for p in resources if p.is_dir()), None)
    print(f"Java source: {source}")
    print(f"Java files: {len(java_files)}")
    print(f"Resources: {assets if assets else 'MISSING'}")
    if not java_files:
        print("MISSING: Java files (directory is empty)", file=sys.stderr)
        return 3
    if not assets:
        print("WARNING: assets are absent; full client cannot load.")
    print("Source inventory only. This does NOT imply Web compatibility or a playable client.")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path, help="Local licensed Minecraft 26.3 source directory")
    sys.exit(check(ap.parse_args().source))
