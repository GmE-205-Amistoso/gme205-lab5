from src.rules import MinimumAreaRule, AllowedZoneRule
from src.spatial import Parcel
from shapely.geometry import box

TEST_MIN_AREA = 5000
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

print("Testing Minimum Area rule...", end=" ")
mar = MinimumAreaRule(TEST_MIN_AREA)
expected_passed = True
eval = mar.evaluate(p)
if eval.passed == expected_passed:
    print("Pass")
else:
    print("Fail")