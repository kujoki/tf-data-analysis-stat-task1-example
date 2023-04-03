import pandas as pd
import numpy as np


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    dt = 56 / (len(x) - 1)
    v = np.diff(x) / dt
    a = np.diff(v) / dt
    
    mu = np.mean(a)
    
    return mu
