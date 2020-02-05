import BaseTest
from Base import abc
import pytest

@pytest.mark.run(order=2)
def test_b2():
    base = BaseTest()
    base.OpenBrowser("Chrome")
    base.navigate("url")
    if(not base.isElementPresent("email_xpath")):
        base.ReportFail("Element  not found")
    base.type("email_xpath","selenium")
    base.sleep(2)
    base.getCountOfElements("//a")

@pytest.mark.run(order=1)
def test_b3():
    base = BaseTest()
    base.OpenBrowser("Chrome")
    base.navigate("https://www.amazon.in")
    base.scrollTillEnd()
    base.sleep(2)
    base.getCountOfElements("//a")

