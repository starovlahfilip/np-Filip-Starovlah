from .experiment import IrisExperiment
from .observers import ConsoleObserver, TrainingMonitor
from .strategies import AccuracyStrategy


def main():
    monitor = TrainingMonitor()
    monitor.attach(ConsoleObserver())

    experiment = IrisExperiment(
        model_type="logistic_regression",
        metric=AccuracyStrategy(),
        monitor=monitor,
    )

    rezultat = experiment.run()

    print(f"\nKonačna tačnost modela: {rezultat:.4f}")


if __name__ == "__main__":
    main()