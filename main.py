import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

from src.scrapper.web_scrapping import Scrapper

if __name__ == "__main__":
    URL = "https://abe.web.geniussports.com/competitions/?WHurl=%2Fperson%2F2151822%2Fgamelog%3F"
    sc = Scrapper(URL)
    print(sc.scrap_and_load())