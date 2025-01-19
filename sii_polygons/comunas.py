# sii_polygons/comunas.py

import geopandas as gpd

from sii_polygons.params import PATHS

def get_comunas() -> gpd.GeoDataFrame:
    comunas = gpd.read_parquet(PATHS['comunas'])
    return comunas