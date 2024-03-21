from src.Detailed_MLFLow_project.config.configuration import Configuration_Manager
from src.Detailed_MLFLow_project.components.data_validation import Data_validation
from src import logger

class DataValidation_training_pipeline:
    def __init__(self):
        pass

    def main(self):
        STAGE="Data Validation Stage"

        try:
            con1=Configuration_Manager()
            data_val_configure=con1.data_validation_config()
            data_val=Data_validation(config=data_val_configure)
            data_val.check_data_validation()
        except Exception as e:
            raise e
        



