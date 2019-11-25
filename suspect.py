from selenium import webdriver
import time

TOPIC = "srd98"


driverChrome = webdriver.Chrome("C:/Users/pgr20192/Documents/AutoEnemy/driver/chromedriver.exe")

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
    while(logsNumber == len(driverChrome.find_elements_by_class_name("logitem"))):
        #if(driverChrome.find_elements_by_class_name("logitem")[-1].get)
        print(logsNumber,len(driverChrome.find_elements_by_class_name("logitem")) )
        #print("Esperando Respuesta")
    driverChrome.find_element_by_class_name("chatmsg ").send_keys("Hola")
    driverChrome.find_element_by_class_name("sendbtn").click()
    print(logsNumber,len(driverChrome.find_elements_by_class_name("logitem")) )
    time.sleep(1)



