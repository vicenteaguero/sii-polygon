# sii_polygons/requests.py

from tqdm import tqdm
import numpy as np
import cv2

import requests
import os

from sii_polygons.utils import get_bbox, get_save_map_folder
from sii_polygons.params import API_URLS, MAPS_PAYLOAD, SERVICES_PAYLOAD, BASE_SIZE
from sii_polygons.comunas import get_grid, check_comuna

def get_map(
    comuna: str,
    service: dict,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    size: int = BASE_SIZE,
) -> None:
    service_name, service = list(service.items())[0]
    payload = MAPS_PAYLOAD.copy()
    payload['layers'] = service['layer']
    payload['styles'] = service['style']
    payload['comuna'] = service['comuna']
    payload['bbox'] = get_bbox(xmin, xmax, ymin, ymax)
    payload['width'] = size
    payload['height'] = size
    save_folder = get_save_map_folder(
        comuna=comuna, service=service_name,
        size=size, xmin=xmin
    )
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
    service: dict,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    size: int = BASE_SIZE,
    download: bool = True,
) -> None:
    bbox = get_bbox(xmin, xmax, ymin, ymax)
    save_folder = get_save_map_folder(
        comuna=comuna, service=list(service.keys())[0],
        size=size, xmin=xmin
    )
    save_path = os.path.join(save_folder, bbox+'.png')
    if not os.path.exists(save_path):
        if not download:
            raise FileNotFoundError(f'Map not found with download=False: {save_path}')
        success = get_map(
            comuna=comuna, service=service,
            xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, size=size,
        )
        if not success:
            raise FileNotFoundError(f'Map not found (success={success}): {save_path}')
    img = cv2.imread(save_path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def load_maps_from_comuna(
    comuna: str,
    service: str,
    factor: int = 8,
    size: int = BASE_SIZE,
    buffer: int = 500,
    download: bool = True,
) -> None:
    services = get_services(comuna)
    if service not in services:
        raise ValueError(f'Service not found: {service}')
    service_data = {service: services[service]}
    grid = get_grid(comuna, factor=factor, buffer=buffer)
    maps = dict()
    for _, row in tqdm(grid.iterrows(), total=grid.shape[0]):
        xmin, ymin, xmax, ymax = row.geometry.bounds
        bbox = get_bbox(xmin, xmax, ymin, ymax)
        maps[bbox] = load_map(
            comuna=comuna, service=service_data,
            xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax,
            size=size*factor, download=download,
        )
    return maps

def get_services(comuna: str) -> dict:
    comuna = check_comuna(comuna)
    services_comuna = list()
    for sii_id in comuna['sii_id'].values[0]:
        payload = SERVICES_PAYLOAD.copy()
        payload['data']['comuna'] = str(sii_id)
        r = requests.post(API_URLS['services'], json=payload)
        r.raise_for_status()
        services_data = r.json()['data']
        services = dict()
        for service in services_data:
            key = service['nombreServicio'].lower().replace(' ', '_')
            for letter, replacement in zip('áéíóú', 'aeiou'):
                key = key.replace(letter, replacement)
            services[key] = service
        services_comuna.append(services)
    if len(services_comuna) == 1:
        return services_comuna[0]
    return services_comuna
