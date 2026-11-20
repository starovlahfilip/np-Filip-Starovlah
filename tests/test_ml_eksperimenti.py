
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from src.ml_eksperimenti.decorators import measure_time
from src.ml_eksperimenti.experiment import IrisExperiment
from src.ml_eksperimenti.model_factory import ModelFactory
from src.ml_eksperimenti.observers import TrainingMonitor
from src.ml_eksperimenti.strategies import (
    AccuracyStrategy,
    F1Strategy,
    PrecisionStrategy,
    RecallStrategy,
)

# FACTORY TESTOVI

def test_factory_creates_logistic_regression():
    model = ModelFactory.create_model("logistic_regression")
    assert isinstance(model, LogisticRegression)


def test_factory_creates_decision_tree():
    model = ModelFactory.create_model("decision_tree")
    assert isinstance(model, DecisionTreeClassifier)


def test_factory_creates_knn():
    model = ModelFactory.create_model("knn")
    assert isinstance(model, KNeighborsClassifier)


def test_factory_raises_error_for_unknown_model():
    import pytest

    with pytest.raises(ValueError):
        ModelFactory.create_model("unknown")


# STRATEGY TESTOVI

def test_accuracy_strategy():
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]

    assert AccuracyStrategy().calculate(y_true, y_pred) == 0.75


def test_other_metric_strategies():
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]

    assert 0 <= PrecisionStrategy().calculate(y_true, y_pred) <= 1
    assert 0 <= RecallStrategy().calculate(y_true, y_pred) <= 1
    assert 0 <= F1Strategy().calculate(y_true, y_pred) <= 1


# OBSERVER TEST

def test_training_monitor_notifies_observer():
    class FakeObserver:
        def __init__(self):
            self.messages = []

        def update(self, event):
            self.messages.append(event)

    monitor = TrainingMonitor()
    observer = FakeObserver()

    monitor.attach(observer)
    monitor.notify("Test poruka")

    assert observer.messages == ["Test poruka"]


# TEMPLATE METHOD TEST

def test_iris_experiment_returns_valid_accuracy():
    monitor = TrainingMonitor()

    experiment = IrisExperiment(
        model_type="logistic_regression",
        metric=AccuracyStrategy(),
        monitor=monitor,
    )

    result = experiment.run()

    assert 0 <= result <= 1
    assert result > 0.8


# DECORATOR TEST

def test_measure_time_decorator(capsys):
    @measure_time
    def sample_function():
        return "Uspjeh"

    result = sample_function()

    captured = capsys.readouterr()

    assert result == "Uspjeh"
    assert "[TIME]" in captured.out
