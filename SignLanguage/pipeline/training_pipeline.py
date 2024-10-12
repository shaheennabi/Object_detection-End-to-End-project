import sys, os
from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.components.data_ingestion import DataIngestion
from SignLanguage.entity.config_entity import DataIngestionConfig
from SignLanguage.entity.artifacts_entity import DataIngestionArtifact
from SignLanguage.components.data_validation import DataValidation
from SignLanguage.entity.config_entity import DataValidationconfig
from SignLanguage.entity.artifacts_entity import DataValidationArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationconfig()




    def start_data_ingestion(self)-> DataIngestionArtifact:
            try: 
                logging.info(
                    "Entered the start_data_ingestion method of TrainPipeline class"
                )
                logging.info("Getting the data from URL")

                data_ingestion = DataIngestion(
                    data_ingestion_config =  self.data_ingestion_config
                )

                data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
                logging.info("Got the data from URL")
                logging.info(
                    "Exited the start_data_ingestion method of TrainPipeline class"
                )

                return data_ingestion_artifact

            except Exception as e:
                raise SignException(e, sys)


    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")


        try: 
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=self.data_validation_config)

            data_validation_artifact = data_validation.initiate_data_validation()


            logging.info("Performed the data validtion operation")
              
            logging.info("Exited the start_data_validation method of TrainPippeline class")


            return data_validation_artifact
         

        except Exception as e:
             raise SignException(e, sys)










    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)

        except Exception as e:
            raise SignException(e, sys)
