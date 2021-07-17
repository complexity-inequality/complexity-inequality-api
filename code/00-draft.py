

import pandas as pd
import requests
import json

response = requests.get('http://localhost:8000/df')
pd.read_json(response.content)