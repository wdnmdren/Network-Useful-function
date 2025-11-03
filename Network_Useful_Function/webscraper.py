import requests
from bs4 import BeautifulSoup
import logging
import time
import random
import csv
import pickle
import os

# Logging
LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "kardashian_problems.log")
logging.basicConfig(filename=LOG_FILE, encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 课程抓取
def get_course_titles_and_descriptions(source):
    if source.startswith("http"):
        html = requests.get(source).text
    else:
        html = source
    soup = BeautifulSoup(html, "html.parser")
    container = soup.find("div", class_="sc_sccoursedescs")
    if container is None:
        return {}
    courses_detail = {}
    for block in container.find_all("div", class_="courseblock"):
        title_tag = block.find("p", class_="courseblocktitle noindent")
        desc_tag = block.find("p", class_="cb_desc")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        desc = desc_tag.get_text(strip=True) if desc_tag else "No description"
        courses_detail[title] = desc
    return courses_detail

# Kardashian抓取
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "kardashian_jenner_urls_jan_1_2024_to_july_31_2024_mediacloud.csv")
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        urls = [line[-1] for line in reader][1:]
else:
    urls = []
    logger.warning(f"CSV file not found at {DATA_PATH}")

def get_people_in_article(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            logger.debug(f"HTTP {response.status_code} for {url}")
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        people = []
        for p_tag in soup.find_all("p"):
            for a_tag in p_tag.find_all("a", href=True):
                href = a_tag["href"]
                if "https://www.tmz.com/people" in href:
                    person = href.rstrip("/").split("/")[-1]
                    people.append(person)
        return people
    except requests.exceptions.RequestException as e:
        logger.debug(f"Request error {url}: {e}")
        return None

def collect_people_from_random_articles(sample_size=30, delay=7, output_pickle="lists_of_people.pkl"):
    if not urls:
        logger.error("URL list empty")
        return []
    lists_of_people = []
    sampled = random.sample(urls, min(sample_size, len(urls)))
    for url in sampled:
        lists_of_people.append(get_people_in_article(url))
        time.sleep(delay)
    pickle_path = os.path.join(os.path.dirname(__file__), "..", output_pickle)
    with open(pickle_path, "wb") as f:
        pickle.dump(lists_of_people, f)
    logger.info(f"Saved people lists to {pickle_path}")
    return lists_of_people
