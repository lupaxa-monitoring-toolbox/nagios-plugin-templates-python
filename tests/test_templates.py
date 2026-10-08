"""Nagios status line and exit code for the template scripts."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASIC = ROOT / "src" / "basic" / "basic.py"
ADVANCED = ROOT / "src" / "advanced" / "advanced.py"

PREFIXES = {
    0: "OK",
    1: "WARNING",
    2: "CRITICAL",
    3: "UNKNOWN",
}


def _run(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Run a template script and capture its text output."""
    return subprocess.run(
        [sys.executable, str(script), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def _assert_sample_check(result: subprocess.CompletedProcess[str]) -> None:
    """Require one prefixed line and the matching exit code."""
    assert result.returncode in PREFIXES
    assert result.stderr == ""
    line = result.stdout.strip()
    prefix = PREFIXES[result.returncode]
    assert line.startswith(f"{prefix} - Test Value = ")
    value = int(line.rsplit("=", 1)[1].strip())
    assert 1 <= value <= 100


def test_basic_check_matches_exit_code() -> None:
    """basic.py reports the random sample with the matching status."""
    _assert_sample_check(_run(BASIC))


def test_advanced_check_matches_exit_code() -> None:
    """advanced.py accepts -w and -c, then reports the sample."""
    _assert_sample_check(_run(ADVANCED, "-w", "75", "-c", "90"))


def test_advanced_rejects_warning_at_or_above_critical() -> None:
    """Reject a warning level that is not below the critical level."""
    result = _run(ADVANCED, "-w", "90", "-c", "90")
    assert result.returncode == 3
    assert result.stdout.strip() == "UNKNOWN - Warn level MUST be lower than Critical level"
