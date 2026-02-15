import os
from ml_project.entity.config_entity import DataValidationConfig
import pandas as pd
from ml_project import logger

class DataValiadtion:
    
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool|None:
        try:
            validation_status = None

            data = pd.read_csv(self.config.source_path)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
        
        except Exception as e:
            logger.exception(e)
            raise e
        else:
            return validation_status
