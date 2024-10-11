import sys
from SignLanguage.exception import SignException
import zipfile
import os

class Zipper:
    
    def __init__(self, zip_file_path, extract_to_folder):
        self.zip_file_path = zip_file_path
        self.extract_to_folder = extract_to_folder

    try:
        def unzip(self):
            with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.extract_to_folder)
    

    except Exception as e:
        raise SignException(e, sys)