

import time

import allure
import pytest

from DataDrivenFrameWork import DataUtil
from DataDrivenFrameWork.Base import abc
from DataDrivenFrameWork.ReadingData import XLReader


def getTestData():
    global xls
    global testCaseName

    print("Get Test Data Called")
    # Initializing XLS Reader
    xls = XLReader("C:\\Users\\whizdom\\Desktop\\Book1.xlsx")
    
        # Specifying Test Case Name
    testCaseName = "TestB"
    
    return DataUtil.getTestData(testCaseName, xls)

@pytest.mark.parametrize("dataRetrievedDictionary", getTestData())
def test_logIn(dataRetrievedDictionary):
        with allure.step(" Screenshot added !!"):  
        
            base = abc()
        if (DataUtil.isRunnable(testCaseName, readXLS) and dataRetrievedDictionary.get('Runmode') == "Y"):
            base.OpenBrowser("Chrome")
            base.Navigate("URL")
            if(not base.isElementPresent("email_xpath")) :
                base.ReportFail("Element is not present")        
            if(not base.verifyText("signin_xpath" , "signinText")):
                base.ReportFail("Not verified")
            base.Type("email_xpath" , "email_id")
            time.sleep(5)
            base.Click("click_xpath")
            time.sleep(5)
            base.verifyText("signin_xpath", "signinText")
            base.ReportFail("Title doesn't match")
            print(dataRetrievedDictionary.get("FirstName"), dataRetrievedDictionary.get("LastName"))
        else:
            print("Runmode is set to N")
            pytest.skip("Runmode is set to N")
    