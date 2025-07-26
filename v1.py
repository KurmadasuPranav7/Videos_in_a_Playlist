from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/playlist?list=PLBlnK6fEyqRiyryTrbKHX1Sh9luYI0dhX")

driver.implicitly_wait(5)

soup = BeautifulSoup(driver.page_source, "html.parser")
thumbnails = soup.find_all("a", id="thumbnail")

for thumb in thumbnails:
    href = thumb.get("href")
    print(f"Video Link :", f"https://www.youtube.com{href}")

driver.quit()
