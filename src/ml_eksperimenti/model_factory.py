
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


class ModelFactory:

    @staticmethod
    def create_model(model_type: str):
        if model_type == "logistic_regression":
            return LogisticRegression(max_iter=200)

        elif model_type == "decision_tree":
            return DecisionTreeClassifier(random_state=42)

        elif model_type == "knn":
            return KNeighborsClassifier(n_neighbors=5)

        else:
            raise ValueError(f"Nepoznat tip modela: {model_type}")
