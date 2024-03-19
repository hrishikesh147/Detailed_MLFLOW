from src import logger
from src.Detailed_MLFLow_project.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline 


STAGE_NAME="Data Ingestion"

dat=DataIngestionTrainingPipeline()
logger.info(f"Stage {STAGE_NAME} started...")
dat.main()
logger.info(f"Stage {STAGE_NAME} COMPLETED...")