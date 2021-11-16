import pandas as pd
import json
from pathlib import Path

p = Path(r'Schedule.json')
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

df = pd.json_normalize(data)

df.to_csv('Schedule_4.csv', encoding='UTF-8')
