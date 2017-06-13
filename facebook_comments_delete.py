#!/bin/python

import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


driver = None


def load_driver():
    global driver
    driver = webdriver.Chrome()


def log_in(username, password):
    global driver
    counter = 0
    driver.get("https://m.facebook.com")
    username_elem = driver.find_element_by_name("email")
    username_elem.clear()
    username_elem.send_keys(username)
    password_elem = driver.find_element_by_name("pass")
    password_elem.clear()
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)
    time.sleep(2) # Adjust according to your Internet speed
    continue_link = driver.find_element_by_link_text('Not Now')
    continue_link.click()
    time.sleep(2)
    goto_profile_menu = driver.find_elements_by_class_name("_59tf")
    goto_profile_menu[5].click()
    time.sleep(2)
    goto_profile = driver.find_elements_by_class_name("_52x3")
    goto_profile[0].click()
    time.sleep(2)

    while True:
        try:
            delete_post_button_list = driver.find_element_by_class_name('_4s19')
            delete_post_button_list.click()
            time.sleep(2)
            drop_down_delete = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[2]/a[26]')
            drop_down_delete.click()
            time.sleep(2)
            final_delete_button = driver.find_element_by_xpath("//a[@title='Delete']")
            final_delete_button.click()
            time.sleep(2)
            counter =  counter + 1
            print("{} posts have been deleted".format(counter))
        except:
            print("Your posts have all been deleted.")

def click_to_profile():
    global driver


if __name__ == "__main__":
    username = ""
    password = ""
    # username = raw_input("Enter your Facebook username: ")
    # password = getpass.getpass("Enter your Facebook password: ")
    # target = raw_input("Enter the target's Facebook username: ")
    load_driver()
    log_in(username, password)
