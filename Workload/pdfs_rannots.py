"""
d:/Python_Code/ActeLocale/Scripts/python.exe d:/Python_Code/ActeLocale/Workload/pdfs_rannots.py
"""

import configs
from PDFs.PDFs_Remove_Annot import remove_annots
from shutil import copyfile
from Telegram_funcs import Send_Telegram_Message
from time import time
from os import listdir


def main():
    time_start = time()
    Report_annots = 0
    Report_copy = 0
    
    Docs = listdir(configs.Folder_PDFs)
    Docs_annots = listdir(configs.Folder_PDFs_noannons)
    print(Docs[1])
    #Remove annots
    for doc in Docs:
        if doc in Docs_annots: 
            print(f"Already {doc} rannots {'_'*20}")
            continue
        input = f"{configs.Folder_PDFs}/{doc}"
        output = f"{configs.Folder_PDFs_noannons}/{doc}"
        try:
            remove_annots(input, output)
            Report_annots += 1
            print(f"Removed annots for {doc}")
        except:
            copyfile(input, output)
            Report_copy += 1

    print(f"Removed annons of {Report_annots} docs")
    print(f"Just copied {Report_copy} docs")

    time_end = time()
    took = int(time_end-time_start)
    print(f"Took {took} seconds")

    Report_str = f"""RSAL_rannots> annots = {Report_annots}, copy= {Report_copy}. Took = {took} seconds.""".replace("  ","")
    Send_Telegram_Message(configs.Telegram_Constantin, Report_str)
    
from sys import argv
if __name__ == "__main__":
    print("Executing the main")
    main()
else: 
    print(f"Imported {argv[0]}")

