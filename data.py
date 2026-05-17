import pandas as pd
import random

def load_and_filter_data():
    df = pd.read_csv(/Users/paigemason/Desktop/bcog200/vortex-lab/data/tornado_data.csv)
    df["STATE"] = df["STATE"].str.title()
    filtered = df[
        (df["STATE"] == state) &
        (df["MONTH_NAME"] == month)
    ]

    if len(filtered) < 5:
        print("Low chance of tornado formation.")
    return filtered

def adjust_intensity(ef_rating, temperature, humidity):
    new_rating = ef_rating

    if temperature >= 70 and humidity >= 60:
        new_rating += 1
    elif temperature <= 60 or humidity <= 40:
        new_rating -= 1

    if new_rating < 0:
        new_rating = 0
    elif new_rating > 5:
        new_rating = 5

    return new_rating