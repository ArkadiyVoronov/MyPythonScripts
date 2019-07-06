# !/usr/bin/env python

try:
    import docx
    from docx.shared import Inches
except:
    sys.exit("[!] Install the docx writer library as root or through sudo: pip install python-docx")
