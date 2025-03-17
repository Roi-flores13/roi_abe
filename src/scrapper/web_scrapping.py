import requests
import re
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

class Scrapper():
    
    def __init__(self, url:str):
        self.url = url
        options = Options()
        options.add_argument("--headless")
        self.driver = Chrome(options=options)
        self.driver.get(self.url)

    def __splitting_data(self, text) -> list:
        pattern = r"(\d{1,2} [A-Za-z]+\.? \d{4} \d{2}:\d{2})"
        match = re.search(pattern, text)
        
        if match:
            date = match.group(1)
            university_name = text[:match.start()].strip()
            numeric_values = text[match.end():].strip().split()
            
            return [university_name, date] + numeric_values
        
        else:
            return None

    def scrap_and_load(self) -> str:
        stat_names = self.driver.find_elements(By.TAG_NAME, "tr")
        headers = [stat for stat in stat_names[0].text.split()]
        data = [self.__splitting_data(stat_names[stat].text) for stat in range(1, len(stat_names))]   
        roi_stats = pd.DataFrame(data=data, columns=headers)
        roi_stats.to_csv("data/raw/stats.csv", index=None)
        print("Scrapping and loading done successfully!!")
        return "data/raw/stats.csv"