import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

print("\nWelcome to PDF MERGER")
print('\nNote :- Kindly copy all the files you want to merge to the current folder.')

forward = input("Enter Y after copying all the files : ").lower()

if forward == "y":
    files = os.listdir()

    merger = PdfMerger()

    for pdf in files:
        if pdf.endswith(".pdf"):
            merger.append(pdf)
    print("\n--> All files merged!")

    merger.write("Merged file.pdf")
    merger.close()
print("\nThanks for using our program!")