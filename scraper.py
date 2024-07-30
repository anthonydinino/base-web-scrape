from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures

def scrape(url):
  browser = get_browser(headless=False)
  browser.get(url)
  return {"data" : "selenium response data"}

def get_browser(headless=True):
  server = "http://selenium-hub:4444"
  options = webdriver.ChromeOptions()
  if headless:
    options.add_argument("--headless")
  return webdriver.Remote(options=options, command_executor=server)

