import pandas as pd
import glob

files = glob.glob("/Users/paigemason/Desktop/bcog200/vortex-lab/data/raw/*.csv")

all_tornadoes = []

for file in files:
    df = pd.read_csv(file)

    tornadoes = df[df["EVENT_TYPE"] == "Tornado"]
    
    tornadoes = tornadoes[[
        "STATE",
        "MONTH_NAME",
        "TOR_F_SCALE",
        "TOR_WIDTH",
        "TOR_LENGTH",
        "DEATHS_DIRECT",
        "CZ_NAME"
    ]]

    tornadoes["STATE"] = tornadoes["STATE"].str.title()
    all_tornadoes.append(tornadoes)

combined = pd.concat(all_tornadoes)
combined.to_csv("/Users/paigemason/Desktop/bcog200/vortex-lab/data/tornado_data.csv", index=False)