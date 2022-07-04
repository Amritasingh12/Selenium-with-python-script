from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://admin.ambulanceme.com/adminLogin")
driver.find_element_by_name("user_name").send_keys("admin@admin.com")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("proced").click()
