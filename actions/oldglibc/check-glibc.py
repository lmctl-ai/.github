#!/usr/bin/env python3
"""Fail when an ELF binary needs a glibc newer than --max. Static binaries (no glibc symbols) pass.

usage: check-glibc.py --max 2.28 PATH_OR_GLOB...
"""
import argparse
import glob
import re
import subprocess
import sys


def floor(path):
    out = subprocess.run(["readelf", "-V", "-W", path], capture_output=True, text=True).stdout
    versions = sorted({tuple(map(int, v.split("."))) for v in re.findall(r"GLIBC_(\d+(?:\.\d+)+)", out)})
    return versions[-1] if versions else None


def is_elf(path):
    try:
        with open(path, "rb") as f:
            return f.read(4) == b"\x7fELF"
    except OSError:
        return False


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max", required=True)
    p.add_argument("paths", nargs="+")
    a = p.parse_args()
    ceiling = tuple(map(int, a.max.split(".")))
    files = sorted({f for pattern in a.paths for f in (glob.glob(pattern) or [pattern])})
    checked, failed = 0, 0
    for f in files:
        if not is_elf(f):
            print(f"{f}: not an ELF file (skipped)" if glob.glob(f) else f"{f}: not found", file=sys.stderr)
            failed += 0 if glob.glob(f) else 1
            continue
        v = floor(f)
        checked += 1
        shown = ".".join(map(str, v)) if v else "none (static)"
        if v and v > ceiling:
            print(f"FAIL {f}: needs glibc {shown}, limit {a.max}", file=sys.stderr)
            failed += 1
        else:
            print(f"ok   {f}: glibc {shown} (limit {a.max})")
    if checked == 0:
        print("no ELF binary was checked", file=sys.stderr)
        return 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
