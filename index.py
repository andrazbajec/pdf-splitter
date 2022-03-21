from PyPDF2 import PdfFileWriter, PdfFileReader
import os

fileName = input("File name (without '.pdf'): ").replace(".pdf", "")
switchElements = input("Reverse the order of the pages (Y/N): ").lower() == "y"
inputPdf = PdfFileReader(open("%s.pdf" % fileName, "rb"), strict = False)

pages = []

for i in range(inputPdf.numPages):
    output = PdfFileWriter()
    pages.append(inputPdf.getPage(i))

    if (i + 1) % 2 == 0:
        if switchElements:
            pages.reverse()

        for page in pages:
            output.addPage(page)

        pages = []

        if not os.path.exists("export"):
            os.makedirs("export")

        if not os.path.exists("export/%s" % fileName):
            os.makedirs("export/%s" % fileName)

        with open("export/%s/%s_%s.pdf" % (fileName, fileName, (int(i / 2) + 1)), "wb") as outputStream:
            output.write(outputStream)
