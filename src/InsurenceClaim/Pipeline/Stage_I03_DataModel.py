import os
import sys 
from InsurenceClaim.Config.ConfigurationManagerConfig import ConfigurationManagerConfig
from InsurenceClaim.Components.DataModel import DataModel
from InsurenceClaim import logger

Stage_Name ="Data Model "

class DataModelPipeline:
    def __init__(self):
        pass
    def main(self,x_train,x_test,y_train,y_test):
        config=ConfigurationManagerConfig()
        get_model_config=config.get_data_model()
        data_model=DataModel(config=get_model_config)
        data_model_eve=data_model.DataModel(x_train,x_test,y_train,y_test)


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj=DataModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
