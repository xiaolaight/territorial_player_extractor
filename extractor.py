from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
import pandas as pd

url = "https://territorial.io"

style_args = {

    "color" : "rgb(170, 170, 170)",
    "cursor" : "pointer",
    margin - top: 0.2em
    margin - right: 0.2em
    margin - bottom: 0.2em
    max - width: 9em
    width: 9em
    max - height: 1.4em
    height: 1.4em
    white-space-collapse: collapse
    text-wrap-mode: nowrap
    overflow-x: hidden
    overflow-y: hidden
    text-overflow: ellipsis
    font: inherit;
    display: inline - block

}

driver = webdriver.Chrome()
driver.get(url)
driver.find_elements_by_xpath("//*[contains(text(), 'Multiplayer')]").click()
soup = BeautifulSoup(driver.page_source, 'html.parser')
players = soup.find_all(attrs={})
