from selenium import webdriver
import time
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TOPIC = "srd98"

driverPath = os.path.abspath(PROJECT_ROOT+"/driver/chromedriver.exe")


driverChrome = webdriver.Chrome(driverPath)


driverChrome.set_page_load_timeout(10)
driverChrome.get("https://www.omegle.com/")
driverChrome.find_element_by_class_name("newtopicinput").send_keys(TOPIC)
driverChrome.find_element_by_id("textbtn").click()

time.sleep(1)



logsNumber = len(driverChrome.find_elements_by_class_name("logitem"))
print(logsNumber)

while (logsNumber == len(driverChrome.find_elements_by_class_name("logitem"))):
    print("Esperando")

while(True):
    logsNumber = len(driverChrome.find_elements_by_class_name("logitem"))
    while(logsNumber == len(driverChrome.find_elements_by_class_name("logitem")) or driverChrome.find_elements_by_class_name("logitem")[-1].text == "Stranger is typing..."):
        #if(driverChrome.find_elements_by_class_name("logitem")[-1].text == "Stranger is typing..."): continue
        #print(logsNumber,len(driverChrome.find_elements_by_class_name("logitem")) )
        #print(driverChrome.find_elements_by_class_name("logitem")[-1])
        #print(driverChrome.find_elements_by_class_name("logitem")[-1].text)
        time.sleep(1)
        
    driverChrome.find_element_by_class_name("chatmsg ").send_keys("Hola")
    driverChrome.find_element_by_class_name("sendbtn").click()
    print(logsNumber,len(driverChrome.find_elements_by_class_name("logitem")) )
    time.sleep(3)

