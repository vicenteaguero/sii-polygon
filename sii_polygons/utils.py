# sii_polygons/utils.py

import os

from sii_polygons.params import PATHS

def get_bbox(xmin: float, xmax: float, ymin: float, ymax: float) -> str:
    return f'{xmin},{ymin},{xmax},{ymax}'

def get_coords(bbox: str) -> tuple[float, float, float, float]:
    return tuple(map(float, bbox.split(',')))

def get_save_map_folder(comuna: str, size: int, xmin: float) -> str:
    size_folder = f'{size}x{size}'
    xmin_folder = int(xmin)//100
    return os.path.join(PATHS['predios'], comuna.upper(), size_folder, f'{xmin_folder}')
