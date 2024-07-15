#!/usr/bin/env python3
"""This module list the students sorted by the average score"""


def top_students(mongo_collection):
    """get students sorted by avg score"""
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": 1, "topics": 1,
                "averageScore": {"$avg": "$topics.score"},
            }
        },
        {"$sort": {"averageScore": -1}},
    ])
