import os
from dotenv import load_dotenv
import requests
import datetime
import time
load_dotenv()

SESSION = os.getenv("SESSION")
cookies = {'session': SESSION}
while (datetime.datetime.now().strftime("%H") != "21"):
    time.sleep(1)
d = datetime.datetime.now()

date = int(d.strftime("%d"))+1
r = requests.get(f'https://adventofcode.com/2022/day/{date}/input', cookies=cookies)
with open(f"day{date}.in", "w") as f:
    f.write(r.text)
