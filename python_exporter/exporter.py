import logging
import requests
import time

from environs import Env
from prometheus_client import start_http_server, Gauge, Counter, Summary, Histogram


#REQUESTS_TOTAL = Counter('total_requests_api_page_total','1')
#REQUEST = Counter('requests_total','2',['url','status_code'])
#FAILED = Counter('failed_requests_total','3',['status_code'])
#DURATION = Gauge('request_duration', '4',['url'])

REQUESTS = Gauge('requests_api_page_total','1',['url','status_code'])
DURATION_HYSTO = Histogram('request_duration_histogram', '6',['url','status_code','status'])

class MetricsApi:
    def __init__(self):
        env = Env()
        env.read_env()
        self.url_oncall = env.str("URL_ONCALL")
        self.url_api  = env.str("URL_API")
        self.sleep = env.int("SLEEP_ONCALL")
        self.user = env("USER_ONCALL")
        self.password = env("PASSWORD_ONCALL")
        start_http_server(env.int("PORT_ONCALL"))
        logging.basicConfig(level=env.log_level("LOG_LEVEL"))


    def login(self):
        url = self.url_oncall + "/login"
        payload = 'username={}&password={}'.format(self.user,self.password)
        response = requests.post(url,payload)
        return response
    
    def healthcheck(self):
        url = self.url_oncall + "/healthcheck"
        response = requests.get(url)
        return response
    

    def get_request(self):
        logging.info("Making a request to api oncall...")
        
        self.req = self.login()
        
        if self.req.url == self.url_oncall + "/login":
            DURATION_HYSTO.labels(url=self.url_oncall + "/login",status_code=self.req.status_code,status="").observe(self.req.elapsed.total_seconds())
            REQUESTS.labels(url=self.url_oncall + "/login",status_code=self.req.status_code).inc(1)
            
        logging.info("Making a request to healthcheck oncall...")
        
        self.req = self.healthcheck()

        if self.req.url == self.url_oncall + "/healthcheck":
            if str(self.req.status_code) == '404':
                DURATION_HYSTO.labels(url=self.url_oncall + "/healthcheck",status_code=self.req.status_code,status="could not open healthcheck file").observe(self.req.elapsed.total_seconds())
            elif str(self.req.status_code)[0] == '5':
                DURATION_HYSTO.labels(url=self.url_oncall + "/healthcheck",status_code=self.req.status_code,status="failed to query DB for healthcheck").observe(self.req.elapsed.total_seconds())
            else:
                DURATION_HYSTO.labels(url=self.url_oncall + "/healthcheck",status_code=self.req.status_code,status="success").observe(self.req.elapsed.total_seconds())
            
            REQUESTS.labels(url=self.url_oncall + "/healthcheck",status_code=self.req.status_code).inc(1)        
        
def main():
    time.sleep(10)
    api = MetricsApi()
    
    api.req = api.login()

    while True:
        api.get_request()
        time.sleep(api.sleep)

if __name__ == '__main__':
    main()
    