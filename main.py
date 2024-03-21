from src import logger
from src.Detailed_MLFLow_project.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline 
from src.Detailed_MLFLow_project.pipeline.stage02_data_validation import DataValidation_training_pipeline


STAGE_NAME="Data Ingestion"
dat=DataIngestionTrainingPipeline()
logger.info(f"Stage {STAGE_NAME} started...")
dat.main()
logger.info(f"Stage {STAGE_NAME} COMPLETED...")


STAGE_NAME="Data Validation Stage"
obj=DataValidation_training_pipeline()
logger.info(f"Stage {STAGE_NAME} started...")
obj.main()
logger.info(f"Stage {STAGE_NAME} COMPLETED...")
