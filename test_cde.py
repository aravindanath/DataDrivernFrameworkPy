

import time
import allure
import logging
# from pytest_expectr.plugin import expect
from delayed_assert.delayed_assert import assert_expectations, expect

logger=logging.getLogger()
logger.setLevel(logging.INFO)
def test_a():
    with allure.step(" Screenshot added !!"):
    
        base = abc()
        base.OpenBrowser("Chrome")
        base.Navigate("URL")    
        expect(False,"kaka pagal hai")
        expect(False,"puri pagal hai")
        expect(False,"abhishek pagal hai")
        expect(False,"bedi pagal hai")
        expect(False,"riya pagal hai")
        expect(False,"chicken pagal hai")
        assert_expectations()
    
        if(not base.isElementPresent("email_xpath")) :
            base.ReportFail("Element is not present")
            
        if(not base.verifyText("signin_xpath" , "signinText")):
            base.ReportFail("Not verified")
  
        base.Type("email_xpath" , "email_id")
        time.sleep(5)
        base.Click("click_xpath")
        time.sleep(5)
        base.verifyText("signin_xpath", "signinText")
        base.ReportFail( "T4itle doesn't match")
        
def quit_test():
    try:
        assert_expectations()
         
    except Exception as capturedError:
        logger.error(capturedError)
        
        
