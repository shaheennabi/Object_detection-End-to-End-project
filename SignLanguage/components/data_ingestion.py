import os 
import sys
import gdown
from six.moves import urllib
import zipfile
from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.entity.config_entity import DataIngestionConfig
from SignLanguage.entity.artifacts_entity import DataIngestionArtifact




class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()): 
        try: 
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise SignException(e,sys)
        


    def down_load_data(self) -> str: 
        """
        Fetching Data from Google Drive URL with gdown package
        """

        pass 