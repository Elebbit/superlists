from selenium import webdriver

browser = webdriver.Chrome("/users/taek2/desktop/chromedriver")
browser.get('http://localhost:8000')

assert 'Django' in browser.title