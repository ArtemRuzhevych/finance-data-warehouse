import pandas as pd
import sqlalchemy as db
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_SERVER = os.getenv('DATABASE_SERVER')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

try:
    db = db.create_engine(f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_NAME}")
    print("Database connection established successfully.")
except Exception as e:
    print("Error connecting to the database:", e)

def load_stocks(file_path):
    data = pd.read_csv(file_path)
    return data

def insert_data(data):
    try:
        data.to_sql('stocks', con=db, if_exists='append', index=False)
        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)

if __name__ == "__main__":
    insert_data(load_stocks('nasdaq100_components.csv'))