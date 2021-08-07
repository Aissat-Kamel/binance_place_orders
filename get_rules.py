"""
from time to time you have to delete "ticker_rules.py" file
and run this file to create new update to the rules
"""
from binance_client import client
import math

rules = {}

info = client.get_exchange_info()
for i in info["symbols"]:
    minPrice = int(round(-math.log(float(i["filters"][0]["minPrice"]), 10), 0))
    tickSize = int(round(-math.log(float(i["filters"][0]["tickSize"]), 10), 0))
    minQty = int(round(-math.log(float(i["filters"][2]["minQty"]), 10), 0))
    stepSize = int(round(-math.log(float(i["filters"][2]["stepSize"]), 10), 0))
    minNotional = float(i["filters"][3]["minNotional"])
    rules[i["symbol"]] = [minPrice, tickSize, minQty, stepSize, minNotional]

with open('ticker_rules.py', 'x') as f:
    f.write('# 0 -- minPrice \n# 1 -- tickSize \n# 2 -- minQty \n# 3 -- stepSize \n# 4 -- minNotional \nrules = '+str(rules))
