# coding = utf-8
#   http://chromedriver.storage.googleapis.com/index.html    谷歌驱动
#   https://github.com/mozilla/geckodriver/releases     火狐驱动

from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

browser.quit()