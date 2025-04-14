# predictor.py

# Paste the r6econ() function here from server.py
# For now, this is just a placeholder until you send me the actual function

def r6econ(data):
    # example logic — replace with real function logic
    if not data:
        return 0
    return int(sum(data) / len(data))
