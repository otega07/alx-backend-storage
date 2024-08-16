#!/usr/bin/env python3
"""Task 12
"""
from pymongo import MongoClient


def main():
    # Connect to the MongoDB database
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client['logs']
    collection = db['nginx']

    # Get the total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\t{method}: {method_count}")

    # Count for specific condition: method=GET and path=/status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"GET /status: {status_count}")

if __name__ == "__main__":  
    main()
