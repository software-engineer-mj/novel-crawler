from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

with open("config.json", "r") as common:
    config = json.load(common)

chrome_options = Options()
chrome_options.add_argument("--window-size=10000, 10000")
driver = webdriver.Chrome(executable_path="bin/driver_" + config["operating_system"], chrome_options=chrome_options)

for genre in config["genres"]:
    # 해당 웹 사이트 이동
    driver.get(config["website_url"])
    time.sleep(3)

    # 장르 메뉴 버튼 클릭
    menu_button = driver.find_element_by_class_name("trigger-genres")
    menu_button.click()
    time.sleep(3)

    menus = driver.find_element_by_id("NAV-GENRES")
    genre_button = menus.find_element_by_link_text(genre)
    genre_button.click()
    time.sleep(3)

    novel = driver.find_element_by_css_selector("#SECTION-LIST ul li a.title")
    novel.click()
    time.sleep(3)

    title = driver.find_element_by_css_selector("td.subject a")
    file_name = title.text
    title.click()
    time.sleep(3)

    novel_file = open("novels/" + file_name + ".txt", "w")
    lines = driver.find_elements_by_css_selector(".tcontent p")
    for line in lines:
        novel_file.write(line.text + "\n")
    novel_file.close()
