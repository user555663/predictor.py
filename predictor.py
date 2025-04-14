# predictor.py

def r6econ(data):
    """
    Predicts the next value based on the average of the last 10 entries.
    """
    if not data:
        return 0
    return round(sum(data[-10:]) / min(len(data), 10))
