import os 
import sys 
from InsurenceClaim.Config.ConfigurationManagerConfig import ConfigurationManagerConfig
from InsurenceClaim.Components.DataPreProcessing import DataPreProcessing
from InsurenceClaim import logger

Stage_Name="Data Pre Validation"
class DataPreProcessingPipeline:
    def __init__(self):
        pass
    def main(self,df):
        try:
            config=ConfigurationManagerConfig()
            data_preprocess_config=config.get_data_preprocessing()
            data_preprocess_val=DataPreProcessing(config=data_preprocess_config)
            data_validation=data_preprocess_val.DataPreValidation(df)
            data_duplicate=data_preprocess_val.DataDuplicateVal(data_validation)
            data_encoding=data_preprocess_val.DataEncodingCategoricalVar(data_duplicate)
            x_train,x_test,y_train,y_test=data_preprocess_val.data_train_test_split(data_encoding)
            logger.info(f"x Trains Shape : {x_train.shape}")
            logger.info(f"x Test Shape : {x_test.shape}")
            logger.info(f"y Trains Shape : {y_train.shape}")
            logger.info(f"y Test Shape : {y_test.shape}")
            return x_train,x_test,y_train,y_test
        except Exception as e:
            raise e

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataPreProcessingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

