
# import logging
# from delayed_assert.delayed_assert import assert_expectations, expect
# from _overlapped import NULL
import time

import allure
import pytest

import DataUtil
from Base import abc
from ReadingData import XLReader
# from _overlapped import NULL
import null as NULL
testCaseName = NULL
readXLS = NULL


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
def test_a(dataRetrievedDictionary):
#     with allure.step(" Screenshot added !!"):  
        
#         base = abc()
#         if (DataUtil.isRunnable(testCaseName, readXLS) and dataRetrievedDictionary.get('Runmode') == "Y"):
#             base.OpenBrowser("Chrome")
#             base.Navigate("URL")
#             if(not base.isElementPresent("email_xpath")) :
#                 base.ReportFail("Element is not present")        
#             if(not base.verifyText("signin_xpath" , "signinText")):
#                 base.ReportFail("Not verified")
#             base.Type("email_xpath" , "email_id")
#             time.sleep(5)
#             base.Click("click_xpath")
#             time.sleep(5)
#             base.verifyText("signin_xpath", "signinText")
#             base.ReportFail("Title doesn't match")
            print(dataRetrievedDictionary.get("FirstName"), dataRetrievedDictionary.get("LastName"))
#         else:
            print("Runmode is set to N")
#             pytest.skip("Runmode is set to N")
        
########################################################################################################################
# from pytest_expectr.plugin import expect
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# def quit_test():
#     
#     with allure.step(" Screenshot added !!"):  
#         
#         base = abc()
#         if (dataRetrievedDictionary.get('Runmode') == "N"): 
#         base.OpenBrowser("Chrome")
#         base.Navigate("URL")    
#         expect(False,"kaka pagal hai")
#         expect(False,"puri pagal hai")
#         expect(False,"abhishek pagal hai")
#         expect(False,"bedi pagal hai")
#         expect(False,"riya pagal hai")
#         expect(False,"chicken pagal hai")
#         assert_expectations()
#             
#         if(not base.isElementPresent("email_xpath")) :
#             base.ReportFail("Element is not present")
#                     
#         if(not base.verifyText("signin_xpath" , "signinText")):
#             base.ReportFail("Not verified")
#           
#             base.Type("email_xpath" , "email_id")
#             time.sleep(5)
#             base.Click("click_xpath")
#             time.sleep(5)
#             base.verifyText("signin_xpath", "signinText")
#             base.ReportFail( "T4itle doesn't match")                    
#     print(dataRetrievedDictionary[0].get("Runmode"))
#             expect(False, "kaka pagal hai")
#             expect(False, "puri pagal hai")
#             expect(False, "abhishek pagal hai")
#             expect(False, "bedi pagal hai")
#             expect(False, "riya pagal hai")
#             expect(False, "chicken pagal hai")
#             assert_expectations()
#######################################################################################################################            