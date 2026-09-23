from rules import MinimumAreaRule, AllowedZoneRule, NoHazardOverlapRule
from spatial import Parcel, HazardZone
from assessment import ParcelAssessment
from shapely.geometry import box

parcel = Parcel(
    "P-001",
    box(0, 0, 80, 80),
    "Residential",
    7200
)

hazard_zone = HazardZone(
    "HZ-01",
    box(90, 85, 110, 100),
    "Flood",
    "High"
)

assessment = ParcelAssessment( 
    parcel=parcel, 
    rules=[ 
        MinimumAreaRule(5000),
        AllowedZoneRule({"Residential", "Commercial"}),
        NoHazardOverlapRule(hazard_zone), 
    ], 
)

assessment.evaluate()
if assessment.passed():
    print(f"Parcel {parcel.parcel_id} passed.")
else:
    print(f"Parcel {parcel.parcel_id} failed.")