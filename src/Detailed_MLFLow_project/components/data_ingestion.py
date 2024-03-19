import os
import urllib.request as request
from src import logger
import zipfile
from src.Detailed_MLFLow_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"file : {filename} downloaded")
        else:
            filename=self.config.local_data_file
            logger.info(f"file : {filename} already exists")

    def extract_zip_file(self):
        try:
            unzip_path=self.config.unzip_data
            
            with zipfile.ZipFile(self.config.local_data_file,'r') as zip_d:
                zip_d.extractall(unzip_path)
            logger.info("file unzipped successfully")
        except Exception as e:
            raise e