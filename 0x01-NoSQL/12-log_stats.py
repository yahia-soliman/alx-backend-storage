#!/usr/bin/env python3
"""This module list the status of nginx logs"""

if __name__ == "__main__":
    from pymongo import MongoClient

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient()
    collection = client.logs.nginx

    logs_count = collection.count_documents({})
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    result = collection.aggregate([
        { "$group": {"_id": "$method", "c": {"$count": {}}} },
    ])
    method_count = {doc["_id"]: doc["c"] for doc in result}

    print(f"{logs_count} logs\nMethods:")
    for method in methods:
        print(f"\tmethod {method}: {method_count.get(method, 0)}")
    print(f"{status_check} status check")
