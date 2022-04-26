"""
d:/Python_Code/ActeLocale/Scripts/python.exe d:/Python_Code/ActeLocale/Workload/pdfs_dl.py
"""

from PDFs.PDFs_Download import list_of_pfds, download_pdf_rsal_list
import configs
from PDFs.PDFs_Remove_Annot import remove_annots
from shutil import copyfile


def main():
    date_after = '2019-10-01'
    Docs = list_of_pfds(date_after)
    print(f"Grabbed {len(Docs)} docs after {date_after}")
    download_pdf_rsal_list(Docs, Folder= configs.Folder_PDFs)
    print(f"Downloaded {len(Docs)} docs after {date_after}")
    #Remove annots
    for doc in Docs:
        input = f"{configs.Folder_PDFs}/{doc}.pdf"
        output = f"{configs.Folder_PDFs_noannons}/{doc}.pdf"
        try:
            remove_annots(input, output)
        except:
            copyfile(input, output)

    print(f"Removed annons of {len(Docs)} docs after {date_after}")

from sys import argv
if __name__ == "__main__":
    print("Executing the main")
    main()
else: 
    print(f"Imported {argv[0]}")

