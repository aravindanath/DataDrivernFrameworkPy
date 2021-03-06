from BaseTest import BaseTest
import pytest

@pytest.mark.run(order=2)
def test_b1():
    base = BaseTest()
    base.openBrowser("Chrome")
    base.navigate("url")
    base.getCountOfElements("//a")
    base.getLinks("//a")
    base.sleep(2)
    base.type("//input[@name='q']","selenium")
    base.sleep(2)

@pytest.mark.run(order=1)
def test_b3():
    base = BaseTest()
    base.OpenBrowser("Chrome")
    base.navigate("https://www.amazon.in")
    base.scrollTillEnd()
    base.sleep(2)
    base.getCountOfElements("//a")


