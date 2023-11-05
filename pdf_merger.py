from PyPDF2 import PdfMerger
import os, sys


merger = PdfMerger()

args = sys.argv
files = args[1:]

try:
    for file in files:
        merger.append(file)
        merger.write("final.pdf")
        merger.close()
except:
    raise TimeoutError("Unable to merge.. Corrupted files detected!")