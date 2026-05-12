import pandas as pd
import glob

files = glob.glob("/Users/paigemason/Desktop/bcog200/vortex-lab/data/raw/*.csv")

all_tornadoes = []

for file in files:
    df = pd.read_csv(file)

    tornadoes = df[df["EVENT_TYPE"] == "Tornado"]
    all_tornadoes.append(tornadoes)
    
    tornadoes = tornadoes[[
        "STATE",
        "MONTH_NAME",
        "TOR_F_SCALE",
        "TOR_WIDTH",
        "TOR_LENGTH",
        "DEATHS_DIRECT",
        "CZ_NAME"
    ]]
combined = pd.concat(all_tornadoes)
combined["STATE"] = combined["STATE"].str.title()
combined.to_csv("/Users/paigemason/Desktop/bcog200/vortex-lab/data/tornado_data.csv", index=False)