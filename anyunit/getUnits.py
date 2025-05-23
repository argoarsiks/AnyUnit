from .units import *


def getAllUnits() -> dict:
    return {
        "LENGTH": list(LENGTH.keys()),
        "WEIGHT": list(WEIGHT.keys()),
        "AREA": list(AREA.keys()),
        "VOLUME": list(VOLUME.keys())
    }