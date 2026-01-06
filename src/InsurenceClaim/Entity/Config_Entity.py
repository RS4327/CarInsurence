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
@dataclass
class LogisticRegressionConfig: 
    solver: str
    max_iter: int
    class_weight: str
    c: int
    random_state: int
@dataclass
class RamdomForestConfig:
    n_estimators: int
    max_depth: int
    class_weight: str
    random_state: int
@dataclass
class DecisionTreeConfig:
    max_depth: int
    class_weight: str
    random_state: int
@dataclass
class KNeighborsConfig:
    n_neighbors: int
@dataclass
class SVMConfig:
    kernal: str
    probability: bool
    class_weight: str
    random_state: int
@dataclass
class GradientBoostingConfig:
    random_state: int
@dataclass
class AdaBoostConfig:
    random_state: int
@dataclass
class XGBoostConfig:
    scale_pos_weight : float
    use_label_encoder: bool
    eval_metric : str
    random_state: int
@dataclass
class LightGBMConfig:
    class_weight: str
    random_state: int
@dataclass
class CatBoostConfig: 
    verbose: int
    random_state: int
    
@dataclass
class DataModelConfig:
    root_dir: Path
    logistic_model_path: Path
    randomforest_model_path: Path
    scaler_path: Path
    Logistic_Regression: LogisticRegressionConfig
    Random_Forest: RamdomForestConfig
    Decision_Tree: DecisionTreeConfig
    KNeighbors: KNeighborsConfig
    SVM: SVMConfig
    Gradient_Boosting: GradientBoostingConfig
    AdaBoost: AdaBoostConfig
    XGBoost: XGBoostConfig
    LightGBM: LightGBMConfig
    CatBoost: CatBoostConfig

    



