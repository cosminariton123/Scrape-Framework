from selenium import webdriver
from core.drivers.generic_driver import GenericDriver


class EdgeDriver(GenericDriver(webdriver.Edge)):
    def __init__(self, executable_path, options=None):
        super().__init__(
            executable_path=executable_path,
            options=options
        )
