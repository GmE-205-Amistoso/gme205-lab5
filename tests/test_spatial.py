from src.spatial import Parcel, HazardZone
from shapely.geometry import box

# ----------------------------
# spatial.Parcel tests
# ----------------------------
test_parcel = {
    "name": "P-001",
    "geometry": box(0, 0, 80, 80),
    "zone": "Residential",
    "area_sqm": 7200
}

p = Parcel(
    test_parcel["name"],
    test_parcel["geometry"],
    test_parcel["zone"],
    test_parcel["area_sqm"]
)

print("Testing Parcel object creation...", end=" ")
expected_parcel_id = "P-001"
if(p.parcel_id) == expected_parcel_id:
    print("Pass")
else:
    print("Fail")

print("Testing Invalid Parcel object creation...", end=" ")
test_invalid_parcel = {
    "name": "IP-001",
    "geometry": box(0, 0, 80, 0),
    "zone": "Invalid",
    "area_sqm": 5000
}
try:
    p = Parcel(
        test_invalid_parcel["name"],
        test_invalid_parcel["geometry"],
        test_invalid_parcel["zone"],
        test_invalid_parcel["area_sqm"]
    )
    print("Fail. Created Parcel object with invalid parameter.")
except (KeyError, TypeError, ValueError) as exc:
    print(f"Pass. Correctly captured error: {exc}")

# ----------------------------
# spatial.HazardZone tests
# ----------------------------
test_hazard = {
    "zone_id": "HZ-01", 
    "geometry": box(60, 50, 110, 100), 
    "hazard_type": "Flood", 
    "severity": "High",
}

hz = HazardZone(
    test_hazard["zone_id"],
    test_hazard["geometry"],
    test_hazard["hazard_type"],
    test_hazard["severity"]
)
print("Testing HazardZone object creation...", end=" ")
expected_hazard_id = "HZ-01"
if(hz.zone_id) == expected_hazard_id:
    print("Pass")
else:
    print("Fail")

print("Testing Invalid HazardZone object creation...", end=" ")
test_invalid_hazard = {
    "zone_id": "IHZ-0001", 
    "geometry": box(0, 00, 110, 100), 
    "hazard_type": "Invalid", 
    "severity": None,
}
try:
    invalid_hz = HazardZone(
        test_invalid_hazard["zone_id"],
        test_invalid_hazard["geometry"],
        test_invalid_hazard["hazard_type"],
        test_invalid_hazard["severity"]
    )
    print("Fail. Created HazardZone object with invalid parameter.")
except (KeyError, TypeError, ValueError) as exc:
    print(f"Pass. Correctly captured error: {exc}")

print("Testing Parcel intersects method...", end=" ")
if p.intersects(hz):
    print("Pass")
else:
    print("Fail")
    