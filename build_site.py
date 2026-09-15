import markdown

with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

# Replace .ipynb links with .html so the dashboard links directly to the generated web pages
text = text.replace(".ipynb", ".html")

body = markdown.markdown(text, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Machine Learning & Statistical Inference Laboratory</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
  <style>
    body {{ max-width: 950px; margin: auto; padding: 24px; }}
    table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
    th, td {{ padding: 10px 12px; border: 1px solid #444; }}
    th {{ background: #222; color: #fff; }}
    pre {{ padding: 12px; border-radius: 6px; }}
  </style>
</head>
<body>
{body}
</body>
</html>"""

with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("dist/index.html generated successfully!")