#!/usr/bin/python

import json
import datetime
import time

from pprint import pprint

from db_api import CouchAPI
from temp_data import temp_data
from config import DATABASE_NAME


if __name__ == "__main__":

    total_documents = 0
    new_api = CouchAPI("localhost", 5984)

    start_hour = datetime.datetime.now().hour * 60 * 60
    start_minute = datetime.datetime.now().minute * 60
    start_second = datetime.datetime.now().second
    start_time = start_hour + start_minute + start_second

    for doc in temp_data:
        data = json.dumps(doc)
        print new_api.create_doc(DATABASE_NAME, data)
        total_documents = total_documents + 1

    end_hour = datetime.datetime.now().hour * 60 * 60
    end_minute = datetime.datetime.now().minute * 60
    end_second = datetime.datetime.now().second
    end_time = end_hour + end_minute + end_second

    total_time = end_time - start_time

    print "Total time was %s seconds." % (total_time)
    print "Total writes were %s documents." % (len(temp_data))
    print "Writes per second %f." % (len(temp_data) / total_time * 1.0)
