from src import logger
import pandas as pd
from src.Detailed_MLFLow_project.entity.config_entity import DataValidationConfig

class Data_validation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def check_data_validation(self) ->bool:
        validation_status=None
        df=pd.read_csv("artifacts/data_ingestion/data/part_names.csv")
        ref_columns=list(df.columns)
        all_schema=self.config.all_schema.keys()

        try:
            for i in ref_columns:
                if i not in all_schema:
                    validation_status=False
                    logger.info(f"feature {i} does not exist")
                    with open(self.config.status_file, "w") as stat:
                        stat.write(f"Validation Status: {validation_status}")
                
                else:
                    validation_status=True
                    logger.info(f"feature {i} matched")
                    with open(self.config.status_file, "w") as stat:
                        stat.write(f"Validation Status: {validation_status}")


        except Exception as e:
            raise e