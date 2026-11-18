#!/usr/bin/env python3
"""render — turn an audit report into one static HTML page (the dashboard).

No scripts, no external requests: the page is the report, readable offline.
A private repository shows its name and statuses only, never evidence text
(governor, 2026-11-18).

Usage: audit/render.py report.json > site/index.html
Substrate: Python 3.11+ standard library.
"""

import json
import sys
from html import escape as e

GROUPS = ["Front door", "Change control", "Quality", "Security", "Versioning", "Rust", "Python", "Specification"]
REPO = "https://github.com/praveenprk/eng-principles"

CSS = """
:root{--bg:#fbfbfa;--fg:#1d1d1b;--muted:#6b6b66;--line:#e4e3df;--card:#fff;
--pass:#1f7a4d;--pass-bg:#e3f2ea;--fail:#b3261e;--fail-bg:#fbe7e5;--na:#8a8a84;--na-bg:#efefec;--warn:#8a5a00;--warn-bg:#fbf0d9;--bar:#e4e3df}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141413;--fg:#ecebe6;--muted:#a3a29b;--line:#2c2b29;--card:#1c1c1a;
--pass:#6fcf97;--pass-bg:#173525;--fail:#f28b82;--fail-bg:#3d1b18;--na:#8f8e88;--na-bg:#262624;--warn:#f2c46b;--warn-bg:#3a2e12;--bar:#2c2b29}}
:root[data-theme="dark"]{--bg:#141413;--fg:#ecebe6;--muted:#a3a29b;--line:#2c2b29;--card:#1c1c1a;
--pass:#6fcf97;--pass-bg:#173525;--fail:#f28b82;--fail-bg:#3d1b18;--na:#8f8e88;--na-bg:#262624;--warn:#f2c46b;--warn-bg:#3a2e12;--bar:#2c2b29}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1180px;margin:0 auto;padding:32px 16px 64px}
h1{font-size:24px;margin:0 0 4px;letter-spacing:-.01em}
h2{font-size:17px;margin:40px 0 12px}
p.sub{color:var(--muted);margin:0 0 24px}
a{color:inherit}
.wrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
tr:last-child td{border-bottom:0}
td.num{white-space:nowrap}
.meter{display:inline-block;width:72px;height:6px;border-radius:3px;background:var(--bar);vertical-align:middle;margin-right:8px;overflow:hidden}
.meter i{display:block;height:100%;background:var(--pass)}
.chip{display:inline-block;min-width:38px;text-align:center;padding:1px 7px;border-radius:999px;font-size:12px;font-weight:600;white-space:nowrap}
.pass{color:var(--pass);background:var(--pass-bg)}.fail{color:var(--fail);background:var(--fail-bg)}
.na{color:var(--na);background:var(--na-bg)}.part{color:var(--warn);background:var(--warn-bg)}
.kind{color:var(--muted);font-size:13px}
details{border:1px solid var(--line);border-radius:10px;background:var(--card);margin:12px 0}
summary{cursor:pointer;padding:12px 14px;font-weight:600;list-style-position:inside}
details table{border-top:1px solid var(--line)}
td.ev{color:var(--muted);font-size:13px;max-width:460px}
td.ref{color:var(--muted);font-size:12px;max-width:240px}
.legend{display:flex;flex-wrap:wrap;gap:10px 18px;color:var(--muted);font-size:13px;margin:16px 0 0}
footer{color:var(--muted);font-size:13px;margin-top:40px;border-top:1px solid var(--line);padding-top:16px}
"""

STATUS = {"pass": ("pass", "pass"), "fail": ("fail", "fail"), "n/a": ("na", "n/a"), "not assessed": ("na", "not assessed")}


def chip(status):
    cls, label = STATUS.get(status, ("na", status))
    return f'<span class="chip {cls}">{e(label)}</span>'


def meter(done, total):
    pct = 100 * done / total if total else 0
    return f'<span class="meter"><i style="width:{pct:.0f}%"></i></span>{done}/{total}'


