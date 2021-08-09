# Code for AudioBook........................................................................................

import pyttsx3
import PyPDF2
book = open('readThis.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(8)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()


# Rotating PDF File..........................................................................................

def PDFrotate(origFileName, newFileName, rotation):

	# creating a pdf File object of original pdf
	pdfFileObj = open(origFileName, 'rb')
	
	# creating a pdf Reader object
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	# creating a pdf writer object for new pdf
	pdfWriter = PyPDF2.PdfFileWriter()
	
	# rotating each page
	for page in range(pdfReader.numPages):

		# creating rotated page object
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(rotation)

		# adding rotated page object to pdf writer
		pdfWriter.addPage(pageObj)

	# new pdf file object
	newFile = open(newFileName, 'wb')
	
	# writing rotated pages to new file
	pdfWriter.write(newFile)

	# closing the original pdf file object
	pdfFileObj.close()
	
	# closing the new pdf file object
	newFile.close()
	

def main():

	# original pdf file name
	origFileName = 'readThis.pdf'
	
	# new pdf file name
	newFileName = 'rotated_File.pdf'
	
	# rotation angle
	rotation = 270
	
	# calling the PDFrotate function
	PDFrotate(origFileName, newFileName, rotation)
	
if __name__ == "__main__":
	# calling the main function
	main()


# Merging PDF files..............................................................................................

import PyPDF2


def PDFmerge(pdfs, output):
	# creating pdf file merger object
	pdfMerger = PyPDF2.PdfFileMerger()

	# appending pdfs one by one
	for pdf in pdfs:
		pdfMerger.append(pdf)

	# writing combined pdf to output pdf file
	with open(output, 'wb') as f:
		pdfMerger.write(f)


def main():
	# pdf files to merge
	pdfs = ['readThis.pdf', 'rotated_File.pdf']

	# output pdf file name
	output = 'combined_File.pdf'

	# calling pdf merge function
	PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
	# calling the main function
	main()
