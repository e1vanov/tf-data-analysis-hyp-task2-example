import pandas as pd
import numpy as np
from scipy import stats


chat_id = 464814509 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #t, p = stats.ks_2samp(x, y)
    res = stats.cramervonmises_2samp(x, y)
    return res.pvalue <= 0.08
