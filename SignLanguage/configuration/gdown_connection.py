import sys
import os
import gdown
from SignLanguage.exception import SignException
from SignLanguage.constant.training_pipeline import DATA_DOWNLOAD_URL 

class Drive:
    def __init__(self, destination):
        self.destination = destination

    def download_file(self):
        try:
            data_download_url = os.getenv("DATA_DOWNLOAD_URL")
            if data_download_url is None:
                raise ValueError("Environment variable 'DATA_DOWNLOAD_URL' is not set.")
        
            file_id = data_download_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?export=download&id="
            
            gdown.download(prefix + file_id, self.destination, quiet=False)

            return os.path.basename(self.destination) 
            
        except Exception as e:
            raise SignException(e, sys)


