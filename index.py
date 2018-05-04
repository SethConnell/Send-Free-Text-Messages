from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def SendText(yourname, message, recipientPhoneNumber):
    try:
        driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
        driver.get("http://www.24sms.net/")
        driver.find_element_by_name('SendFrom').send_keys(str(name))
        driver.find_element_by_name('SendTo').send_keys(str(recipientPhoneNumber))
        driver.find_element_by_name("Msg").send_keys(str(message))
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.close()
        driver.quit()
        return True
    except:
        return False
        
