import os

ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "GDRIVE_CONNECTION"


"""
Data Validation  related constant with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test","valid", "data.yaml"]


"""
Model Trainer related constant start with MODEL_TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16


"""
Model Pusher related constant start with MODEL_PUSHER var name
"""

BUCKET_NAME = "sign-language-22"
S3_MODEL_NAME = "best.pt"


