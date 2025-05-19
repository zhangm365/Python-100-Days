"""
Python 读取 PDF 文件
"""

from pypdf import PdfReader

reader = PdfReader("test.pdf")
for page in reader.pages:
    print(page.extract_text())
