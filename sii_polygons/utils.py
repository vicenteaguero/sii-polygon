# sii_polygons/utils.py

import os

from sii_polygons.params import PATHS

def get_bbox(xmin: float, xmax: float, ymin: float, ymax: float) -> str:
    return f'{xmin},{ymin},{xmax},{ymax}'

def get_coords(bbox: str) -> tuple[float, float, float, float]:
    return tuple(map(float, bbox.split(',')))

def get_save_map_folder(comuna: str, service: str, size: int, xmin: float) -> str:
    size_folder = f'{size}x{size}'
    xmin_folder = int(xmin)//100
    if service not in PATHS:
        raise NotImplementedError(f'Service {service} not implemented')
    return os.path.join(PATHS[service], comuna.upper(), size_folder, f'{xmin_folder}')