def group_cell(checks, group):
    cs = [c for c in checks if c["group"] == group and c["status"] in ("pass", "fail")]
    if not cs:
        return '<span class="chip na">—</span>'
    ok = sum(c["status"] == "pass" for c in cs)
    cls = "pass" if ok == len(cs) else ("fail" if ok == 0 else "part")
    return f'<span class="chip {cls}">{ok}/{len(cs)}</span>'


def project_rows(p):
    order = {"fail": 0, "not assessed": 1, "pass": 2, "n/a": 3}
    rows = []
    for c in sorted(p["checks"], key=lambda c: (order.get(c["status"], 9), c["level"] != "MUST")):
        ev = "" if p["private"] else e(c["evidence"])
        rows.append(f'<tr><td>{e(c["title"])}<br><span class="kind">{e(c["group"])} · {e(c["id"])}</span></td>'
                    f'<td>{e(c["level"])}</td><td>{chip(c["status"])}</td><td class="ev">{ev}</td><td class="ref">{e(c["ref"])}</td></tr>')
    return "\n".join(rows)


def page(report):
    ps = report["projects"]
    head = "".join(f"<th>{e(g)}</th>" for g in GROUPS)
    summary = []
    for p in ps:
        name = f'<a href="{e(p["url"])}">{e(p["name"])}</a>' if not p["private"] else f'{e(p["name"])} <span class="kind">(private)</span>'
        if not p.get("readable", True):
            summary.append(f'<tr><td>{name}<br><span class="kind">{e(", ".join(p["kinds"]))}</span></td>'
                           f'<td colspan="{2 + len(GROUPS)}"><span class="chip na">not assessed</span> '
                           f'<span class="kind">repository not readable by the audit token</span></td></tr>')
            continue
        cells = "".join(f"<td>{group_cell(p['checks'], g)}</td>" for g in GROUPS)
        summary.append(f'<tr><td>{name}<br><span class="kind">{e(", ".join(p["kinds"]))} · {e(p["head"])}</span></td>'
                       f'<td class="num">{meter(*p["must"])}</td><td class="num">{meter(*p["should"])}</td>{cells}</tr>')
    details = []
    for p in ps:
        if not p.get("readable", True):
            continue
        fails = sum(c["status"] == "fail" for c in p["checks"])
        details.append(f'<details><summary>{e(p["name"])} — {fails} gap{"s" if fails != 1 else ""}'
                       f' · required {p["must"][0]}/{p["must"][1]} · recommended {p["should"][0]}/{p["should"][1]}</summary>'
                       f'<div style="overflow-x:auto"><table><thead><tr><th>Check</th><th>Level</th><th>Status</th><th>Evidence</th><th>Standard</th></tr></thead>'
                       f'<tbody>{project_rows(p)}</tbody></table></div></details>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Engineering Standards Dashboard</title><style>{CSS}</style></head>
<body><main>
<h1>Engineering standards dashboard</h1>
<p class="sub">Every governed project, measured against <a href="{REPO}/blob/main/standards/ENG-STD-008-contributor-readiness.md">ENG-STD-008</a>
from what is on GitHub now. Generated {e(report["generated"])} by <a href="{REPO}/tree/main/audit">audit/</a>.</p>
<div class="wrap"><table><thead><tr><th>Project</th><th>Required</th><th>Recommended</th>{head}</tr></thead>
<tbody>{"".join(summary)}</tbody></table></div>
<div class="legend"><span>{chip("pass")} all pass</span><span><span class="chip part">2/3</span> some pass</span>
<span>{chip("fail")} none pass</span><span><span class="chip na">—</span> does not apply</span>
<span>Required = MUST checks, Recommended = SHOULD checks, counting only checks that apply.</span></div>
<h2>Gaps by project</h2>
{"".join(details)}
<footer>The standards cited (ENG-STD, OpenSSF Best Practices and Scorecard, SemVer, Keep a Changelog, Rust API Guidelines,
PEP 621, IETF BCP 14 and RFC 3552, ISO/IEC/IEEE 12207, 29119, 29148) are used as reference models. Passing a check is not
certification or compliance with any of them (ENG-DEC-004). Private repositories show statuses only.</footer>
</main></body></html>
"""


def main():
    sys.stdout.write(page(json.load(open(sys.argv[1]))))


if __name__ == "__main__":
    main()
