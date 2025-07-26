# Videos_in_a_Playlist
# 🎥 YouTube Playlist Scraper (Selenium + BeautifulSoup)

This Python script extracts video links from a YouTube playlist by scraping `<a id="thumbnail">` elements using Selenium and BeautifulSoup.

YouTube dynamically renders content using JavaScript, so traditional HTTP-based scraping (like with `requests`) will not work. Selenium opens a real browser, waits for the page to load, and then extracts the video links.

---

## 🚀 Features

- Extracts all video links from a YouTube playlist
- Handles JavaScript-rendered content using Selenium
- Simple and customizable

---

## 📦 Requirements

Install the following dependencies:

```bash
pip install selenium beautifulsoup4
