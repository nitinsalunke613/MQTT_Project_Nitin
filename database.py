from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, db_name="mqtt_data", collection_name="messages"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_message(self, message):
        self.collection.insert_one(message)

    def aggregate_status_count(self, start_time, end_time):
        pipeline = [
            {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
            {"$group": {"_id": "$status", "count": {"$sum": 1}}}
        ]
        return list(self.collection.aggregate(pipeline))
