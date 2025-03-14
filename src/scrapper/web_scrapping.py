import requests
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

URL = "https://abe.web.geniussports.com/competitions/?WHurl=%2Fperson%2F2151822%2Fgamelog%3F"

options = Options()
options.add_argument("--headless")
driver = Chrome(options=options)
driver.get(URL)

stat_names = driver.find_elements(By.TAG_NAME, "tr")
headers = [stat_names[0].text]
data =[[stat_names[game].text] for game in range(1, len(stat_names))]

roi_stats = pd.DataFrame(data=data, columns=headers)
roi_stats.to_csv("../../data/raw/stats.csv", index=None)