from assessment import AssessmentRule, RuleResult

class MinimumAreaRule(AssessmentRule):
    def __init__(self, min_area):
        super().__init__("Minimum parcel area")
        self._min_area = min_area

    def evaluate(self, parcel):
        passed = parcel.area_sqm >= self._min_area
        message = (
            f"{parcel.area_sqm:.0f} m² >= {self._min_area:.0f} m²"
            if passed
            else f"{parcel.area_sqm:.0f} m² < {self._min_area:.0f} m²"
        )
        return RuleResult(self.name, passed, message)

class AllowedZoneRule(AssessmentRule):
    def __init__(self, allowed_zones):
        super().__init__("Allowed zones")
        self._allowed_zones = allowed_zones

    def evaluate(self, parcel):
        passed = parcel.zone in self._allowed_zones
        message = (
            f"{parcel.zone} is in the allowed zones {self._allowed_zones}"
            if passed
            else f"{parcel.zone} is not in the allowed zones {self._allowed_zones}"

        )
        return RuleResult(self.name, passed, message)

class NoHazardOverlapRule(AssessmentRule):
    def __init__(self, hazard_zone):
        super().__init__("No hazard overlap")
        self._hazard_zone = hazard_zone

    def evaluate(self, parcel):
        passed = not parcel.intersects(self._hazard_zone)
        message = (
            f"{parcel.parcel_id} is not in a mapped hazard zone {self._hazard_zone.zone_id}"
            if passed
            else f"{parcel.parcel_id} intersects a mapped hazard zone {self._hazard_zone.zone_id}"

        )
        return RuleResult(self.name, passed, message)