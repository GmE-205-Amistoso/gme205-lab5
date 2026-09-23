# test/test_spatial.py
import pytest
from spatial import Parcel, HazardZone, Road
from shapely.geometry import box, LineString

# -----------------------
# Parcel Tests
# -----------------------

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

# -----------------------
# HazardZone Tests
# -----------------------

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

# -----------------------
# Road Tests
# -----------------------

def test_valid_road_creation_passes():
    r = Road(
        "R-001",
        LineString([(5,5), (50,5)])
    )
    assert r.road_id == "R-001"

def test_invalid_road_creation_raises_exception():
    with pytest.raises((KeyError, TypeError, ValueError)):
        Road(
            None,
            LineString([(5,5), (50,5)])
        )
