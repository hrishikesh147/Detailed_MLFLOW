from src.Detailed_MLFLow_project.constants import *
from src.Detailed_MLFLow_project.utils.common import read_yaml,create_directories
from src.Detailed_MLFLow_project.entity.config_entity import (DataIngestionConfig,DataValidationConfig,Data_Transformation_Config)

class Configuration_Manager:
    def __init__(self,config_f=CONFIG_FILE_PATH,schema_f=SCHEMA_FILE_PATH,params_f=PARAMS_FILE_PATH):
        self.config_read=read_yaml(config_f)
        self.schema_read=read_yaml(schema_f)
        self.params_read=read_yaml(params_f)

        create_directories([self.config_read.artifacts_root])

    def data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config_read.data_ingestion
        create_directories([config.root_dir])

        get_data_ingestion_config=DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_data = config.unzip_data 

        )
        return get_data_ingestion_config
    

    def data_validation_config(self) ->DataValidationConfig:
        config=self.config_read.data_validation
        schema=self.schema_read.COLUMNS

        create_directories([config.root_dir])

        get_data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )

        return get_data_validation_config
    
    def data_transformed_configuration(self)->Data_Transformation_Config:
        config=self.config_read.data_transformation

        create_directories([config.root_dir])
    
        get_data_transformed_config=Data_Transformation_Config(
            root_dir=config.root_dir,
            data_transformation_input=config.data_transformation_input

        )

        return get_data_transformed_config
