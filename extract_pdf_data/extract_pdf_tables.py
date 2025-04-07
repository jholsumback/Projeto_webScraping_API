import pandas as pd
import pdfplumber
from pathlib import Path
from compress_files import compress
from clear_directory import clear_path

project_dir = Path(__file__).resolve().parent
file_path = str(project_dir) +"\\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
zip_file_path = str(project_dir) +"\\zip_files"
csv_file_path = str(project_dir) +"\\extracted_data"
full_csv_file_path = csv_file_path +"\\extract_tables.csv"

dataframes = []
with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            dataframe = pd.DataFrame(table[1:], columns=table[0])
            dataframe = dataframe.rename(columns={
                'OD': 'Seg. Odontológica', 
                'AMB': 'Seg. Ambulatorial'
            })
            dataframes.append(dataframe)
if dataframes:
    clear_path(csv_file_path)
    final_dataframe = pd.concat(dataframes, ignore_index=True)
    final_dataframe.to_csv(full_csv_file_path, index=False, sep=';')
    compress(csv_file_path, zip_file_path, 'Teste_JhonatanSumback.zip')
    