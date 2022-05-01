import os

_DRIVERS_PATH = "driver_executables"

CHROMEDRIVERPATH = os.path.join(_DRIVERS_PATH, "chromedriver.exe")

EDGEDRIVERPATH = os.path.join(_DRIVERS_PATH, "msedgedriver.exe")

FIREFOXDRIVERPATH = ""

OPERADRIVERPATH = ""

SAFARIDRIVERPATH = ""

RESOURCESPATH = "resources"

INPUT_FILES_PATH = os.path.join(RESOURCESPATH, "input")

OUTPUT_FILES_PATH = os.path.join(RESOURCESPATH, "output")

EXCEL_INPUT_FILENAME = "Template.xlsx"
