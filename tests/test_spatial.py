# test/test_spatial.py
import pytest
from spatial import Parcel, HazardZone
from shapely.geometry import box


def test_parcel_object_creation_passes():
    p = Parcel(
        "P-001",
        box(0, 0, 80, 80),
        "Residential",
        7200
    )
    assert isinstance(p, Parcel)


def test_invalid_parcel_creation_raises_exception():
    with pytest.raises((KeyError, TypeError, ValueError)):
        Parcel(
            "IP-001",
            box(0, 0, 80, 0),
            "Invalid",
            5000
        )


def test_hazard_zone_creation_passes():
    hz = HazardZone(
        "HZ-01",
        box(60, 50, 110, 100),
        "Flood",
        "High"
    )
    assert isinstance(hz, HazardZone)


def test_invalid_hazard_zone_creation_raises_exception():
    with pytest.raises((KeyError, TypeError, ValueError)):
        HazardZone(
            "IHZ-0001",
            box(0, 0, 110, 100),
            "Invalid", 
            None
        )


