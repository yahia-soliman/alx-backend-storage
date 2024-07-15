#!/usr/bin/env python3
"""This module list the status of nginx logs"""

if __name__ == "__main__":
    from pymongo import MongoClient

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient()
    coll = client.logs.nginx

    logs_count = coll.count_documents({})
    status_check = coll.count_documents({"method": "GET", "path": "/status"})
    result = coll.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
    ])
    method_count = {doc["_id"]: doc["count"] for doc in result}

    top_ips = coll.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ])

    print(f"{logs_count} logs\nMethods:")
    for method in methods:
        print(f"\tmethod {method}: {method_count.get(method, 0)}")
    print(f"{status_check} status check\nIPs:")

    for ip in top_ips:
        print(f"\t{ip["_id"]}: {ip["count"]}")
