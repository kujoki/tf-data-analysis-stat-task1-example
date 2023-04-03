import pandas as pd
import numpy as np


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    T = 56
    a = x * 2 / T**2
    median = np.median(a)
    return median
