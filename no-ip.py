from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
#chrome_options.add_argument("--headless") 
driver=Chrome(options=chrome_options)

 # Optional argument, if not specified will search path.
driver.get('https://www.noip.com/login')
print ("navegador lanzado")
username = driver.find_element_by_name("username")
username.clear()
#username.send_keys("pythonsendmailja@gmail.com")
username.send_keys("sirzatirtu@nedoz.com")
print ("usuario")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("python20")
print ("Contraseña")
#password.send_keys("IvanJA#2020")
driver.find_element_by_name("Login").click()
sleep (3)
driver.find_element_by_class_name("stat-panel").click()
print ("entrando en el panel de hosts")
sleep (3)
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/form/div[1]/button").click()
print ("creando hosts")
sleep(2)
hostname = driver.find_element_by_id("name")
sleep (1)
hostname.send_keys("fdksajflkasdj")
sleep (2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[4]/button[1]/div").click()
print ("host creado")
driver.quit()

//*[@id="host-panel"]/div[1]/div/form/div[1]/button
/html/body/div[1]/div/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/form/div[1]/button
document.querySelector("#host-panel > div.panel-heading.pull-left > div > form > div.text-right.pull-left.pb-20.pb-md-0 > button")