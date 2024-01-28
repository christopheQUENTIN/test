"""

import json
import pandas as pd

json_string = input("paste the json data >>> ")

data_dict = json.loads(json_string)

df = pd.DataFrame([data_dict])

pd.set_option('display.max_columns', None)

print(df)

"""

"""
import json
import pandas as pd

json_string = input("paste the json data >>> ")

data = json.loads(json_string)

if isinstance(data, dict):
   df = pd.DataFrame([data])
elif isinstance(data, list):
    df = pd.DataFrame(data)
else:
    raise("unable to convert json object into a python list or dictionnary , thus failing providing dataframe")

#df = pd.DataFrame([datat])

pd.set_option('display.max_columns', None)

print(df)
"""

import json
import pandas as pd

json_string = input("\n\n paste the json data >>> ")

try:
    # Replace 'json_data' with your JSON string or file
    data = json.loads(json_string)
    # Process your data here
except json.decoder.JSONDecodeError as e:
    print("JSON Decode Error: ", e)

#data = json.loads(json_string)


if isinstance(data, dict):
    for (key, value) in data.items():
        print("\n  ",key,"  :   ", value)
    df = pd.DataFrame([data])

elif isinstance(data, list):
    df = pd.DataFrame(data)
else:
    raise("unable to convert json object into a python list or dictionnary , thus failing providing dataframe")

print("\n\n\n ")

print("len_data = ",len(data),"   confirm type : ",type(data))




#df = pd.DataFrame([data]) # crash en multirow

#df = pd.DataFrame(data)  # ValueError: All arrays must be of the same length   ONELINER json

print("\n\n\n _________________________________________________________________________________________ \n\n\n")

#pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', 20)


print(df)