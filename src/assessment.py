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