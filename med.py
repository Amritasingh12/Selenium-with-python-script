from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://adminmed.fourbrick.in/adminLogin")
driver.find_element_by_name("user_name").send_keys("admin@admin.com")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("proced").click()
#source= driver.find_element_by_link_text('nav-link')
#action = ActionChains(driver)
#action.move_to_element(source).click().perform()
a = ActionChains(driver)
m = driver.find_element_by_class_name("menu-icon")
a.move_to_element(m).perform()
#continue_link = driver.find_element_by_link_text('nav-link')
#dropdown = Select(driver.find_element_by_class_name('nav-item active'))
#dropdown.select_by_value('All Drivers')
#dropdown.select_by_visible_text('All Drivers')
