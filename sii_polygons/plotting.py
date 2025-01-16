# sii_polygons/plotting.py

from matplotlib import pyplot as plt
import geopandas as gpd
import numpy as np

def plot_map(
    map: np.ndarray,
) -> None:
    plt.imshow(map)
    plt.show()

def plot_pipeline(
    map: np.ndarray,
    label_map: np.ndarray,
    gdf: gpd.GeoDataFrame,
) -> None:
    pass
