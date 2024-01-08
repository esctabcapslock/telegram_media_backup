import os

def get_file_extension(file_path:str)->str:
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()
    return file_extension