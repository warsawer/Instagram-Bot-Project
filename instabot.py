from pages import HomePage
from selenium import webdriver

browser = webdriver.Safari() # maybe change to the Firefox
browser.implicitly_wait(5) # set a 5 second delay. 
# # If Selenium cannot find an item, 
# it waits for everything to load and then tries again

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("username", "password")

browser.close()
