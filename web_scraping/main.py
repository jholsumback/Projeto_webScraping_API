from pathlib import Path

from clear_directory import clear_path
from compress_files import compress
from download_attachments import download_files_web_scraping

def download_compress_files():
    filename = 'anexos.zip'
    url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
    project_dir = Path(__file__).resolve().parent
    file_path = str(project_dir) +"\\files"
    zip_file_path = str(project_dir) +"\\zip_files"

    clear_path(file_path)
    download_files_web_scraping(url, file_path)
    compress(file_path, zip_file_path, filename)

download_compress_files()