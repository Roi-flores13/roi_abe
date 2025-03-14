import requests
import re
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
headers = [stat for stat in stat_names[0].text.split()]

def splitting_data(text):
    pattern = r"(\d{1,2} [A-Za-z]+\.? \d{4} \d{2}:\d{2})"
    match = re.search(pattern, text)
    
    if match:
        date = match.group(1)
        university_name = text[:match.start()].strip()
        numeric_values = text[match.end():].strip().split()
        
        return [university_name, date] + numeric_values
    
    else:
        return None

data = [splitting_data(stat_names[stat].text) for stat in range(1, len(stat_names))]    

roi_stats = pd.DataFrame(data=data, columns=headers)
roi_stats.to_csv("../../data/raw/stats.csv", index=None)
