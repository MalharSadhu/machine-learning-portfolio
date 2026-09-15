import markdown
import re

with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

# Fix link targets from notebook to html
text = text.replace(".ipynb", ".html")

# Render Markdown with tables and fenced code blocks
body = markdown.markdown(text, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Machine Learning & Statistical Inference Portfolio</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
  <style>
    body {{ max-width: 950px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
    table {{ width: 100%; border-collapse: collapse; margin: 25px 0; }}
    th, td {{ padding: 12px 14px; border: 1px solid #444; }}
    th {{ background: #1f2428; color: #fff; }}
    pre {{ background: #161b22; padding: 16px; border-radius: 6px; overflow-x: auto; }}
    code {{ font-family: Consolas, monospace; }}
    a {{ color: #58a6ff; }}
  </style>
</head>
<body>
{body}
</body>
</html>"""

with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Site regenerated successfully!")