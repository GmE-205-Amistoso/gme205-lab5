from rules import MinimumAreaRule, AllowedZoneRule, NoHazardOverlapRule, RoadAccessRule
from spatial import Parcel, HazardZone, Road
from assessment import ParcelAssessment

from shapely.geometry import box, LineString
from dataclasses import asdict
import json

OUTPUT_DIR = "output"

def main():
    parcel_a = Parcel(
        "P-001",
        box(0, 0, 80, 90),
        "Residential",
        7200
    )

    parcel_b = Parcel(
        "P-002",
        box(120, 0, 190, 80),
        "Commercial",
        5600
    )

    hazard = HazardZone(
        "HZ-01",
        box(60, 50, 110, 100),
        "Flood",
        "High"
    )

    road = Road(
        "R-001",
        LineString([(25,15), (50,15)])
    )

    rules = [
        MinimumAreaRule(5000),
        AllowedZoneRule(["Residential", "Commercial"]),
        NoHazardOverlapRule(hazard),
        RoadAccessRule(road, 20)
    ]

    assessment_a = ParcelAssessment(
        parcel_a,
        rules
    )
    evaluate_a = assessment_a.evaluate()

    assessment_b = ParcelAssessment(
        parcel_b,
        rules
    )
    evaluate_b = assessment_b.evaluate()

    summary = {
        "scenario": "parcel-development-assessment",
        "parcels": [
            {
                "parcel_id": parcel_a.parcel_id,
                "passed": assessment_a.passed(),
                "results": [asdict(r) for r in evaluate_a]
            },
            {
                "parcel_id": parcel_b.parcel_id,
                "passed": assessment_b.passed(),
                "results": [asdict(r) for r in evaluate_b]
            }
        ]
    }

    with open(OUTPUT_DIR+"/lab5_report.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    

if __name__ == "__main__":
    main()