'''
populateDB.py ultimately receives data from webScraper/Scrape.py
and uploads to the AWS Dynamo DB using the boto3 module
'''
import sys
from webScraper import Scrape
import boto3


def main(argv):
    dbConnection = 'boto3()'
    pushDB(dbConnection, getJSON())

def getJSON():
    if (len(argv) < 3):
        print("Usage: python3 populateDB.py <token> <email> <search_param>")
    else:
        token = argv[0]

        email = argv[1]
        search_param = argv[2]

        Scrape.usajob(token,
                      email, 'PositionTitle', search_param)
        Scrape.github(search_param)
    return ['x', 'y']

def pushDB(conn, data):

    return True

if __name__ == '__main__':
    main(sys.argv[1:])
