from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless") 
driver=Chrome(options=chrome_options)

 # Optional argument, if not specified will search path.
driver.get('https://www.noip.com/login')
print ("navegador lanzado")
username = driver.find_element_by_name("username")
username.clear()
username.send_keys("pythonsendmailja@gmail.com")
#username.send_keys("sirzatirtu@nedoz.com")
print ("usuario")
password = driver.find_element_by_name("password")
password.clear()
#password.send_keys("python20")
print ("Contraseña")
password.send_keys("IvanJA#2020")
driver.find_element_by_name("Login").click()
sleep (3)
driver.find_element_by_class_name("stat-panel").click()
print ("entrando en el panel de hosts")
sleep (1)
bttn=driver.find_elements_by_class_name("btn-labeled")
bttn[0].click()
sleep (1)
ipv4=driver.find_elements_by_class_name("form-control")
ipv4[4].clear()
ipv4[4].send_keys("3.3.3.3")
driver.find_element_by_class_name("btn.btn-170.btn-flat.btn-success.btn-round-corners.pr-sm.ml-sm-30").click()
print ("update hosts")

driver.quit ()