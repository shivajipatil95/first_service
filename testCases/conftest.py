import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
    return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# Step 7:  Run Tests on Desired Browser(Cross Browser Testing)/Parallel
#
# 	7.1: update contest.py with required fixtures which will accept command line argument (browser).
# 7.2: Pass browser name as argument in command line
#
# To Run tests on desired browser
# pytest -s -v .\testCases\test_001_AccountRegistration.py --browser edge
#
# To Run tests parallel
# pytest -s -v -n=3 .\testCases\test_001_AccountRegistration.py --browser edge
########### pytest HTML Report ################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'
    #config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

#
# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Step 8:  Generate pytest HTML Reports
    #
    # 8.1: Update conftest.py with pytest hooks
    #
    # pytest -s -v --html=reports\report.html --capture=tee-sys .\testCases\test_001_A
    # ccountRegistration.py --browser chrome

#Specifying report folder location and save report with timestamp
    @pytest.hookimpl(tryfirst=True)
    def pytest_configure(config):
        config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

#