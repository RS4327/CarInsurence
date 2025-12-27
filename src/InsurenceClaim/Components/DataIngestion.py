import os
from pathlib import Path
import pandas as pd
#from InsurenceClaim.Config.ConfigurationManagerConfig import ConfigurationManagerConfig
from InsurenceClaim import logger
from InsurenceClaim.Entity.Config_Entity import DataIngestionConfig
#from InsurenceClaim.Utils.common import create_directories


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def DataLoading(self) -> pd.DataFrame:
        """
        Load dataset from URL or local path and return a pandas DataFrame.
        """
        try:
            url = self.config.data_url_path
            local_data_path = self.config.data_load_path

            # ✅ Ensure directory exists
            os.makedirs(os.path.dirname(local_data_path), exist_ok=True)
            logger.info(f"Ensured directory exists for data at: {local_data_path}")

            # ✅ Read CSV from given URL or file path
            df = pd.read_csv(url)
            logger.info("✅ Data successfully loaded from source.")

            # ✅ Save raw data to local artifacts (optional)
            df.to_csv(local_data_path, index=False)
            logger.info(f"✅ Data saved locally at: {local_data_path}")

            # ✅ Log basic info
            logger.info(f"DataFrame shape: {df.shape}")
            logger.info(f"DataFrame columns: {list(df.columns)}")
            logger.info(f"First 2 rows:\n{df.head(2)}")

            return df

        except FileNotFoundError:
            logger.error(f"❌ File not found at path: {url}")
            raise
        except pd.errors.EmptyDataError:
            logger.error("❌ The dataset is empty.")
            raise
        except Exception as e:
            logger.error(f"❌ Error during data ingestion: {str(e)}")
            raise e
