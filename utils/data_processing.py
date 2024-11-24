import pandas as pd

def load_user_data(filepath):
    return pd.read_csv(filepath)

def load_activity_data(filepath):
    return pd.read_json(filepath)
