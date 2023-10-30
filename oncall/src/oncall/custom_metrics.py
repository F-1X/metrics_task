from prometheus_client import Gauge, start_http_server, Histogram
import time
import logging
import os
import psutil

logger = logging.getLogger()


def uptime():
    with open('/proc/uptime', 'r') as f:
        seconds = float(f.readline().split()[0])
    return seconds


def get_la():
    return os.getloadavg()


def get_process_info(user):
    mem_total = 0
    cpu_total = 0
    for process in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'cpu_percent']):
        logger.info(process.info)

        if process.info['username'] == user:
            mem_total += (process.info['memory_info'].rss/1024)/1024
            cpu_total += process.info['cpu_percent']
            
    return {"mem": mem_total, "cpu": cpu_total}


class CustomMetrics(object):
    def __init__(self):
        self.LA_ONCALL = Gauge('la_load_average', '', ['LA'])
        self.LA_ONCALL_HIST = Histogram('la_load_average_oncall_hist','',['LA'],buckets=[0.1,0.25,0.5,0.75,1,1.5,2,2.5,3.5,4,5])
        
        self.MEM_ONCALL = Gauge('oncall_usage_memory' , '')
        self.CPU_ONCALL = Gauge('oncall_usage_cpu' , '')
        
        self.CPU_HIST = Histogram('cpu_hist','',)
        self.MEM_HIST = Histogram('mem_hist' , '')
        
        self.UPTIME = Gauge("uptime",'')
        
        self.process_user= "oncall"
        start_http_server(8882)
        
        
        

    def start(self):
        la = get_la()

        self.LA_ONCALL.labels(LA="1").set(la[0])
        self.LA_ONCALL.labels(LA="5").set(la[1])
        self.LA_ONCALL.labels(LA="15").set(la[2])

        self.LA_ONCALL_HIST.labels(LA="1").observe(la[0])
        self.LA_ONCALL_HIST.labels(LA="5").observe(la[1])
        self.LA_ONCALL_HIST.labels(LA="15").observe(la[2])

        process = get_process_info(self.process_user)
        
        self.CPU_ONCALL.set(process["cpu"])
        self.MEM_ONCALL.set(process["mem"])
        
        self.CPU_HIST.observe(process["cpu"])
        self.MEM_HIST.observe(process["mem"])

        self.UPTIME.set(uptime())

def main():
    a = CustomMetrics()
    while True:
        a.start()
        time.sleep(10)

if __name__ == '__main__':
    main()
    
    
        