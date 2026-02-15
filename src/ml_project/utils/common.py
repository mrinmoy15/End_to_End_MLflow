from omegaconf import OmegaConf
from typing import Dict, Any
from ensure import ensure_annotations
import os
from pathlib import Path
from ml_project import logger
from box import ConfigBox
import json


@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Read a YANL file using OmegaConf and return its contents as a dictionary.
    
    params:
    path_to_yaml (str): Path to the YANL file

    returns: A dictionary containing the contents of the YANL file.
    """

    try:
        yaml_content = OmegaConf.load(path_to_yaml)
        return ConfigBox(OmegaConf.to_container(yaml_content, resolve=True))
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories if they do not exist.

    params:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool, optional): If True, logs output. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")