from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_transformation import DataTransformation
from ml_project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    
    def __init__(self):
        pass

    def main(self):
        
        with open(Path("artifacts/data_validation/status.txt"), "r") as f:
            status = f.read().split(" ")[-1]

        if status == "True":
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()

        else:
            logger.info("Data Validation failed. Data Schema not valid. Data Transformation cannot be performed.")
            raise Exception("Data Validation failed. ata Schema not valid. Data Transformation cannot be performed.")
        
if __name__ == "__main__":
    try:
        logger.info(f"******************** Stage {STAGE_NAME} started ********************")   
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.main()
        logger.info(f"******************** Stage {STAGE_NAME} completed ********************")
    except Exception as e: 
        logger.exception(e)
        raise e