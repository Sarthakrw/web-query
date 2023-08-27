import requests
from bs4 import BeautifulSoup
import re

def scraper(url):
  req = requests.get(url)
  soup = BeautifulSoup(req.content, "html.parser")
  context = soup.get_text()
  relevant_text = soup.get_text()
  cleaned_text = re.sub(r'\s+', ' ', relevant_text).strip()

  return cleaned_text