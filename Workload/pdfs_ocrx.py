"""
d:/Python_Code/ActeLocale/Scripts/python.exe d:/Python_Code/ActeLocale/Workload/pdfs_ocrx.py
"""


import configs
import PDFs.PDFs_OCR as ocr_funcs
from time import time



def main():
    time_start = time()
    Files_PDFs= ocr_funcs.files(configs.Folder_PDFs_noannons)
    Files_TXTs= ocr_funcs.files(configs.Folder_TXTs)
    Done= 0
    for pdfx in Files_PDFs:
        time_start_f = time()
        pdfx_strip = pdfx.split(".")[0]
        if f"{pdfx_strip}.txt" in Files_TXTs: continue
        Text1 = ocr_funcs.extract_text_vfitz(pdfx)
        Text2 = ocr_funcs.extract_text_vpoppler(pdfx)
        Done += 1
        time_end_f = time()
        took = int(time_end_f-time_start_f)
        print(f"Done {Done} out of {len(Files_PDFs)} docs >>(text_len ={len(Text1)} && {len(Text2)}<<, {pdfx_strip}) ({took} sec)<<")

    time_end = time()
    took = int(time_end-time_start)
    print(f"Took {took} seconds")

from sys import argv
if __name__ == "__main__":
    print("Executing the main")
    main()
else: 
    print(f"Imported {argv[0]}")