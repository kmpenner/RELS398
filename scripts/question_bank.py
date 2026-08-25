#!/usr/bin/env python3
"""RELS 398 wrapper for the shared Moodle question-bank builder.

The implementation lives in shared/scripts/question_bank.py so every course
builds banks the same way; question DATA stays here in scripts/banks/.
Do not fork the implementation — that is how shared and per-course copies
drift apart.

    python3 scripts/question_bank.py 1.1
    python3 scripts/question_bank.py 4.1,4.2,4.3
    python3 scripts/question_bank.py --all
"""
import runpy
import sys
from pathlib import Path

COURSE_DIR = Path(__file__).resolve().parent.parent
SHARED = COURSE_DIR.parent / "shared" / "scripts" / "question_bank.py"

if not SHARED.exists():
    sys.exit(f"shared question_bank not found at {SHARED}")

sys.argv = [str(SHARED), *sys.argv[1:], "--course-dir", str(COURSE_DIR)]
runpy.run_path(str(SHARED), run_name="__main__")
