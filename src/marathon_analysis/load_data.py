import os
import kagglehub
import pandas as pd
from dataclasses import dataclass


@dataclass
class Data:
    results: pd.DataFrame
    races: pd.DataFrame


def load() -> Data:
    path = kagglehub.dataset_download("runningwithrock/2024-marathon-results")
    results_path = os.path.join(path, '2024 Results.csv')
    races_path = os.path.join(path, '2024 Races.csv')
    results = pd.read_csv(results_path)
    races = pd.read_csv(races_path)

    return Data(results, races)
