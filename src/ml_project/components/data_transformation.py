import os
from ml_project import logger 
from ml_project.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config


        ## Note: You can add different data transformation techniques such as Scaler, PCA and all
        #You can perform all kinds of EDA in ML cycle here before passing this data to the model

        # I am only adding train_test_spliting cz this data is already cleaned up

    def train_test_split(self):
        
        data = pd.read_csv(self.config.source_path)

        train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(f"Training data size: {train_set.shape}")
        logger.info(f"Test data size: {test_set.shape}")

