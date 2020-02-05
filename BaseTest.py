

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import logging
from pyjavaproperties import Properties
from faker import Faker


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class BaseTest():

    global driver 
    global prop
    global fake

    # Constructor
    def __init__(self):
        self.prop=Properties()
        try:
            propertiesFile = open("../Files/Config.properties",'r')
            self.prop.load(propertiesFile)
            self.prop.list()
        except FileNotFoundError as e:
             print(e)


    def openBrowser(self,browserName):
        if(browserName == "Chrome"):
            p=self.prop["chromePath"]
            self.driver = webdriver.Chrome(executable_path=p)
        elif browserName == "Firefox":
            self.driver = webdriver.Firefox(executable_path="../driver/geckdriver")
        self.driver.implicitly_wait(5)
        self.driver.fullscreen_window()


    def navigate(self,stringUrl):
        a= self.prop[stringUrl]
        self.driver.get(a)

    def type(self,stringXapth,stringData):
        self.driver.find_element_by_xpath(stringXapth).send_keys(stringData)

    def Type(self, StringXpath, StringData):
            a = self.prop[StringXpath]
            print(a)
            b = self.prop[StringData]
            print(b)
            self.driver.find_element_by_xpath(a).send_keys(b)
            pass



    def click(self,stringXpath):
        self.driver.find_element_by_xpath(stringXpath).click()

    def sleep(self,sec):
        time.sleep(sec)

    def mouseHover(self,tgtElement):
        act = ActionChains(driver)
        act.move_to_element(self,tgtElement).perform()

    def dragDrop(self,srcElement,tgtElement):
        act = ActionChains(driver)
        act.drag_and_drop(self,srcElement,tgtElement).perform()

    def takeScreenShot(self,filename=".png"):
        self.driver.save_screenshot(self,filename=filename)


    def selectByVisibleTest(self,element,text):
        sel = Select(element)
        sel.select_by_visible_text(self,text)

    def scrollByPixcel(self, driver, pixcel):
        driver.execute_script("window.scrollBy(0," + pixcel + ")", "")

    def scrollByElement(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def scrollTillEnd(self, driver):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def colourElement(self, driver, element, colour="yellow"):
        driver.execute_script("arguments[0].style.border = '3px solid " + colour + "'", element)


    def getCountOfElements(self,element):
        listOfElements = self.driver.find_elements(By.XPATH,element)
        print("No of elements: "+ str(len(listOfElements)))
        logger.info("No of elements: "+ str(len(listOfElements)))
        for li in listOfElements:
            print(li.text)


    def getLinks(self,element):
        listOfElements = self.driver.find_elements(By.XPATH,element)
        print("No of elements: "+ str(len(listOfElements)))
        for li in listOfElements:
            print(li.text + "---> ", li.get_attribute("href"))


    def getFullName(self):
        fake = Faker()
        return fake.name()

    def getAddress(self):
        fake = Faker()
        return fake.address()

    def getFakeText(self):
        fake = Faker()
        return fake.text()

    def selectByVisbleText(self,element,text):
        ele = self.driver.find_element(By.XPATH, element)
        sel =Select(ele)
        sel.select_by_visible_text(text)