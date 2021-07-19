#stock ticker


import requests
import os
import time
import json

from google.cloud import pubsub_v1

class Publish:
    def __init__(self):
        self.project_id = "elevated-summer-320003"
        self.topic_id = "Stocks"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rajath/python-docker/elevated-summer-320003-421b6b5793ff.json"


    def fetch_stock(self):
        url = 'https://api.polygon.io/v3/reference/tickers?ticker=AAPL&active=true&sort=ticker&order=asc&limit=10&apiKey=ntNvf_gwrWHNHnGeMDM51Bkgb6W_UpqN'
        #set key as envt var

        response = requests.get(url)
        #print(response.json())
        #time.sleep(10)
        string = response.json()['results'][0]
        string['active']= str(string['active'])

        json_string = json.dumps(string)
        print("string =",json_string)

        return str(json_string)


    def publish_msg(self):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id,self.topic_id)

        # fetch_stock should be byte string
        stock_data = self.fetch_stock()
        stock_data = stock_data.encode("utf-8")

        future = publisher.publish(topic_path,stock_data)
        print(future.result())





pub = Publish()
pub.publish_msg()
pub.fetch_stock()
