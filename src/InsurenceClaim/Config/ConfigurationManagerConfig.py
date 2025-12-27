import os
from pathlib import Path
from InsurenceClaim import logger

from InsurenceClaim.Entity.Config_Entity import *
from InsurenceClaim.Utils.common import *
from InsurenceClaim.Constant import *


class ConfigurationManagerConfig:
    def __init__(self,
                 config_path=CONFIG_YAML_PATH,
                 params_path= PARAMS_YAML_PATH
                 ):
        self.config=read_yaml(Path(config_path))
        self.params=read_yaml(Path(params_path))

        create_directories([self.config.artifacts_root])
    def get_data_ingestion(self) ->DataIngestionConfig:
        config=self.config.data_ingestion
        data_ingetion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            data_url_path=config.data_url_path,
            data_load_path=config.data_load_path
        )
        return data_ingetion_config
