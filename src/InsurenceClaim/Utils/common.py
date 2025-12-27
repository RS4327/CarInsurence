from pathlib import Path
import os
import yaml
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from InsurenceClaim import logger


# ++++++++++++++++++++ Fixed YAML READER +++++++++++++++++++++++++++++++++++
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r", encoding='utf-8-sig') as yaml_file:
            content = yaml.safe_load(yaml_file)
        if not isinstance(content, dict):
            raise ValueError(f"YAML must contain a dictionary, got {type(content)}")
        logger.info(f"YAML load successfully : {path_to_yaml}")
        return ConfigBox(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file does not exist → {path_to_yaml}")
    except BoxValueError:
        raise ValueError("YAML content invalid for Box conversion")
    except Exception as e:
        raise e


# ++++++++++++++++++++ Directory Creation ++++++++++++++++++++++++++++++
def create_directories(paths: list, verbose=True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory Created: {path}")


# ++++++++++++++++++++ File Utilities ++++++++++++++++++++++++++++++
def get_size(path: Path) -> str:
    size_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_kb} KB"


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return joblib.load(file_obj)
    except Exception as e:
        raise e
