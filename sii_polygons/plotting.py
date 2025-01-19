# sii_polygons/plotting.py

from matplotlib import pyplot as plt
import geopandas as gpd
from tqdm import tqdm
import numpy as np

from sii_polygons.comunas import check_comuna
from sii_polygons.utils import get_coords

def plot_map(
    map: np.ndarray,
) -> None:
    plt.imshow(map)
    plt.show()

def plot_grid(
    comuna: str | int,
    maps: dict,
    buffer: int = 500,
) -> None:
    comuna = check_comuna(comuna)
    fig, ax = plt.subplots(1, 1, figsize=(30, 30))
    ax.set_aspect('equal')
    for bbox, map in tqdm(maps.items()):
        xmin, ymin, xmax, ymax = get_coords(bbox)
        ax.imshow(map, extent=[xmin, xmax, ymin, ymax])
    comuna.boundary.plot(ax=ax, color='red')
    ax.set_title(f'Comuna: {comuna["comuna"].values[0]}')
    xmin, ymin, xmax, ymax = comuna.geometry.buffer(buffer).total_bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    fig.tight_layout()
    plt.show()

def plot_pipeline(
    map: np.ndarray,
    label_map: np.ndarray,
    gdf: gpd.GeoDataFrame,
) -> None:
    pass
