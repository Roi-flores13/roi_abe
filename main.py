from src.preprocessing.data_cleaning import preprocessing
from src.scrapper.web_scrapping import Scrapper

def scrapping(URL_path):
    sc = Scrapper(URL_path)
    raw_path = sc.scrap_and_load()
    return raw_path
    
if __name__ == "__main__":
    URL = "https://abe.web.geniussports.com/competitions/?WHurl=%2Fperson%2F2151822%2Fgamelog%3F"
    path = scrapping(URL)
    preprocessing(path)