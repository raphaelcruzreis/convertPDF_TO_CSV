# PYTHON SCRIPT DESMONSTRATION READIG TABLES FROM PDF FILE AND SAVING THE INTO CSV AND EXCEL FILES 
# USING TABULA MODULE

# tabula.py is a simple wrapper OF table-java
# Toy can read tables from PDF and conveter into pandas DataFrame

# import necessary packages 
# the module can be install using the command -pip install tabula.py
# https://pypi.org/project/tabula-py/

import tabula

inputPDF = '/storage/user/localfile/file.pdf'

df = tabula.read_pdf(\inputPDF)

print("\nTABLE FROM PDF FILE\n\n" + str(df))

PDF_T_CSV = '/storage/user/localfile/FILE_PDF_TO_CSV.csv'
PDF_T_EXCEL = '/storage/user/localfile/FILE_PDF_TO_EXCEL.xls'

tabula.convert_into(\inputPDF, PDF_T_CSV, output_format='csv', pages='all')
print("\nSUCESSFULLY CONVERTED INTO CSV FILE")

df = to.excel(PDF_toEXCEL, index=false)
print("\nSUCESSFULLY CONVERTED INTO EXCEL FILE")

