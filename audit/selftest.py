#!/usr/bin/env python3
"""selftest — offline checks of the audit itself (ENG-STD-008 §2.2).

1. The check ids in standards/ENG-STD-008 equal the ids in audit/audit.py,
   in the same order, with the same level.
2. audit/projects.json names only known kinds and known check ids.
3. render.py renders a fixture report, including a private and an
   unreadable project, and leaks no evidence for the private one.

Usage: python3 audit/selftest.py      Exit: 0 all pass, 1 any failure.
Substrate: Python 3.11+ standard library. No network.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import audit  # noqa: E402
import render  # noqa: E402

failed = []


def check(cond, what):
    print(("ok   " if cond else "FAIL ") + what)
    if not cond:
        failed.append(what)


std = open(os.path.join(HERE, "..", "standards", "ENG-STD-008-contributor-readiness.md"), encoding="utf-8").read()
rows = re.findall(r"^\| `([a-z_0-9]+)` \| [^|]+\| [^|]+\| (MUST|SHOULD) \| (CRITICAL|HIGH|MEDIUM|LOW) ", std, re.M)
code = [(c[0], c[3], audit.SEVERITY[c[0]][0]) for c in audit.CHECKS]
check(rows == code, f"standard table matches audit.py: ids, levels, severities ({len(rows)} rows, {len(code)} checks)")
check(set(audit.SEVERITY) == {c[0] for c in audit.CHECKS}, "every check has a severity")
check(all(audit.SEVERITY[c][0] in ("HIGH", "CRITICAL") for c in ("security", "pinned", "perms", "supply", "signed", "seccons")),
      "security checks are never below HIGH (ENG-DEC-013)")

kinds = {"rust", "python", "spec", "docs", "standards"}
ids = {c[0] for c in audit.CHECKS}
cfg = json.load(open(os.path.join(HERE, "projects.json"), encoding="utf-8"))
for p in cfg["projects"]:
    check(set(p["kinds"]) <= kinds, f"{p['name']}: kinds known")
    check(set(p.get("overrides", {})) <= ids, f"{p['name']}: overrides name known checks")
    for o in p.get("overrides", {}).values():
        check(o["status"] in ("pass", "fail", "n/a", "not assessed") and o["why"], f"{p['name']}: override has a status and a reason")

secret = "SECRET-EVIDENCE-TEXT"
mk = lambda st, ev: {"id": "readme", "group": "Front door", "title": "README", "level": "MUST", "ref": "x",
                     "severity": "HIGH", "severity_basis": "x", "status": st, "evidence": ev}
fixture = {"generated": "2026-01-01T00:00Z", "projects": [
    {"name": "pub", "url": "https://example.invalid/pub", "kinds": ["rust"], "private": False, "readable": True,
     "head": "abc1234", "gaps": {"HIGH": 1}, "must": [1, 2], "should": [0, 0], "checks": [mk("pass", "README.md"), mk("fail", "no LICENSE")]},
    {"name": "priv", "url": "https://example.invalid/priv", "kinds": ["python"], "private": True, "readable": True,
     "head": "def5678", "must": [0, 1], "should": [0, 0], "checks": [mk("fail", secret)]},
    {"name": "gone", "url": "https://example.invalid/gone", "kinds": ["docs"], "private": False, "readable": False,
     "head": "", "must": [0, 0], "should": [0, 0], "checks": [mk("not assessed", "repository not readable with this token")]},
]}
html = render.page(fixture)
check(html.startswith("<!doctype html>") and "</html>" in html, "render produces a whole page")
check(secret not in html, "private project's evidence not rendered")
check("not assessed" in html, "unreadable project shown as not assessed")
check('class="sev HIGH"' in html, "failing check shows its severity")

sys.exit(1 if failed else 0)
