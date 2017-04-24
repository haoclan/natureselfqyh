from selenium import webdriver
print('hello, world')
browser = webdriver.Chrome()  #Firefox Chrome
browser.get("http://www.google.com/xhtml")
browser.quit()

