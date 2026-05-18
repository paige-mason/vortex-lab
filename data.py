import pandas as pd
import random

def load_and_filter_data(filepath, state, month):
    df = pd.read_csv(filepath)
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

    new_rating = max(0, min(new_rating, 5))

    return new_rating

def generate_day():
    return random.randint(1, 28)

def estimate_wind_speed(ef_rating):
    wind_ranges = {
        0: (65, 85),
        1: (86, 110),
        2: (111, 135),
        3: (136, 165),
        4: (166, 200),
        5: (201, 321)
    }
    low, high = wind_ranges[ef_rating]
    return random.randint(low, high)

def clean_ef_rating(value):
    if pd.isna(value):
        return 0
    value = str(value).replace("EF", "")
    value = value.strip()

    if value == "U":
        return 0
    try:
        return int(value)
    except ValueError:
        return 0

def generate_tornado_event(filtered_data, temperature, humidity):
    if filtered_data.empty:
        return None
    
    location = filtered_data.sample(n=1).iloc[0]
    state = location["STATE"]
    county = location["CZ_NAME"]
    month = location["MONTH_NAME"]

    ef_rating = random.choice(filtered_data["TOR_F_SCALE"].dropna().tolist())
    ef_rating = clean_ef_rating(ef_rating)
    ef_rating = adjust_intensity(ef_rating, temperature, humidity)
    max_ef = clean_ef_rating(filtered_data["TOR_F_SCALE"].dropna().max())
    ef_rating = min(ef_rating, max_ef)
    ef_subset = filtered_data[filtered_data["TOR_F_SCALE"].fillna(0).apply(clean_ef_rating) == ef_rating]
    if ef_subset.empty:
        ef_subset = filtered_data

    path_width = random.choice(ef_subset["TOR_WIDTH"].dropna().tolist())
    path_length = random.choice(ef_subset["TOR_LENGTH"].dropna().tolist())
    fatalities = random.choice(ef_subset["DEATHS_DIRECT"].dropna().tolist())

    wind_speed = estimate_wind_speed(ef_rating)
    day = generate_day()

    event = {
        "state": state,
        "county": county,
        "month": month,
        "day": day,
        "ef_rating": ef_rating,
        "wind_speed": wind_speed,
        "path_width": path_width,
        "path_length": path_length,
        "fatalities": fatalities
    }
    return event
    # future improvement: use weather to influence EF probability before selection
