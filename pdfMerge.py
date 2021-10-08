from PyPDF2 import PdfFileMerger, PdfFileReader

pdf  = []
for i in range(100):
    pdf.append([str(i), str(i) + "-Answers"])

for c in pdf:
    merger = PdfFileMerger()
    for filename in c:

        merger.append(PdfFileReader(filename + ".pdf", 'rb'))

    merger.write("a" + c[0] + "-output.pdf")
