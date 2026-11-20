
from abc import ABC, abstractmethod

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from .decorators import measure_time
from .model_factory import ModelFactory
from .observers import TrainingMonitor
from .strategies import MetricStrategy


class BaseExperiment(ABC):
    def __init__(
        self,
        model_type: str,
        metric: MetricStrategy,
        monitor: TrainingMonitor,
    ):
        self.model_type = model_type
        self.metric = metric
        self.monitor = monitor

    @measure_time
    def run(self) -> float:
        """Template Method – definiše tok eksperimenta."""

        self.monitor.notify("Eksperiment je započet.")

        X, y = self.load_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y,
        )

        model = ModelFactory.create_model(self.model_type)

        self.monitor.notify("Treniranje modela je započeto.")
        model.fit(X_train, y_train)
        self.monitor.notify("Treniranje modela je završeno.")

        predictions = model.predict(X_test)

        rezultat = self.metric.calculate(y_test, predictions)

        self.monitor.notify("Evaluacija modela je završena.")
        self.monitor.notify(f"Rezultat metrike: {rezultat:.4f}")

        return rezultat

    @abstractmethod
    def load_data(self):
        """Učitavanje podataka za eksperiment."""
        pass


class IrisExperiment(BaseExperiment):
    def load_data(self):
        iris = load_iris()
        return iris.data, iris.target
