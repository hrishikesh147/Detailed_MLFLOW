from src.Detailed_MLFLow_project.config.configuration import Configuration_Manager
from src.Detailed_MLFLow_project.components.data_ingestion import DataIngestion
from src import logger

STAGE_NAME= "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            con1=Configuration_Manager()
            data_ingestion_configure=con1.data_ingestion_config()
            data_ingest=DataIngestion(config=data_ingestion_configure)
            data_ingest.download_data()
            data_ingest.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    dat=DataIngestionTrainingPipeline()
    logger.info(f"Stage {STAGE_NAME} started...")
    dat.main()
    logger.info(f"Stage {STAGE_NAME} COMPLETED...")
