from .units import LENGTH, WEIGHT, AREA


def getAllUnits() -> dict:
    return {
        "LENGTH": list(LENGTH.keys()),
        "WEIGHT": list(WEIGHT.keys()),
        "AREA": list(AREA.keys())
    }