from config.default_driver_options import default_chrome_options, default_edge_options, default_firefox_options, \
    default_opera_options
from config.paths import CHROMEDRIVERPATH, EDGEDRIVERPATH, FIREFOXDRIVERPATH, OPERADRIVERPATH, SAFARIDRIVERPATH
from core.drivers.chrome import ChromeDriver
from core.drivers.edge import EdgeDriver
from core.drivers.firefox import FirefoxDriver
from core.drivers.opera import OperaDriver


def get_new_default_chrome_driver():
    return ChromeDriver(executable_path=CHROMEDRIVERPATH,
                        options=default_chrome_options
                        )


def get_new_default_edge_driver():
    return EdgeDriver(executable_path=EDGEDRIVERPATH,
                      options=default_edge_options
                      )


def get_new_default_firefox_driver():
    return FirefoxDriver(executable_path=FIREFOXDRIVERPATH,
                         options=default_firefox_options
                         )


def get_new_default_opera_driver():
    return OperaDriver(executable_path=OPERADRIVERPATH,
                       options=default_opera_options
                       )



DRIVER = None
