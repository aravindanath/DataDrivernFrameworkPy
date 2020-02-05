'''
Created on 17-Apr-2019

@author: whizdom
'''
import pytest
    
@pytest.mark.run(order=1)    
def test_createLead():
    assert False
    
@pytest.mark.run(order=2) 
@pytest.mark.dependency(depends=["test_createLead"])     
def test_convertLead():
    assert True

@pytest.mark.run(order=3)
@pytest.mark.dependency(depends=["test_createLead" , "test_convertLead"])      
def test_deleteLeadAccount():
    assert True  