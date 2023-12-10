from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Function to scrape articles from a given category
def scrape_articles(driver, category):
    print(f"\nScraping articles from {category}:\n{'='*30}")
    
    # Navigate to the category page
    driver.get(f'https://www.hindustantimes.com/{category.lower().replace(" ", "-")}/')
    
    # Wait for the content to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'hdg3')))
    
    # Extract article links and titles
    article_elements = driver.find_elements(By.CSS_SELECTOR, '.hdg3 a')
    article_data = [(element.get_attribute('href'), element.text.strip()) for element in article_elements]
    
    articles_data = []
    for idx, (article_link, article_title) in enumerate(article_data, 1):
        # Click on the article link to access the individual page
        driver.get(article_link)
        
        try:
            # Wait for the article content to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'storyDetails')))
            
            # Get the article text within the specified class and its descendants
            detail_elements = driver.find_elements(By.CLASS_NAME, 'detail')
            article_text = ""
            for detail_element in detail_elements:
                paragraphs = detail_element.find_elements(By.TAG_NAME, 'p')
                for paragraph in paragraphs:
                    article_text += paragraph.text.strip() + "\n"
            
            articles_data.append({
                'Category': category,
                'Article_Title': article_title,
                'Article_Link': article_link,
                'Article_Text': article_text
            })
            
            print(f"{idx}. {article_title}\n   Article Link: {article_link}\n   Text: {article_text}.")
        
        except Exception as e:
            print(f"Error scraping article {article_title}: {str(e)}")
        
        finally:
            # Go back to the category page for the next iteration
            driver.execute_script("window.history.go(-1)")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'hdg3')))
    
    return articles_data

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Specify the desired categories
categories = ['INDIA NEWS', 'LIFESTYLE',
    'ENTERTAINMENT', 'CRICKET', 'EDUCATION',
    'WORLD NEWS', 'SPORTS', 'SCIENCE', 'WEATHER'
]


all_articles_data = []
for category in categories:
    try:
        category_articles_data = scrape_articles(driver, category)
        all_articles_data.extend(category_articles_data)
    except Exception as e:
        print(f"Error scraping articles from {category}: {str(e)}")

# Create a DataFrame from the collected data
df = pd.DataFrame(all_articles_data)

# Create a folder to store the scraped data
folder_path = 'scraped_data'
os.makedirs(folder_path, exist_ok=True)

# Save the DataFrame to a CSV file in the folder
csv_path = os.path.join(folder_path, 'classified_articles_data.csv')
df.to_csv(csv_path, index=False)

# Print the DataFrame for verification
print("\nDataFrame:")
print(df)

# Close the browser
driver.quit()