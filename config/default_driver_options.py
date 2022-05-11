from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.opera.options import Options as OperaOptions

default_chrome_options = ChromeOptions()
default_chrome_options.add_argument("--start-maximized")
default_chrome_options.add_argument("--incognito")
default_chrome_options.add_argument("--headless")

default_edge_options = EdgeOptions()
#default_edge_options.add_argument("--start-maximized")
#default_edge_options.add_argument("--headless")

default_firefox_options = FireFoxOptions()
#default_firefox_options.add_argument("--start-maximized")
#default_firefox_options.add_argument("--headless")

default_opera_options = OperaOptions()
#default_opera_options.add_argument("--start-maximized")
#default_opera_options.add_argument("--headless")


TIMEOUT = 15
STALE_TIMEOUT = 2
NUMBER_OF_TRIES_FOR_STALE_OBJECTS = 5
