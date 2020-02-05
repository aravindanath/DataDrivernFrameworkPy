

import null

from pyjavaproperties import Properties
from selenium.webdriver import Chrome
import logging
import sys
import allure
from allure_commons.types import AttachmentType


class abc:
    global propAbhi
    global logger
    global driver

    def __init__(self):
        self.propAbhi = Properties()
        try:
            propertiesFile = open("./Files/Config.properties")
            self.propAbhi.load(propertiesFile)
            self.propAbhi.list()        
        except FileNotFoundError as e:
            print(e)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.driver = null
     
    def GetElement(self, locatorKey):
        e = null
        a = self.propAbhi[locatorKey]

        try:
            if(locatorKey.endswith("_id")):
                e = self.driver.find_element_by_id(a)
            
            elif(locatorKey.endswith("_name")):
                e = self.driver.find_element_by_name(a)
            
            elif(locatorKey.endswith("_xpath")):
                e = self.driver.find_element_by_xpath(a)
                
            else:
                self.ReportFail("Locator not correct")
                assert False ("Locator not correct")
            
            return e
        except Exception as ex:
            self.ReportFail(self, ex.message)
            print(ex)
            assert False
           
    def OpenBrowser(self, browserName):                                                                                                                                 

            print(self.propAbhi["email_xpath"])
            if(browserName == "Chrome"):
                path = "../driver/chromedriver"
                self.driver = Chrome(executable_path=path)

            elif (browserName == "Mozilla"):
                path = "../driver/geckodriver"
                self.driver = Chrome(executable_path=path)
                self.driver.implicitly_wait(5)
                self.driver.maximize_window()
             
    def Navigate(self, StringURL):
        a = self.propAbhi[StringURL]
        print(a)
        self.driver.get(a)
        pass
     
    def Type(self, StringXpath, StringData):
        a = self.propAbhi[StringXpath]
        print(a)
        b = self.propAbhi[StringData]
        print(b)
        self.driver.find_element_by_xpath(a).send_keys(b)
        pass
    
    def Click(self, locatorKey):
        self.GetElement(locatorKey).click()
        pass
            
    def verify_title(self):
        return False
    
    def isElementPresent(self, locatorKey):
        self.list = null
        a = self.propAbhi[locatorKey]
        if(locatorKey.endswith("_id")):
            self.list = self.driver.find_elements_by_id(a)
            
        elif(locatorKey.endswith("_name")):
            self.list = self.driver.find_elements_by_name(a)
            
        elif(locatorKey.endswith("_xpath")):
            self.list = self.driver.find_elements_by_xpath(a)


        else:
            self.ReportFail("Locator not correct")
            assert False ("Locator not correct")
        
        if (len(self.list) == 0):   
            return False
        else:
            return True
    
    def verifyText(self, locatorKey, expectedText):
        actualText = self.GetElement(locatorKey).text
        expectedText = self.propAbhi[expectedText]
        if(actualText == expectedText):
            return True
        else:
            return False
    
    def ReportPass(self, Stringmsg):
        
        pass
    
    def ReportFail(self, Stringmsg):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot of the screen" , AttachmentType.PNG)
        self.logger.error("Loading Element or element not found")
        assert True 
        
        
    def TakeScreenshot(self, Stringmsg):
        pass

      
class Child(abc): 
    pass      
    
