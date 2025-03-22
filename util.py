def epsilon(val, min, max):
    return min if val < min else (max if val > max else val)