#!/usr/bin/env python3
"""Filter documents with PyMongo"""


def schools_by_topic(mongo_collection, topic):
    """Get a list of documents having specific topic"""
    return mongo_collection.find({"topics": topic})
