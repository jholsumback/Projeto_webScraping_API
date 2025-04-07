import zipfile
from pathlib import Path

def compress(path, zip_path, filename):
    dir_path = Path(path)
    dir_zip_path = Path(zip_path)
    zip_file = dir_zip_path/filename
    with zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for file in dir_path.iterdir():
            if file.is_file():
                zipf.write(file, arcname=file.name)
