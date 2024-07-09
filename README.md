# IEEE-data-scrapping


This project is a web scraper that extracts article names, links, authors, and their  country,institute or company from a list of URLs provided in a CSV file. The extracted data is saved into another CSV file named `rdfinal.csv`.

## Features

- **URL Parsing**: Reads a list of URLs from a CSV file.
- **Article Extraction**: Extracts article names and links from the provided URLs.
- **Author Extraction**: Navigates to each article link to extract author names.
- **Description Extraction**: Extracts author descriptions (including country and affiliation) from each author link.
- **Data Export**: Saves the extracted information into `rdfinal.csv`.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager

## Setup

### 1. Install Required Packages

Make sure you have Python installed on your system. Then, install the required packages using pip:
pip install selenium
pip install webdriver-manager

```bash
Ensure that the Chrome browser is installed on your system.
Adjust the sleep durations (time.sleep()) in the code if necessary, depending on the loading time of the web pages.
The extracted data will be saved in rdfinal.csv with the columns: Article Name, Article Link, Authors, and Author Descriptions.

```bash
pip install selenium
pip install webdriver-manager

```bash
pip install selenium

Ensure that the Chrome browser is installed on your system.
Adjust the sleep durations (time.sleep()) in the code if necessary, depending on the loading time of the web pages.
The extracted data will be saved in rdfinal.csv with the columns: Article Name, Article Link, Authors, and Author Descriptions.
pip install webdriver-manager
