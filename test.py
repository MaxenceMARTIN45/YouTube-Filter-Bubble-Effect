from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

profile_path = r'C:\Program Files\Python39\Scripts\geckodriver-0.31.0'
options=Options()
options.set_preference('profile', profile_path)
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '127.0.0.1')
options.set_preference('network.proxy.socks_port', 9050)
options.set_preference('network.proxy.socks_remote_dns', False)
service = Service('C:\\BrowserDrivers\\geckodriver.exe')
driver = Firefox(service=service, options=options)
driver.get("https://www.google.com")
driver.quit()