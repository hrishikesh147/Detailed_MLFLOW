from dataclasses import dataclass
from pathlib import Path
from src.Detailed_MLFLow_project.constants import *

@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      source_URL: str
      local_data_file: Path
      unzip_data: Path
