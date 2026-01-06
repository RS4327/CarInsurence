import os
from pathlib import Path
from InsurenceClaim import logger

from InsurenceClaim.Entity.Config_Entity import *
from InsurenceClaim.Utils.common import *
from InsurenceClaim.Constant import *


class ConfigurationManagerConfig:
    def __init__(self,
                 config_path=CONFIG_YAML_PATH,
                 params_path= PARAMS_YAML_PATH
                 ):
        self.config=read_yaml(Path(config_path))
        self.params=read_yaml(Path(params_path))

        create_directories([self.config.artifacts_root])
    def get_data_ingestion(self) ->DataIngestionConfig:
        config=self.config.data_ingestion
        data_ingetion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            data_url_path=config.data_url_path,
            data_load_path=config.data_load_path
        )
        return data_ingetion_config
    def get_data_preprocessing(self)->DataPreProcessingConfig:
        config=self.config.data_preprocessing

        data_preprocessing_config=DataPreProcessingConfig(
            root_dir=config.root_dir,
            validation_data_path=config.validation_data_path,
            cleaned_data_path=config.cleaned_data_path,
            preprocessing_data_path=config.preprocessing_data_path,
            encoded_data_path=config.encoded_data_path,
            data_test_size=config.data_test_size,
            data_random_state=config.data_random_state,
            allowed_missing_percentage=config.allowed_missing_percentage,
            allowed_outlier_std=config.allowed_outlier_std,
            encoding_strategy=config.encoding_strategy,
            scaling_strategy=config.scaling_strategy,
            imputation_strategy=config.imputation_strategy,
            handling_outlier=config.handling_outlier,
            handling_missing=config.handling_missing,
            save_intermediate=config.save_intermediate

        )
        return data_preprocessing_config
    def get_data_model(self)->DataModelConfig:
         config=self.config.data_model
         data_model_config=DataModelConfig(
             root_dir=config.root_dir,
             logistic_model_path=config.logistic_model_path,
             randomforest_model_path=config.randomforest_model_path,
             scaler_path=config.scaler_path,
             Logistic_Regression=config.Logistic_Regression,
             Random_Forest=config.Random_Forest,
             Decision_Tree=config.Decision_Tree,
             KNeighbors=config.KNeighbors,
             SVM=config.SVM,
             Gradient_Boosting=config.Gradient_Boosting,
             AdaBoost=config.AdaBoost,
             XGBoost=config.XGBoost,
             LightGBM=config.LightGBM,
             CatBoost=config.CatBoost

         )
         return data_model_config
