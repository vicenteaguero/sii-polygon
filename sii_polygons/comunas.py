# sii_polygons/comunas.py

from shapely.geometry import box
import geopandas as gpd
import numpy as np

from sii_polygons.params import PATHS, BASE_OFFSET

def get_comunas() -> gpd.GeoDataFrame:
    comunas = gpd.read_parquet(PATHS['comunas'])
    return comunas

def check_comuna(comuna: str | int) -> str:
    comunas = get_comunas()
    if isinstance(comuna, int):
        comuna = comunas.loc[comuna, 'comuna']
    elif isinstance(comuna, str):
        comuna = comuna.upper()
    else:
        raise ValueError(f'Invalid comuna: {comuna} (comuna must be int or str)')
    if comuna not in comunas['comuna'].values:
        raise ValueError(f'Comuna not found: {comuna}')
    return comunas[comunas['comuna'] == comuna]

def get_grid(comuna: str | int, factor: int = 16, buffer: int = 500) -> gpd.GeoDataFrame:
    gdf = check_comuna(comuna)
    offset = BASE_OFFSET*factor
    gdf.loc[:, 'geometry'] = gdf.geometry.buffer(buffer)
    xmin, ymin, xmax, ymax = gdf.total_bounds
    x_coords = np.arange(xmin, xmax, offset)
    y_coords = np.arange(ymin, ymax, offset)
    grid = list()
    for x in x_coords:
        for y in y_coords:
            grid.append(box(x, y, x+offset, y+offset))
    grid = gpd.GeoDataFrame(geometry=grid, crs=gdf.crs)
    return grid[grid.intersects(gdf.unary_union)]
