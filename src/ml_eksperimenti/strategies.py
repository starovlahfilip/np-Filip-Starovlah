
from typing import Protocol

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)


class MetricStrategy(Protocol):
    def calculate(self, y_true, y_pred) -> float:
        ...


class AccuracyStrategy:
    def calculate(self, y_true, y_pred) -> float:
        return accuracy_score(y_true, y_pred)


class PrecisionStrategy:
    def calculate(self, y_true, y_pred) -> float:
        return precision_score(
            y_true, y_pred, average="weighted", zero_division=0
        )


class RecallStrategy:
    def calculate(self, y_true, y_pred) -> float:
        return recall_score(
            y_true, y_pred, average="weighted", zero_division=0
        )


class F1Strategy:
    def calculate(self, y_true, y_pred) -> float:
        return f1_score(
            y_true, y_pred, average="weighted", zero_division=0
        )
