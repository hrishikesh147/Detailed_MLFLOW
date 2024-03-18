from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import yaml
from src import logger
import os,sys
import json


# @ensure_annotations
# def read_yaml(yaml_path:Path)-> ConfigBox:
#     try:
#         with open(yaml_path) as f:
#             f=yaml.safe_load(f)
#             logger.info(f"Yaml file {f} loaded successfully")
#             return ConfigBox(f)
#     except Exception as e:
#         raise e
    

# @ensure_annotations
# def create_directories(path_to_dir:Path):
#     try:
#         os.makedirs(path_to_dir,exist_ok=True)
#         logger.info(f"Directory created as path {path_to_dir}")
#     except Exception as e:
#         raise e

@ensure_annotations
def read_yaml(filepath:Path) -> ConfigBox:
    try:
        with open(filepath) as y:
            content=yaml.safe_load(y)
            logger.info(f"yaml file {content} loaded successfully")
            return ConfigBox(content)
        
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(filep:list, verbose=True):
    for i in filep:
        os.makedirs(i,exist_ok=True)
        if verbose:
            logger.info(f"created directory at path {i}")    

@ensure_annotations
def save_json(json_path:Path,data):
    with open(json_path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"{data} saved at path {json_path} Succcessfully")
    
@ensure_annotations
def load_json(json_p:Path)->ConfigBox:
    with open(json_p) as f:
        con=json.load(f)
        return ConfigBox(con)
    logger.info(f"Json file from path {json_p}  opened Succcessfully")  
        
