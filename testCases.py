#Requirements
import sys
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://dequeuniversity.com/demo/mars")


# Test 1
try:
    driver.find_elements_by_css_selector("main-nav")
    print("Test 1 Passed")
except:
    print("Test 1 Failed")


# Test 2
try:
    if ((len(driver.find_elements_by_class_name("span-half left left-first"))) == 3) and ((len(driver.find_elements_by_class_name("span-half right left-first pull-right"))) == 2):
    print("Test 2 Passed")
except:
    print("Test 2 Failed")


# Test 3
try:
    driver.find_element_by_class_name("add-travler").click()
    driver.wait(10)
    if driver.find_element_by_id("traveler1"):
        print("Test 3 Passed")
except:
    print("Test 3 Failed")


# Test 4
try:
    vidTitle0 = driver.find_element_by_id("video-text").text
    driver.find_element_by_class_name("vid-prev icon-video-left-arrow").click()
    vidTitle1 = driver.find_element_by_id("video-text").text
    driver.refresh
    driver.find_element_by_class_name("vid-next icon-video-right-arrow").click()
    vidTitle2 = driver.find_element_by_id("video-text").text
    if (vidTitle0 != vidTitle1) and (vidTitle0 != vidTitle2):
        print("Test 4 Passed")
except:
    print("Test 4 Failed")


# Close Driver
driver.close()
