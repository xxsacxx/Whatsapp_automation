import requests
import time
import sys 
import os.path
import logging
import os
import time
from msgg import whtsapp_ip_msg


#logging
logger = logging.getLogger(__name__)  
here = os.path.dirname(os.path.abspath(__file__))
#here = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(here, 'ip_chkr.log')
# set log level
logger.setLevel(logging.DEBUG)
# define file handler and set formatter
file_handler = logging.FileHandler(log_file)
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


"List of free ip services"
"http://icanhazip.com/"
"http://checkip.dyndns.org/"
"https://freegeoip.net/json/"
"http://www.telize.com/ip"
"http://ip-api.com/json"
"http://curlmyip.com/"
"http://ipinfo.io/ip"

#Global variables
ipFile="/tmp/ip.log"
timeout = 10

class Service:
  url=""
  def request(self): return requests.get(self.url, timeout = timeout)

class Icanhazip(Service):
  name="icanhazip"
  url="http://icanhazip.com/"
  def ip(self): return self.request().text.strip()

class Freegeoip(Service):
  name="freegeoip"
  url="https://freegeoip.net/json/"
  def ip(self): return self.request().json()["ip"]

class Telize(Service):
  name="telize"
  url="http://www.telize.com/ip"
  def ip(self): return self.request().text.strip()

class IpApi(Service):
  name="ip-api"
  url="http://ip-api.com/json"
  def ip(self): return self.request().json()["query"]

class Ifconfig(Service):
  name="ifconfig.me"
  url="http://ifconfig.me/all.json"
  def ip(self): return self.request().json()["ip_addr"]

def request_ip():
  #List of services
  services = [Ifconfig()]
  for i in range(len(services)):
    
    service = services[i]
    try:
      start = time.time()
      logger.info( "* Requesting current ip with '{}'".format(service.name))
      ip = service.ip()
      logger.info("* Request took {} seconds ".format(int(time.time() - start)))
      return ip
    except Exception as error:
      logger.error("* Exception when requesting ip using '{}': {} ".format(service.name, error ))
      
  error = "Non available services, add more services or increase the timeout (services = {}, timeout = {}) ".format(len(services), timeout)
  raise RuntimeError(error)

def current_ip():
  return open(ipFile,"r").readlines()[0]

def save_ip(ip):
  f = open(ipFile,'w')
  f.write(str(ip)) 

#Main
def ip_chk():
    if os.path.isfile(ipFile) : #File exists
        request_ipv = request_ip()  
        current_ipv = current_ip()

        if request_ipv != current_ipv:
            save_ip(request_ipv)
            logger.info("* IP has changed from {} to {}".format(current_ipv, request_ipv))
            whtsapp_ip_msg(ip = current_ipv)
            sys.exit(1)
        else :
            logger.info("* IP is still the same: {}".format(current_ipv))

    else: 
        request_ipv = request_ip()
        save_ip(request_ipv)
        logger.info("* This is the first time to run the ip_change script, I will create a file in {} to store your current address: {} ".format(ipFile, request_ipv))
ip_chk()
#Test
"""
services = [Icanhazip(), Freegeoip(), Telize(), IpApi(), Ifconfig() ]
for i in range(len(services)):
  service = services[i]
  print "{} ip result: {} ".format(service.name, service.ip() )
"""