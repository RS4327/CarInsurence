import os
import sys

#  Ensure the 'src' folder is in the Python path
sys.path.append(os.path.join(os.getcwd(), "src"))
 
from InsurenceClaim import logger

#  Correct and safe import for DataIngestion pipeline
# (works even if your class name capitalization differs)
from InsurenceClaim.Pipeline.Stage_I01_DataIngestion import DataIngestionPipeline
from InsurenceClaim.Pipeline.Stage_I02_DataPreProcessing import DataPreProcessingPipeline
Stage_Name = 'Data Ingestion'

try:
    logger.info(f"============================ *** ==========================================")
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")

    # Instantiate and run pipeline
    obj = DataIngestionPipeline()
    df=obj.main()
    logger.info(f'Data Frame Shape {df.shape}')

    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    logger.info(f"---------------------------- *** ------------------------------------------")

except Exception as e:
    logger.exception(e)
    raise e

Stage_Name="Data Pre Validation"
try:
    logger.info(f"============================ *** ==========================================")
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Started <<<<<<<<<<")
    obj=DataPreProcessingPipeline()
    x_train_scaller,x_test_scaller,y_train,y_test=obj.main(df)
    #logger.info(f'Data Frame Shape {df.shape}')
    logger.info(f">>>>>>>>>> Stage : {Stage_Name} Completed Successfully <<<<<<<<<<")
    logger.info(f"---------------------------- *** ------------------------------------------")
except Exception as e:
    logger.exception(e)
    raise e