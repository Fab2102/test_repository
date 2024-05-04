import pandas as pd
import json

data1 = "/Users/Fabian/Documents/Studium/2 CBK/GdWINF/Assignment/data.json"

with open(data1) as f:
    data = json.load(f)

    

df = pd.DataFrame(data)
df.to_excel('data.xlsx')
