# sii_polygons/requests.py

import cv2

import requests
import os

from sii_polygons.params import API_URLS, MAPS_PAYLOAD, BASE_OFFSET, BASE_SIZE
from sii_polygons.utils import get_bbox, get_save_map_folder

def get_map(
    comuna: str,
    comuna_id: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    size: int = BASE_SIZE,
) -> None:

    payload = MAPS_PAYLOAD
    payload['layers'] = payload['layers'].format(comuna=comuna.upper())
    payload['comuna'] = comuna_id
    payload['bbox'] = get_bbox(xmin, xmax, ymin, ymax)
    payload['width'] = size
    payload['height'] = size

    save_folder = get_save_map_folder(comuna_id, xmin)
    save_path = os.path.join(save_folder, payload['bbox']+'.png')

    try:
        r = requests.get(API_URLS['maps'], params=payload)
        r.raise_for_status()
        os.makedirs(save_folder, exist_ok=True)
        with open(save_path, 'wb') as f:
            f.write(r.content)
        return True
    except requests.exceptions.RequestException:
        return False

def load_map(
    comuna: str,
    comuna_id: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    offset: int = BASE_OFFSET,
    size: int = BASE_SIZE,
    download: bool = True,
) -> None:
    bbox = get_bbox(xmin, xmax, ymin, ymax)
    save_folder = get_save_map_folder(comuna_id, xmin)
    save_path = os.path.join(save_folder, bbox+'.png')
    if not os.path.exists(save_path):
        if not download:
            raise FileNotFoundError(f'Map not found with download=False: {save_path}')
        success = get_map(
            comuna=comuna, comuna_id=comuna_id,
            xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, size=size,
        )
        if not success:
            raise FileNotFoundError(f'Map not found: {save_path}')
    return cv2.cvtColor(cv2.imread(save_path), cv2.COLOR_BGR2RGB)

def get_maps():
    pass

def load_maps():
    pass
