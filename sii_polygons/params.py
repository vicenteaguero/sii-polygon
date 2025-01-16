# sii_polygons/params.py

API_URLS = {
    'maps': 'https://www4.sii.cl/mapasui/services/ui/wmsProxyService/call'
}

BASE_OFFSET = 76.437028285
BASE_SIZE = 256

MAPS_PAYLOAD = {
    'service': 'WMS',
    'request': 'GetMap',
    'layers': 'sii:BR_CART_{comuna}_WMS',
    'styles': 'PREDIOS_WMS_V0',
    'format': 'image/png',
    'transparent': 'true',
    'version': '1.1.1',
    'comuna': '{comuna_id}',
    'eac': '0',
    'eacano': '0',
    'srs': 'EPSG:3857',
}
