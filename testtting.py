from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

def setup_driver():
    # Setup the Chrome driver using webdriver_manager
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def load_urls_from_csv(file_path):
    # Open the CSV file containing URLs
    with open(file_path, mode='r', encoding='utf-8') as url_file:
        url_reader = csv.reader(url_file)
        next(url_reader)  # Skip header row if it exists
        return [row[0] for row in url_reader if row]

def extract_articles(driver, url):
    driver.get(url)
    time.sleep(5)  # Adjust if necessary

    # Extract article names and links
    article_elements = driver.find_elements(By.XPATH, '//*[@id="publicationIssueMainContent global-margin-px"]//h2/a')
    return [(article.text, article.get_attribute('href')) for article in article_elements]

def extract_authors(driver, article_link):
    driver.get(article_link)
    time.sleep(5)  # Adjust if necessary

    # Extract author names
    authors_element = driver.find_element(By.CLASS_NAME, 'authors-container')
    author_elements = authors_element.find_elements(By.TAG_NAME, 'a')
    author_names = [author.text for author in author_elements]
    authors_combined = ', '.join(author_names)

    # Extract author links
    browse_pub_tab_elements = driver.find_elements(By.CSS_SELECTOR, '#document-tabs > div:nth-child(3) a')
    author_links = [element.get_attribute('href') for element in browse_pub_tab_elements]

    author_descriptions = extract_author_descriptions(driver, author_links)
    author_descriptions_combined = ' '.join(author_descriptions)

    return authors_combined, author_descriptions_combined

def extract_author_descriptions(driver, author_links):
    author_descriptions = []

    for link in author_links:
        driver.get(link)
        time.sleep(3)  # Wait for the author's page to load

        # Extract the author's description using the provided XPath
        description_elements = driver.find_elements(By.XPATH, '//*[@id="authors"]/div[1]/xpl-author-item/div/div[1]/div[2]/div[2]/div')
        descriptions = [element.text for element in description_elements]
        author_descriptions.extend(descriptions)
    
    return author_descriptions

def save_to_csv(file_path, data):
    # Save the data to a CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as final_file:
        writer = csv.writer(final_file)
        writer.writerow(['Article Name', 'Article Link', 'Authors', 'Author Descriptions'])
        for row in data:
            writer.writerow(row)

def main():
    driver = setup_driver()
    urls = load_urls_from_csv('url_list.csv')
    final_data = []

    try:
        for url in urls:
            print(f"Processing URL: {url}")
            articles = extract_articles(driver, url)
            if not articles:
                print(f"No articles found on page: {url}")
                continue
            
            for article_name, article_link in articles:
                try:
                    authors_combined, author_descriptions_combined = extract_authors(driver, article_link)
                    final_data.append([article_name, article_link, authors_combined, author_descriptions_combined])
                except Exception as e:
                    print(f"Error extracting authors from {article_link}: {e}")

        save_to_csv('rdfinal.csv', final_data)
        print("Data saved to rdfinal.csv")

    except Exception as e:
        print(f"Error processing URL list: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
