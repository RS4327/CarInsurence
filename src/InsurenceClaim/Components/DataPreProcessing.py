from pathlib import Path
import os
import pandas as pd
import numpy as np
from InsurenceClaim.Entity.Config_Entity import DataPreProcessingConfig
from InsurenceClaim import logger
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

class DataPreProcessing:
    def __init__(self, config: DataPreProcessingConfig):
        self.config = config

    def DataPreValidation(self, df: pd.DataFrame) -> pd.DataFrame:
        #logger.info(f"{df.info()}")
        """
        Perform data validation and missing value handling.
        """
        try:
            #  Save input DataFrame for traceability
            os.makedirs(os.path.dirname(self.config.validation_data_path), exist_ok=True)
            df.to_csv(self.config.validation_data_path, index=False)
            logger.info(f" Data Frame Columns : {df.columns}")
            logger.info(f"Data frame saved to {self.config.validation_data_path}")

           
            #  Handle missing values if enabled
            allowed_missing = self.config.allowed_missing_percentage
            
            if self.config.handling_missing:
                logger.info("============== Checking Missing Values ==============")
                df = self._check_missing_values(df, allowed_missing)

            logger.info(" Data Pre Validation completed successfully.")
            return df

        except Exception as e:
            logger.exception(f" Error during DataPreValidation: {e}")
            raise e

    # ============================================
    #  Internal helper for missing values
    # ============================================
    def _check_missing_values(self, df: pd.DataFrame, allowed_missing: float) -> pd.DataFrame:

        """
        Check missing values, drop or impute columns exceeding allowed threshold.
        """
        missing_percentage = (df.isnull().sum() / len(df)) * 100
        logger.info("Checking missing value percentage per column:")

        for col, pct in missing_percentage.items():
            logger.info(f" - {col}: {pct:.2f}% missing")

        exceed_cols = missing_percentage[missing_percentage > allowed_missing].index.tolist()
        if exceed_cols:
            logger.warning(f" Columns exceeding {allowed_missing}% missing values: {exceed_cols}")

            for col in exceed_cols:
                dtype = df[col].dtype
                logger.info(f"Handling column '{col}' of type {dtype}")

                #  Handle numeric columns safely
                if np.issubdtype(dtype, np.number):
                    if self.config.imputation_strategy.lower() == "mean":
                        df[col]=df[col].fillna(df[col].mean(), inplace=True)
                    elif self.config.imputation_strategy.lower() == "median":
                        df[col]=df[col].fillna(df[col].median(), inplace=True)
                    elif self.config.imputation_strategy.lower() == "mode":
                        df[col]=df[col].fillna(df[col].mode()[0], inplace=True)
                    else:
                        df.drop(columns=[col], inplace=True)
                        logger.info(f"Dropped numeric column '{col}'")

                #  Handle categorical (object/string) columns safely
                else:
                    if self.config.imputation_strategy.lower() in ["mode", "most_frequent"]:
                        df[col]=df[col].fillna(df[col].mode()[0], inplace=True)
                    else:
                        df.drop(columns=[col], inplace=True)
                        logger.info(f"Dropped non-numeric column '{col}'")

            logger.info(f"Missing value handling completed using {self.config.imputation_strategy} strategy.")
        else:
            logger.info(" No columns exceed missing value threshold.")

        #Drop columns not useful for predictions
        drop_cols=['policy_number','incident_location','incident_date','auto_make','auto_model','policy_bind_date']
        logger.info(f'Dropped the not useful for predictions : {drop_cols}')
        df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)
        return df
    
    def DataDuplicateVal(self,df:pd.DataFrame):
        logger.info(f'************ Checking Duplicate Values ****************')
        logger.info(f'Cheking Shape of the Data Frame before Handling the Duplciate values {df.shape}')
        if df.duplicated().sum() > 0:
            logger.warning(f"Found {df.duplicated().sum()} duplicate rows. Removing them...")
            df = df.drop_duplicates()
            logger.info("Duplicate rows removed successfully.")
        else:
            logger.info(" No duplicate rows found.")

        logger.info(f'Cheking Shape of the Data Frame after Handling the Duplciate values {df.shape}')
        os.makedirs(os.path.dirname(self.config.cleaned_data_path), exist_ok=True)
        df.to_csv(self.config.cleaned_data_path, index=False)
        #df.to_csv(self.config.cleaned_data_path)
        return df
    def DataEncodingCategoricalVar(self, df: pd.DataFrame):
        
        # Step 1: Ensure DataFrame
        if not isinstance(df, pd.DataFrame):
            df = pd.DataFrame(df)
            logger.warning("Input was not a DataFrame — converted to pandas DataFrame.")

        # Step 2: Encode categorical columns
        cat_cols = df.select_dtypes(include='object').columns
        le = LabelEncoder()

        for col in cat_cols:
            try:
                df[col] = le.fit_transform(df[col].astype(str))
            except Exception as e:
                logger.error(f"Encoding failed for column {col}: {e}")

        # Step 3: Logging
        logger.info("Categorical Encoding Done")
        logger.info(f"Data sample after encoding:\n{df.head(1)}")

        # Step 4: Return encoded DataFrame
        os.makedirs(os.path.dirname(self.config.encoded_data_path), exist_ok=True)
        df.to_csv(self.config.encoded_data_path)
        return df
    
    def data_train_test_split(self,df:pd.DataFrame):
        logger.info(f"================ Data Train Test Split ================")
        x=df.drop('fraud_reported',axis=1)
        y=df['fraud_reported'].apply(lambda x: 1 if x in ['Y','y',1,'YES','yes'] else 0 )
        logger.info(f" x shape :{x.shape}")
        logger.info(f" y shape :{y.shape}")
        x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.2,random_state=self.config.data_random_state,stratify=y)
        logger.info(" Train/Test split done")
        logger.info('================ Feature Scalling ================ ')
        sclar=StandardScaler()
        x_train_scaller=sclar.fit_transform(x_train)
        x_test_scaller=sclar.transform(x_test)
        os.makedirs(os.path.dirname(self.config.preprocessing_data_path), exist_ok=True)
        with open(self.config.preprocessing_data_path, 'wb') as f:
            pickle.dump(sclar, f)
        return x_train_scaller,x_test_scaller,y_train,y_test



         


    



