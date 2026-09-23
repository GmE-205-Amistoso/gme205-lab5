import pytest
from assessment import AssessmentRule, RuleResult, ParcelAssessment
from spatial import Parcel
from rules import MinimumAreaRule
import dataclasses
from shapely.geometry import box

# -----------------------
# AssessmentRule Tests
# -----------------------

# Testing AssessmentRule's base behavior
class DummyRule(AssessmentRule):
    def evaluate(self, parcel):
        return RuleResult(self.name, True, "dummy result")

def test_assessment_rule_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        AssessmentRule("Some rule")

def test_assessment_rule_raises_on_empty_name():
    with pytest.raises(ValueError):
        DummyRule("")

def test_assessment_rule_raises_on_none_name():
    with pytest.raises(ValueError):
        DummyRule(None)

def test_assessment_rule_name_property_returns_constructor_value():
    rule = DummyRule("Minimum parcel area")
    assert rule.name == "Minimum parcel area"

def test_dummy_rule_evaluate_returns_rule_result():
    rule = DummyRule("Dummy")
    result = rule.evaluate(parcel=None)
    assert isinstance(result, RuleResult)
    assert result.rulename == "Dummy"
    assert result.passed is True

# -----------------------
# RuleResult Tests
# -----------------------

# Test if RuleResult is still immutable (frozen=True)
def test_rule_result_is_immutable():
    result = RuleResult("Some rule", True, "ok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.passed = False

def test_rule_result_equality():
    a = RuleResult("Some rule", True, "ok")
    b = RuleResult("Some rule", True, "ok")
    assert a == b

# -----------------------
# ParcelAssessment Tests
# -----------------------

def test_parcel_assessment_no_rules_raised_exception():
    parcel = Parcel(
        "P-001",
        box(0, 0, 80, 80),
        "Residential",
        7200
    )
    with pytest.raises(ValueError):
        assessment = ParcelAssessment( 
            parcel=parcel, 
            rules=[], 
        )

def test_parcel_assessment_with_rules_passed():
    parcel = Parcel(
        "P-001",
        box(0, 0, 80, 80),
        "Residential",
        7200
    )
    assessment = ParcelAssessment( 
        parcel=parcel, 
        rules=[MinimumAreaRule(5000)], 
    )
    assert assessment.passed()