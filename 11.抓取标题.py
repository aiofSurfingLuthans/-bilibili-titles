import requests
import csv
from lxml import html

MOVIE_LIST_FILE = "csv_data/bilibili_list.csv"
BILIBILI_BASE_URL = "https://www.bilibili.com/video/BV1sHU9BmEne"

def save_titles(titles):
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["标题"])
        for title in titles:
            writer.writerow([title])

def get_titles(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers, timeout=60)
    doc = html.fromstring(resp.text)
    titles = doc.xpath('//div[@class="title-txt"]/text()')
    return [t.strip() for t in titles if t.strip()]

def main():
    titles = get_titles(BILIBILI_BASE_URL)
    save_titles(titles)
    print(f"保存 {len(titles)} 个标题")

if __name__ == '__main__':
    main()