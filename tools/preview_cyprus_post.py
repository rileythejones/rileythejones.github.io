"""Render the current post for review without requiring a Jekyll installation."""
from pathlib import Path
from html import escape
import re
import yaml
from markdown_it import MarkdownIt
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/"_drafts/larnaca-temperature.md").read_text()
_,front,body=text.split("---",2)
metadata=yaml.safe_load(front)
title=re.search(r"^title:\s*(.+)$",front,re.M).group(1)
body=re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}",r"\1",body)
body=MarkdownIt("commonmark",{"html":True}).enable("table").render(body)
assert "{{" not in body
head="""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__ | Draft preview</title><style>*{box-sizing:border-box}body{margin:0;color:#20353e;background:#fff;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;font-size:17px;line-height:1.7}main{max-width:1000px;padding:34px 28px 60px;margin:auto}.status{font-size:11px;font-weight:650;letter-spacing:.12em;text-transform:uppercase;color:#70828b;margin:0 0 12px}h1{font-size:36px;line-height:1.2;letter-spacing:-.025em;margin:0 0 25px;font-weight:650}h2{font-size:25px;line-height:1.3;margin:38px 0 15px;font-weight:650}p{margin:0 0 19px}a{color:#246482;text-underline-offset:3px}iframe{display:block;max-width:100%;margin:0 0 10px}a:focus-visible{outline:3px solid #f5b849;outline-offset:3px}table{width:100%;border-collapse:collapse;margin:27px 0 21px;font-size:15px;line-height:1.5}th,td{padding:12px;text-align:left;border-bottom:1px solid #dbe4e8}th{background:#f1f6f8;font-weight:650}tbody tr:last-child td{border-bottom:2px solid #b8ccd5}@media(max-width:600px){main{padding:23px 15px 40px;font-size:16px}h1{font-size:29px}h2{font-size:22px}iframe{width:calc(100% + 20px);max-width:none;margin-left:-10px}}</style></head><body><main><p class="status">Draft preview</p><h1>__TITLE__</h1>"""
styles="".join('<link rel="stylesheet" href="'+escape(path,quote=True)+'">' for path in metadata.get("css",[]))
scripts="".join('<script src="'+escape(path,quote=True)+'"></script>' for path in metadata.get("js",[]))
html=head.replace("__TITLE__",escape(title)).replace("</head>",styles+"</head>")+body+"</main>"+scripts+"</body></html>"
out=ROOT/"_preview/larnaca-temperature.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html)
print("Updated draft preview:",out)
