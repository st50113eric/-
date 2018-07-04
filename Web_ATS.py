import sys
import time
import string
from selenium import webdriver

test_url = "http://192.168.2.161/"
login_account = "admin"
login_password = "admin"

chrome_driver_path = "./chromedriver.exe"
chrome_web = webdriver.Chrome(chrome_driver_path) 
chrome_web.get(test_url)
time.sleep(5)

try:
    # Login page
    username = chrome_web.find_element_by_name("luci_username")
    username.clear()
    username.send_keys(login_account)

    password = chrome_web.find_element_by_name("luci_password")
    password.clear()
    password.send_keys(login_password)

    login_bt = chrome_web.find_element_by_css_selector("input.cbi-button.cbi-button-apply")
    login_bt.click()

    time.sleep(5)

    # Status page
    Status_tables = chrome_web.find_elements_by_tag_name("table")
    
    for Status_table in Status_tables:
        status = Status_table.find_elements_by_tag_name("tr")

        for row in status:
            cols = row.find_elements_by_tag_name("td")

            if "Firmware Version" in cols[0].text:
                print "DUT Firmware Version: " + cols[1].text
                break
            
            # Print data from each row
            #line = []
            #for col in cols:
            #    line.append(col.text)    
            #print "\t".join(line)
        break

    # Enter "SON>Firmware" page
    chrome_web.find_element_by_partial_link_text('SON').click()
    time.sleep(1)
    chrome_web.find_element_by_partial_link_text('Firmware').click()
    
    time.sleep(10)
except:     
    print("Unexpected error:" + str(sys.exc_info()[0]))

finally:
    print("Test finished!")
    chrome_web.quit()
