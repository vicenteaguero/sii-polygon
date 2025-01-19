# sii_polygons/params.py

import os

################################################################################

# Constants

API_URLS = {
    'maps': 'https://www4.sii.cl/mapasui/services/ui/wmsProxyService/call',
    'services': 'https://www4.sii.cl/mapasui/services/data/mapasFacadeService/listServiciosComunas',
}

BASE_OFFSET = 76.437028285
BASE_SIZE = 256*2

GRAY_THRESHOLD = 230

MAPS_PAYLOAD = {
    'service': 'WMS',
    'request': 'GetMap',
    'layers': 'sii:BR_CART_{comuna}_WMS',
    'styles': 'PREDIOS_WMS_V0',
    'format': 'image/png',
    'transparent': 'true',
    'version': '1.1.1',
    'comuna': 'None',
    'eac': '0',
    'eacano': '0',
    'srs': 'EPSG:3857',
}

SERVICES_PAYLOAD = {
    'data': {'comuna': '{comuna}'},
    'metaData': {
        'namespace': (
            'cl.sii.sdi.lob.bbrr.mapas.data.api.interfaces.MapasFacadeService'
            '/listServiciosComunas'
        ),
        'conversationId': 'UNAUTHENTICATED-CALL45.71.44.84',
        'transactionId': '6d2ab282-4759-d322-4882-6fbaf8bb3454'
    },
}

################################################################################

# Folders

DATA_FOLDER = 'data'
SRC_FOLDER = 'sii_polygons'

PREDIOS_DATA_FOLDER = 'predios'

################################################################################

# Paths

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATHS = {
    'root': ROOT_PATH,
    'data': os.path.join(ROOT_PATH, DATA_FOLDER),
}

PATHS['predios'] = os.path.join(PATHS['data'], PREDIOS_DATA_FOLDER)
PATHS['comunas'] = os.path.join(PATHS['data'], 'comunas.parquet')
