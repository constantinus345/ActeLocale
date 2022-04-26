import PyPDF2

def remove_annots(input, output):
    #Filex = "E:/RSAL/Dispozitii_PDF/1435722.pdf"
    with open(input, 'rb') as pdf_obj:
        pdf = PyPDF2.PdfFileReader(pdf_obj)
        out = PyPDF2.PdfFileWriter()
        for page in pdf.pages:
            out.addPage(page)
            out.removeLinks()
        with open(output, 'wb') as f: 
            out.write(f)

from sys import argv
if __name__ == "__main__":
    print("Executing the main")
else: 
    print(f"Imported {argv[0]}")