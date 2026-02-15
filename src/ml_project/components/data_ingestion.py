import shutil
import os
from ml_project import logger
from ml_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def copy_datafile_to_artifacts(self):
        filename = os.path.basename(self.config.source_path)
        dest_file_path = os.path.join(self.config.root_dir, filename)
        
        # Check if file already exists
        if not os.path.exists(dest_file_path):
            shutil.copy(self.config.source_path, self.config.root_dir)
            logger.info(f"{filename} is copied successfully to artifacts.")
        else:
            logger.info(f"{filename} already exists in artifacts. Skipping copy.")