import os
import sys
from InsurenceClaim.Config.ConfigurationManagerConfig import ConfigurationManagerConfig
from InsurenceClaim.Components.DataIngestion import DataIngestion
from InsurenceClaim import logger

Stage_Name = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            # ✅ Load configuration
            config = ConfigurationManagerConfig()

            # ✅ Get Data Ingestion config entity
            Data_Ingestion_Config = config.get_data_ingestion()

            # ✅ Initialize Data Ingestion Component
            data_ingestion = DataIngestion(config=Data_Ingestion_Config)

            # ✅ Execute data loading
            df = data_ingestion.DataLoading()

            # ✅ Log success
            logger.info(f"✅ Data Ingestion Completed. Loaded data shape: {df.shape}")

        except Exception as e:
            logger.exception(f"❌ Error in {Stage_Name}: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
