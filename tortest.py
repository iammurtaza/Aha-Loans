import stem.process
from stem import Signal
from stem.control import Controller
from splinter import Browser
import time
proxyIP = "127.0.0.1"
proxyPort = 9150
proxy_settings = {"network.proxy.type":1,"network.proxy.ssl": proxyIP,"network.proxy.ssl_port": proxyPort,"network.proxy.socks": proxyIP,"network.proxy.socks_port": proxyPort,"network.proxy.socks_remote_dns": True,"network.proxy.ftp": proxyIP,"network.proxy.ftp_port": proxyPort}
browser = Browser('firefox', profile_preferences=proxy_settings)
browser.visit("http://www.icanhazip.com")

def switchIP():
	with Controller.from_port(port=9151) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)


for x in range(10):
    browser.visit("http://www.icanhazip.com")
    switchIP()
    time.sleep(5)