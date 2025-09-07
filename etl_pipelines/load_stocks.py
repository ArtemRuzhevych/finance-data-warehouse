import pandas as pd
import sqlalchemy as sql

def load_stocks(file_path):
    data = pd.read_csv(file_path)
    return data

