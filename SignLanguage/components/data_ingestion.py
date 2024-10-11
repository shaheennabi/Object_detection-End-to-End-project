import os
import sys
from datetime import datetime
from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.entity.config_entity import DataIngestionConfig
from SignLanguage.entity.artifacts_entity import DataIngestionArtifact
from SignLanguage.utils.main_utils import Zipper
from SignLanguage.configuration.gdown_connection import Drive


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SignException(e, sys)

    def download_data(self) -> str:
        """
        Download the zip data into the specified data ingestion directory.
        """
        logging.info("Entered download_data method")
        try:
            # Get the data ingestion directory from config
            data_ingestion_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(data_ingestion_dir, exist_ok=True)

            # Specify the zip file path
            zip_file_path = os.path.join(data_ingestion_dir, "SignLangData.zip")

            # Download the file using the Drive downloader
            drive_downloader = Drive(destination=zip_file_path)
            drive_downloader.download_file()

            logging.info(f"Data downloaded to {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise SignException(e, sys)

    def extract_zip_file(self, zip_file_path: str) -> str:
        """
        Extract the zip file into the feature_store directory.
        """
        try:
            logging.info(f"Extracting {zip_file_path} into feature store")

            # Get the feature store path from config
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)

            # Unzip the downloaded file into the feature_store_path
            unzipper = Zipper(zip_file_path=zip_file_path, extract_to_folder=feature_store_path)
            unzipper.unzip()

            logging.info(f"Extraction completed. Files are stored in {feature_store_path}")
            return feature_store_path

        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Orchestrates the data ingestion process: downloading the zip file and extracting it.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            # Download the zip file
            zip_file_path = self.download_data()

            # Extract the zip file into the feature store directory
            feature_store_path = self.extract_zip_file(zip_file_path)

            # Create data ingestion artifact object to track paths
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info(f"Data ingestion artifact created: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
