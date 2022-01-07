from typing import List
import numpy as np
from scipy import stats


def calculate_correlation(x: List[float], y: List[float]):
    assert len(x) == len(y)

    return np.corrcoef(x, y)[0][1], stats.ttest_ind(x, y)[1]
