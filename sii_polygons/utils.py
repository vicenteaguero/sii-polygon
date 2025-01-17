# sii_polygons/utils.py

import os

from sii_polygons.params import PATHS

def get_bbox(xmin: float, xmax: float, ymin: float, ymax: float) -> str:
    return f'{xmin},{ymin},{xmax},{ymax}'

def get_coords(bbox: str) -> tuple[float, float, float, float]:
    return tuple(map(float, bbox.split(',')))

def get_save_map_folder(comuna_id: int, xmin: float) -> str:
    xmin_folder = int(xmin)//100
    return os.path.join(PATHS['predios'], f'{comuna_id}', f'{xmin_folder}')
