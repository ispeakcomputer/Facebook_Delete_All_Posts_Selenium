#!/bin/python

import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


driver = None


def load_driver():
	global driver
	chromedriver = os.path.abspath("./chromedriver")
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)


def log_in(username, password):
	global driver
	driver.get("https://m.facebook.com")
	username_elem = driver.find_element_by_name("email")
	username_elem.clear()
	username_elem.send_keys(username)
	password_elem = driver.find_element_by_name("pass")
	password_elem.clear()
	password_elem.send_keys(password)
	password_elem.send_keys(Keys.RETURN)
	time.sleep(3) # Adjust according to your Internet speed

if __name__ == "__main__":
	username = raw_input("Enter your Facebook username: ")
	password = getpass.getpass("Enter your Facebook password: ")
	target = raw_input("Enter the target's Facebook username: ")
	load_driver()
	log_in(username, password)
