"""
d:/Python_Code/ActeLocale/Scripts/python.exe d:/Python_Code/ActeLocale/Workload/pdfs_ocrx.py
"""


import configs
import PDFs.PDFs_OCR as ocr_funcs
from time import time
from Telegram_funcs import Send_Telegram_Message
from os import listdir

def main():
    time_start = time()
    Report_OCRed_fitz = 0
    Report_OCRed_poppler = 0
    Error_List = []

    Folder_PDFs= configs.Folder_PDFs_noannons
    Folder_TXTs= configs.Folder_TXTs
    Folder_TXTs_vfitz = f"{Folder_TXTs}_vfitz"
    Folder_TXTs_vpoppler = f"{Folder_TXTs}_vpoppler"

    Files_PDFs= ocr_funcs.files(configs.Folder_PDFs_noannons)
    Files_TXTs= set(ocr_funcs.files(configs.Folder_TXTs))
    Files_TXTs_vfitz = set(listdir(Folder_TXTs_vfitz))
    Files_TXTs_vpoppler = set(listdir(Folder_TXTs_vpoppler))

    Done= 0
    for pdfx in Files_PDFs:
        time_start_f = time()
        pdfx_strip = pdfx.split(".")[0]
        
        #if f"{pdfx_strip}.txt" in Files_TXTs: continue
        try:
            if pdfx.replace(".pdf",".txt") not in Files_TXTs_vfitz:

                Text1 = ocr_funcs.extract_text_vfitz(pdfx)
                Report_OCRed_fitz += 1
                time_end_f = time()
                took = int(time_end_f-time_start_f)
                print(f">>fitz<<Done {Report_OCRed_fitz} out of {len(Files_PDFs)} docs >>(text_len ={len(Text1)}<<, {pdfx_strip}) ({took} sec)<<")
        except Exception as e:
            Error_List.append(e)
            print(e)
            pass
        
        try:
            if pdfx.replace(".pdf",".txt") not in Files_TXTs_vpoppler:
                Text2 = ocr_funcs.extract_text_vpoppler(pdfx)
                Report_OCRed_poppler += 1
                time_end_f = time()
                took = int(time_end_f-time_start_f)
                print(f">>poppler<<Done {Report_OCRed_poppler} out of {len(Files_PDFs)} docs >>(text_len ={len(Text2)}<<, {pdfx_strip}) ({took} sec)<<")  
        except Exception as e:
            Error_List.append(e)
            print(e)
            pass
        print(f"{Files_PDFs.index(pdfx)} / {len(Files_PDFs)}>{'_'*60}")
        Done += 1
        

    time_end = time()
    took = int(time_end-time_start)
    print(f"Took {took} seconds")

    Report_str = f"""RSAL_OCR OCR_ed {Report_OCRed_fitz} fitz, {Report_OCRed_poppler} poppler,\
    {len(Error_List)} errors. Took {took} seconds""".replace("  ","")
    Send_Telegram_Message(configs.Telegram_Constantin, Report_str)

from sys import argv
if __name__ == "__main__":
    print("Executing the main")
    main()
else: 
    print(f"Imported {argv[0]}")