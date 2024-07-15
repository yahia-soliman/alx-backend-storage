#!/usr/bin/env python3
"""First thing to do with PyMongo"""


def list_all(mongo_collection):
    """List all documents in mongo_collection"""
    return mongo_collection.find()
