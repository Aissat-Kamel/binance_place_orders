import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Trading_bot"]

class Types():
    buy_market = "buy_market_orders"
    sell_market = "sell_market_orders"
    buy_limit = "buy_limit_orders"
    sell_limit = "sell_limit_orders"
    sell_oco = "sell_oco_orders"


class Orders():
    def save_order(collection, order):
        collection = db[collection]
        data = collection.insert(order)
        return data
