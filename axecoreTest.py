#Requirements
import sys
from selenium import webdriver
from axe_selenium_python import Axe


def test_page():
    driver = webdriver.Chrome()
    driver.get("https://dequeuniversity.com/demo/mars")
    axe = Axe(driver)
    # Inject axe-core into page.
    axe.inject()
    # Run accessibility checks.
    results = axe.run()
    # Output results to terminal
    print(results)
    # Close driver
    driver.close()
    # Assert no violations are found
    assert len(results["violations"]) == 0, axe.report(results["violations"])
