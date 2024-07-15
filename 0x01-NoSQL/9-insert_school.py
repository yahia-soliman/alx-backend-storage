#!/usr/bin/env python3
"""Create documents with PyMongo"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document into a given mongo collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
