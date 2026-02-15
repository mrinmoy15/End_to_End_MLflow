from ml_project import logger
from ml_project.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from ml_project.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from ml_project.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from ml_project.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    
    logger.info(f"******************** Stage {STAGE_NAME} started ********************")   
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"******************** Stage {STAGE_NAME} completed ********************")

except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"******************** Stage {STAGE_NAME} started ********************")   
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"******************** Stage {STAGE_NAME} completed ********************")

except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"******************** Stage {STAGE_NAME} started ********************")   
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f"******************** Stage {STAGE_NAME} completed ********************")

except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f"******************** Stage {STAGE_NAME} started ********************")   
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.main()
    logger.info(f"******************** Stage {STAGE_NAME} completed ********************")
except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME = "Model evaluation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




