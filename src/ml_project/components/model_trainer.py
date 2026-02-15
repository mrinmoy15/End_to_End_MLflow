import pandas as pd
import os
from ml_project import logger
from sklearn.linear_model import ElasticNet
import joblib
from ml_project.entity.config_entity import ModelTrainerConfig

class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]]

        X_test = test_data.drop(self.config.target_column, axis=1)
        y_test = test_data[[self.config.target_column]]

        model = ElasticNet(
            alpha = self.config.alpha, 
            l1_ratio = self.config.l1_ratio,
            random_state=42
        )
        model.fit(X_train, y_train)

        os.makedirs(self.config.root_dir, exist_ok=True)
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model, model_path)
