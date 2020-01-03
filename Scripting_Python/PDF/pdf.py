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