from PIL import Image
from pdf2image import convert_from_path
from pytesseract import image_to_string, get_languages
import os
import configs
import fitz

filename = "1733961.pdf"
Files_PDFs_path =configs.Folder_PDFs
Files_TXTs_path = configs.Folder_TXTs
Files_jpg = "D:/Python_Code/Misc/Poppler conv"
filename_strip = filename.split(".")[0]

print(get_languages(config=''))

def extract_text(filename, Files_PDFs_path =configs.Folder_PDFs, Files_TXTs_path = configs.Folder_TXTs):
    poppler = configs.poppler
    filename_strip = filename.split(".")[0]

    doc = fitz.open(f"{Files_PDFs_path}/{filename}")
    npages = doc.pageCount 
    txt_all = ""

    for pageNo in range(npages):
        page = doc.loadPage(pageNo) # number of pages
        pix = page.get_pixmap() # if you need to scale a scanned image
        output = f"{Files_jpg}/{filename_strip}_{pageNo}.jpg" + str(pageNo) + '.jpg'
        pix.save(output) # skip this if you don't need to render a page
        text = str(((image_to_string(Image.open(output), lang='ron'))))
        txt_all += f"\n{text}\n"
        with open(f"{Files_TXTs_path}/{filename_strip}.txt", "w", encoding='utf-8') as text_file:
           text_file.write(txt_all)
    print(txt_all)
    return txt_all




























#doc = convert_from_path(f"{Files_PDFs_path}/{filename}", poppler_path= poppler, grayscale=True, strict = True, use_pdftocairo=True, fmt="jpeg") 

import tempfile
with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(f"{Files_PDFs_path}/{filename}", poppler_path= poppler,
     grayscale=True,  use_pdftocairo=True, fmt="jpeg", output_folder=Files_jpg)

import fitz #python -m pip install --upgrade pymupdf #NOT fitz

doc = fitz.open(f"{Files_PDFs_path}/{filename}")
page = doc.loadPage(0)
print(len(doc))  # number of page
pix = page.get_pixmap()
output = f"{Files_jpg}/outfile.png"
pix.save(output)

for page in doc:
    text = page.get_text().encode("utf8")
    print(text)

def extract_text(filename, Files_PDFs_path =configs.Folder_PDFs, Files_TXTs_path = configs.Folder_TXTs):
    filename_strip = filename.split(".")[0]
    doc = fitz.open(f"{Files_PDFs_path}/{filename}")
    #output = f"{Files_jpg}/outfile.png"
    #pix.save(output)
    txt_all= ""
    for pg in range(len(doc)):
        page_data = doc.loadPage(pg)
        print(len(doc))  # number of page
        pix = page_data.get_pixmap()
        #img_array = array(pix)
        #imgx = Image.fromarray(page_data)
        #txt = image_to_string(img_array, lang= "ron")
        txt = image_to_string(pix, lang= "ron")
        txt_all += f"\n{txt}\n"
    #with open(f"{Files_TXTs_path}/{filename_strip}.txt", "w", encoding='utf-8') as text_file:
     #   text_file.write(txt_all)
    return txt_all

filename = "1733961.pdf"
Files_PDFs_path =configs.Folder_PDFs
Files_TXTs_path = configs.Folder_TXTs
Files_jpg = "D:/Python_Code/Misc/Poppler conv"
poppler = configs.poppler
filename_strip = filename.split(".")[0]

djx = extract_text(filename)
print(djx)

def files(Folder):
    for (dirpath, dirnames, filenames) in os.walk(Folder):
        files= filenames
        break
    return files

def extract_text(filename, Files_PDFs_path =configs.Folder_PDFs, Files_TXTs_path = configs.Folder_TXTs):
    poppler = configs.poppler
    filename_strip = filename.split(".")[0]
    doc = convert_from_path(f"{Files_PDFs_path}/{filename}", poppler_path= poppler) 
    txt_all= ""
    for page_number, page_data in enumerate(doc):
        img_array = array(page_data)
        #imgx = Image.fromarray(page_data)
        txt = image_to_string(img_array, lang= "ron")

        txt_all += f"\n{txt}\n"
    with open(f"{Files_TXTs_path}/{filename_strip}.txt", "w", encoding='utf-8') as text_file:
        text_file.write(txt_all)
    return txt_all


from sys import argv
if __name__ == "__main__":
    print("Executing the main")
else: 
    print(f"Imported {argv[0]}")



