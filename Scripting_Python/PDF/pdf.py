# pdf's in python
 #find the best library to process pdf - the best one is PyPDF2
 
import PyPDF2


with open ('dummy.pdf', 'rb') as file: #you have to read a binary file
    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
 #rotate the dummy.pdf by 180%
    with open('tilt.pdf', 'wb') as new_file:
         writer.write(new_file)
         
         
#combine pdfs 


import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)


# a tool that water marks all the pdf's for thousands of files or more

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()
                                                    
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open('watermarked_output.pdf', 'wb') as  file1:
        output.write(file1)