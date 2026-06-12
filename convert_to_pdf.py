#!/usr/bin/env python3
import os
import markdown2
from weasyprint import HTML, CSS
from pathlib import Path

# Папка с файлами
folder = "/Users/Admin/Desktop/игра"
os.chdir(folder)

# Все MD файлы для конверсии
md_files = [
    "README.md",
    "СПЕЦИФИКАЦИЯ_ИГРЫ.md",
    "ПЛАН_А_MVP.md",
    "ПЛАН_B_FULL.md",
    "ФИНМОДЕЛЬ.md",
    "ТАСК_ЛИСТЫ_ОЛЕГ.md",
    "ТАСК_ЛИСТЫ_ЛЕВА.md",
    "ПОЛНЫЙ_ПЛАН.md"
]

# CSS для красивого вида
css_string = """
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
        }
        h1 { color: #667eea; font-size: 32px; margin-top: 40px; margin-bottom: 20px; border-bottom: 2px solid #667eea; }
        h2 { color: #764ba2; font-size: 24px; margin-top: 30px; margin-bottom: 15px; }
        h3 { color: #667eea; font-size: 18px; margin-top: 20px; margin-bottom: 10px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #f5f5f5; font-weight: bold; }
        code { background-color: #f5f5f5; padding: 2px 6px; border-radius: 3px; font-family: monospace; }
        pre { background-color: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; }
        ul, ol { margin: 15px 0; padding-left: 30px; }
        li { margin: 8px 0; }
        a { color: #667eea; text-decoration: none; }
        a:hover { text-decoration: underline; }
        hr { border: none; border-top: 2px solid #ddd; margin: 30px 0; }
        blockquote { border-left: 4px solid #667eea; padding-left: 15px; margin-left: 0; color: #666; }
        .page-break { page-break-after: always; }
    </style>
"""

print("🔄 Конвертирую файлы в PDF...\n")

for md_file in md_files:
    try:
        # Читаем MD файл
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Конвертируем MD в HTML
        html_content = markdown2.markdown(content, extras=['tables', 'fenced-code-blocks'])

        # Добавляем CSS и обёрнем в HTML
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            {css_string}
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # Создаём PDF файл
        pdf_name = md_file.replace('.md', '.pdf')
        HTML(string=full_html).write_pdf(pdf_name)

        print(f"✅ {md_file:30} → {pdf_name}")

    except Exception as e:
        print(f"❌ {md_file:30} ОШИБКА: {e}")

print("\n🎉 Все файлы конвертированы в PDF!")
print("📁 Папка: /Users/Admin/Desktop/игра/")
