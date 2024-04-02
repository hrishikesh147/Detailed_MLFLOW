from src import logger
from src.Detailed_MLFLow_project.config.configuration import Configuration_Manager
from src.Detailed_MLFLow_project.components.data_transformation import DataTransformation,Data_Transformation_Config,Feature_Engineering
STAGE_NAME="Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info("data_transformation_started")
        try:
            conf=Configuration_Manager()
            con=conf.data_transformed_configuration()  
            fe=Feature_Engineering(con)
            fe1=fe.feature_E()
            dt=DataTransformation(con)
            dt.train_test_split()
        except Exception as e:
            raise e
