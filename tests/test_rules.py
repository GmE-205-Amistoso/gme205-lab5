from rules import MinimumAreaRule, AllowedZoneRule, NoHazardOverlapRule
from spatial import Parcel, HazardZone
from shapely.geometry import box

TEST_MIN_AREA = 5000
ALLOWED_ZONES = ["Residential", "Commercial"]

# -----------------------
# MinimumAreaRule Tests
# -----------------------

def test_minimum_area_at_threshold_passes():
    mar = MinimumAreaRule(TEST_MIN_AREA)
    evaluated = mar.evaluate(
        Parcel(
            "P-001",
            box(0, 0, 80, 80),
            "Residential",
            5000
        )
    )
    assert evaluated.passed

def test_minimum_area_below_threshold_fails():
    mar = MinimumAreaRule(TEST_MIN_AREA)
    evaluated = mar.evaluate(
        Parcel(
            "P-002",
            box(0, 0, 80, 80),
            "Residential",
            3000
        )
    )
    assert not evaluated.passed

# -----------------------
# AllowedZoneRule Tests
# -----------------------

def test_allowed_zone_in_list_passes():
    allowed_zones = AllowedZoneRule(ALLOWED_ZONES)
    evaluated = allowed_zones.evaluate(
        Parcel(
            "P-002",
            box(0, 0, 80, 80),
            "Residential",
            3000
        )
    )
    assert evaluated.passed

def test_allowed_zone_rule_not_in_list_fails():
    allowed_zones = AllowedZoneRule(ALLOWED_ZONES)
    evaluated = allowed_zones.evaluate(
        Parcel(
            "P-003",
            box(0, 0, 80, 80),
            "Industrial",
            3000
        )
    )
    assert not evaluated.passed

# -----------------------
# NoHazardOverlapRule Tests
# -----------------------

def test_parcel_not_intersecting_hazard_zone_passes():
    hz = NoHazardOverlapRule(
        HazardZone(
            "HZ-01",
            box(60, 50, 110, 100),
            "Flood",
            "High"
        )
    )
    evaluated = hz.evaluate(
        Parcel(
            "P-001",
            box(115, 120, 280, 280),
            "Residential",
            7200
        )
    )
    assert evaluated.passed

def test_parcel_intersects_hazard_zone_fails():
    hz = NoHazardOverlapRule(
        HazardZone(
            "HZ-01",
            box(60, 50, 110, 100),
            "Flood",
            "High"
        )
    )
    evaluated = hz.evaluate(
        Parcel(
            "P-002",
            box(0, 0, 80, 80),
            "Residential",
            7200
        )
    )
    assert not evaluated.passed