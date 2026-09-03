#!/usr/bin/env python3
"""RELS 398 wrapper for shared update_moodle_item.py."""
import runpy, sys
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent.parent
SHARED = COURSE_DIR.parent / "shared" / "scripts" / "update_moodle_item.py"

if not SHARED.exists():
    sys.exit(f"shared script not found at {SHARED}")

sys.argv = [str(SHARED), "--course-dir", str(COURSE_DIR), *sys.argv[1:]]
runpy.run_path(str(SHARED), run_name="__main__")
