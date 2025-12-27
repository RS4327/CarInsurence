from pathlib import Path
import os 
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project_name="InsurenceClaim"

list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/Config/__init__.py",
    f"src/{project_name}/Constant/__init__.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Pipeline/__init__.py",
    f"src/{project_name}/Entity/__init__.py",
    f"src/{project_name}/Utils/__init__.py",
    f"src/{project_name}/__init__.py",
    "Config/Config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    f"Template/index.html",
    f"Template/home.html",
    f"requirment.txt",
    f"stepup.py"
]
for filepath in list_of_files:
      filepath=Path(filepath)
      filedir,filename=os.path.split(filepath)
      if filedir!="":
            os.makedirs(filedir,exist_ok=True)
      if (not  os.path.exists(filepath) or os.path.getsize==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating the Empty File : {filepath}")
      else:
            logging.info(f"{filename} is already exists")