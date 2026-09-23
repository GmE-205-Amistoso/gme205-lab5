from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class RuleResult:
    rulename: str
    passed: bool
    message: str

class AssessmentRule(ABC):
    def __init__(self, name):
        if not name:
            raise ValueError("name is required.")
        
        self._name = name

    @abstractmethod
    def evaluate(self, parcel) -> RuleResult:
        pass

    @property
    def name(self) -> str:
        return self._name

class ParcelAssessment:
    def __init__(self, parcel, rules):
        if (not rules) or (len(rules) == 0):
            raise ValueError("At least one rule is required.")

        self._parcel = parcel
        self._rules = rules

    def evaluate(self):
        results = []
        for rule in self._rules:
            result = rule.evaluate(self._parcel)
            results.append(result)
        return results

    def passed(self):
        for result in self.evaluate():
            if not result.passed:
                return False
        return True