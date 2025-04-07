from pathlib import Path

def clear_path(path):
    dir_path = Path(path)
    for file in dir_path.iterdir():
        if file.is_file():
            file.unlink()