from PIL import Image
from pdf2image import convert_from_path
from pytesseract import image_to_string
from numpy import array
import os
import configs
import fitz

def files(Folder):
    for (dirpath, dirnames, filenames) in os.walk(Folder):
        files= filenames
        break
    return files

"""
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
    """

def extract_text_vfitz(filename, Files_PDFs_path =configs.Folder_PDFs_noannons, Files_TXTs_path = configs.Folder_TXTs, Folder_JPG = configs.Folder_JPG ):
    Files_TXTs_path = configs.Folder_TXTs
    Files_TXTs_path = f"{Files_TXTs_path}_vfitz"
    #print(Files_TXTs_path)
    if not os.path.exists(Files_TXTs_path):
        os.makedirs(Files_TXTs_path)

    poppler = configs.poppler
    filename_strip = filename.split(".")[0]

    doc = fitz.open(f"{Files_PDFs_path}/{filename}")
    npages = doc.pageCount 
    txt_all = ""

    for pageNo in range(npages):
        page = doc.load_page(pageNo) # number of pages
        pix = page.get_pixmap() # if you need to scale a scanned image
        output = f"{Folder_JPG}/{filename_strip}_{pageNo}.jpg"
        pix.save(output) # skip this if you don't need to render a page
        text = str(((image_to_string(Image.open(output), lang='ron'))))
        txt_all += f"\n{text}\n"
        with open(f"{Files_TXTs_path}/{filename_strip}.txt", "w", encoding='utf-8') as text_file:
           text_file.write(txt_all)
    #print(txt_all)
    return txt_all

def extract_text_vpoppler(filename, Files_PDFs_path =configs.Folder_PDFs_noannons, Files_TXTs_path = configs.Folder_TXTs):
    
    Files_TXTs_path = configs.Folder_TXTs
    Files_TXTs_path = f"{Files_TXTs_path}_vpoppler"
    #print(Files_TXTs_path)
    if not os.path.exists(Files_TXTs_path):
        os.makedirs(Files_TXTs_path)

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



