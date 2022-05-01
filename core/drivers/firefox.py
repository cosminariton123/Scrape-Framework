from selenium import webdriver
from core.drivers.generic_driver import GenericDriver


class FirefoxDriver(GenericDriver(webdriver.Firefox)):
    def __init__(self, executable_path, options=None):
        super().__init__(
            executable_path=executable_path,
            options=options
        )
