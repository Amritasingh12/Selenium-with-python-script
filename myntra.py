from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.myntra.com/")
driver.find_element_by_class_name("desktop-searchBar").send_keys("kurta")
ddelement.select_by_index(1)
#select.select_by_value('1')
