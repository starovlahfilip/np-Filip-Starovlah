
from typing import Protocol


class Observer(Protocol):
    def update(self, event: str) -> None:
        ...


class ConsoleObserver:
    def update(self, event: str) -> None:
        print(f"[INFO] {event}")


class TrainingMonitor:
    def __init__(self):
        self.observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event: str) -> None:
        for observer in self.observers:
            observer.update(event)
