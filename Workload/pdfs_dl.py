"""
d:/Python_Code/ActeLocale/Scripts/python.exe d:/Python_Code/ActeLocale/Workload/pdfs_dl.py
"""

from PDFs.PDFs_Download import list_of_pfds, download_pdf_rsal_list
import configs
from PDFs.PDFs_Remove_Annot import remove_annots
from shutil import copyfile
from Telegram_funcs import Send_Telegram_Message
from time import time


def main():
    time_start = time()
    Report_copy = 0
    date_after = configs.Download_Date_After
    Docs = list_of_pfds(date_after)
    print(f"Grabbed {len(Docs)} docs after {date_after}")
    PDFs_Paths = download_pdf_rsal_list(Docs, Folder= configs.Folder_PDFs)
    print(f"Downloaded {len(Docs)} docs after {date_after}")
    time_end = time()
    took = int(time_end-time_start)
    print(f"Took {took} seconds")
    Report_str = f"""RSAL_dwpdfs Downloaded {len(PDFs_Paths)}, date_after= {date_after}, copy= {Report_copy}. Took = {took} seconds.""".replace("  ","")
    Send_Telegram_Message(configs.Telegram_Constantin, Report_str)
    
from sys import argv
if __name__ == "__main__":
    print("Executing the main")
    main()
else: 
    print(f"Imported {argv[0]}")

