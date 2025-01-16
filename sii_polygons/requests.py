# sii_polygons/requests.py


from sii_polygons.params import BASE_OFFSET, BASE_SIZE

def get_map(
    city: str,
    city_id: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    offset: int = BASE_OFFSET,
    size: int = BASE_SIZE,
) -> None:
    pass

def load_map(
    city_id: int,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    offset: int = BASE_OFFSET,
    size: int = BASE_SIZE,
    download: bool = True,
) -> None:
    pass

def get_maps():
    pass

def load_maps():
    pass
