import json
import pandas as pd

json_string = input("paste the json data >>> ")

data_dict = json.loads(json_string)

df = pd.DataFrame([data_dict])

pd.set_option('display.max_columns', None)

print(df)
