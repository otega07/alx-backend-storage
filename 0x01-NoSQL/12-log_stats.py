#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Prints stats about Nginx request logs."""
    # Number of logs
    log_count = nginx_collection.count_documents({})
    print(f'{log_count} logs')

    # Number of logs for each HTTP method
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    # Number of logs where method is GET and path is /status
    status_check_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f'{status_check_count} status check')


def run():
    """Connects to MongoDB and retrieves stats."""
    # Connecting to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Accessing the database and collection
    nginx_collection = client.logs.nginx

    # Printing the request logs stats
    print_nginx_request_logs(nginx_collection)


if __name__ == '__main__':
    run()

# Start MongoDB from command line
# mongo
require 'establish_connection' 

# Everything is documented with comments and explanations in the script file.

# Check for conditions: Collection nginx empty, with 1 document, with 10 documents, with a lot of documents.

# Stop MongoDB: exit
