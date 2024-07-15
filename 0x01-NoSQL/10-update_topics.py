#!/usr/bin/env python3
"""Update documents with PyMongo"""


def update_topics(mongo_collection, name, topics):
    """update the topics of schools what the given name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
