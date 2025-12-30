from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path
    data_url_path: Path
    data_load_path: Path

@dataclass
class DataPreProcessingConfig:
    root_dir: Path
    validation_data_path: Path
    cleaned_data_path: Path
    preprocessing_data_path: Path
    encoded_data_path: Path
    data_test_size: float
    data_random_state: int
    allowed_missing_percentage: float   # ✅ better as float for % values like 5.0
    allowed_outlier_std: float          # ✅ standard deviation threshold (e.g., 3.0)
    encoding_strategy: str              # e.g., 'label', 'onehot', 'ordinal'
    scaling_strategy: str               # e.g., 'standard', 'minmax', 'robust'
    imputation_strategy: str            # e.g., 'mean', 'median', 'mode', or 'drop'
    handling_outlier: bool              # whether to detect & handle outliers
    handling_missing: bool              # whether to handle missing values
    save_intermediate: bool             # save intermediate datasets

