from dataclasses import dataclass
from pathlib import Path
from src.Detailed_MLFLow_project.constants import *

@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      source_URL: str
      local_data_file: Path
      unzip_data: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class Data_Transformation_Config:
    root_dir: Path
    data_transformation_input: Path