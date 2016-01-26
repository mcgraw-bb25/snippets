#!/usr/bin/python

import httplib
import json
from pprint import pprint


class CouchAPI(object):
    ''' class to wrap HTTP methods to access CouchDB '''

    def __init__(self, host, port=5984):
        self.host = host
        self.port = port
        self.base_uri = "http://%s:%s/" % (host, port)

    def connect(self):
        return httplib.HTTPConnection(self.host, self.port)

    def get(self, uri):
        connection = self.connect()
        headers = {"Accept": "application/json"}
        connection.request("GET", uri, None, headers)
        return connection.getresponse()

    def post(self, uri, body):
        connection = self.connect()
        headers = {"Content-type": "application/json"}
        connection.request("POST", uri, body, headers)
        return connection.getresponse()

    def put(self, uri, body):
        connection = self.connect()
        headers = {"Content-type": "application/json"}
        connection.request("PUT", uri, body, headers)
        return connection.getresponse()

    def get_new_uuid(self):
        ''' 
        generates a new uuid 
        note: should throw real errors...
        '''
        uuid_generator = self.base_uri + "_uuids"
        try:
            uuid_doc = self.get(uuid_generator)
            if uuid_doc.status == 200:
                uuid_doc = json.loads(uuid_doc.read())
                return uuid_doc["uuids"][0]
            else:
                return "Error! No UUID created."
        except:
            return "Error! No UUID created."

    def build_database_uri(self, database):
        ''' returns database string '''
        return self.base_uri + database + "/"

    def create_doc(self, database, content):
        ''' 
        creates a new document in database
        only accepts new data, does not update
        '''
        uri = self.build_database_uri(database) + self.get_new_uuid()
        request = self.put(uri, content)
        return request.read()


if __name__ == "__main__":

    pass