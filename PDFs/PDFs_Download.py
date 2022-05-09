from urllib.request import urlretrieve as download
from os import listdir
import configs
import DB_funcs
from random import uniform as rdm

print(rdm(0.1,0.3))
#urls_docs_str= "1972739, 1972572, 1972565"


def list_from_urls_docs_str(urls_docs_str):
    urls_docs_lis = set([x.replace(" ","") for x in str(urls_docs_str).split(",")])
    return urls_docs_lis


def download_pdf_rsal_one(relative_url_pdf, Folder= configs.Folder_PDFs):
    
    #relative_url_pdf= str("1972739")
    
    try:
        Disp_PDF= f"https://actelocale.gov.md/ral/act/downloadAct/{relative_url_pdf}"
        File_PDF=f'{Folder}/{relative_url_pdf}.pdf'
        if f"{relative_url_pdf}.pdf" not in listdir(Folder):
            download( Disp_PDF, File_PDF)
            print(f"downloaded {relative_url_pdf}")
        else:
            print(f"already there {relative_url_pdf}")
    except Exception as e:
        print(e)
    
    return File_PDF

"""import configs
Folder= configs.Folder_PDFs
Files= listdir(Folder)
#print(Files[1])
pdf = "2004024"
print(f"{pdf}.pdf" in Files)"""

def download_pdf_rsal_list(urls_docs, string=False, Folder= configs.Folder_PDFs):
    
    PDFs_Paths = []
    Files= listdir(Folder)
    #Files= listdir(configs.Folder_PDFs)
    print(f"Files PDF already = {len(Files)}")
    if string: 
        urls_docs = list_from_urls_docs_str(urls_docs)

    try:
        for pdf in urls_docs:
            Disp_PDF= f"https://actelocale.gov.md/ral/act/downloadAct/{pdf}"
            File_PDF=f'{Folder}/{pdf}.pdf'
            if f"{pdf}.pdf" not in Files:
                download( Disp_PDF, File_PDF)
                PDFs_Paths.append(pdf)
                print(f"downloaded {pdf} /remaining {len(urls_docs)- urls_docs.index(pdf)} out of {len(urls_docs)}")
            else:
                pass
                print(f"already there {pdf}")
            
    except Exception as e:
        print(e)
    
    return PDFs_Paths

def list_of_pfds (date_after = '2022-03-01'):
    #date_after = '2022-03-01'
    sql_pdfs = f"""
                SELECT urls_docs_str FROM public.rsal_data
                WHERE data_disp > '{date_after}'::date
                ORDER BY id DESC
                """

    pdfs0 = DB_funcs.read_sql_df(sql_pdfs)["urls_docs_str"].tolist()
    pdfs_list = []
    for pdfx in pdfs0:
        pdfs_list.extend(pdfx.split(";"))


    pdfs_list1 = [int(x) for x in pdfs_list if len(str(x))>4]
    pdfs_list2 = list(set(pdfs_list1))
    print(f"Common docs = {len(pdfs_list1) - len(pdfs_list2)}")
    print(f"Len docs = {len(pdfs_list2)}")

    return pdfs_list2

def main():
    date_after = '2022-04-22'
    Docs = list_of_pfds(date_after)
    download_pdf_rsal_list(Docs)

import sys
if __name__ == "__main__":
    main()
    print("Executing the main")
else: 
    print(f"Imported {sys.argv[0]}")