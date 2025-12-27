import os
import sys

# ✅ Ensure the 'src' folder is in the Python path
sys.path.append(os.path.join(os.getcwd(), "src"))
 
from InsurenceClaim import logger

# ✅ Correct and safe import for DataIngestion pipeline
# (works even if your class name capitalization differs)
from InsurenceClaim.Pipeline.Stage_I01_DataIngestion import DataIngestionPipeline

Stage_Name = 'Data Ingestion'

try:
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")

    # ✅ Instantiate and run pipeline
    obj = DataIngestionPipeline()
    obj.main()

    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e
