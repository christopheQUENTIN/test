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

json_string = input("paste the json data >>> ")

data = json.loads(json_string)

#df = pd.DataFrame([data])

df = pd.DataFrame(data)


pd.set_option('display.max_columns', None)

print(df)