# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Scrape function
def scrape():
    scrape_results = {}

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #
    # NASA Mars News
    #

    # Setup url and browser
    marsnews_url = 'https://redplanetscience.com'             
    browser.visit(marsnews_url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Collect latest news title
    news_title = soup.find_all('div', class_='content_title')
    first_news_title = news_title[0].text
    # Collect first paragraph text
    news_text = soup.find_all('div', class_='article_teaser_body')
    first_news_text = news_text[0].text

    # Add to dictionary
    scrape_results['Most Recent Article Title'] = first_news_title
    scrape_results['Most Recent Article Text'] = first_news_text

    #
    # JPL Mars Space Images - Featured Image
    #

    # Setup url and browser
    marspic_url = 'https://spaceimages-mars.com'             
    browser.visit(marspic_url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Collect image
    ft_image = soup.find_all('img', class_='headerimage fade-in')
    ft_image_url = ft_image[0]['src']
    featured_image_url = f"{marspic_url}/{ft_image_url}"
    print(featured_image_url)

    # Add to dictionary

    #
    # Mars Facts
    #

    #
    # Mars Hemispheres
    #

    #   Close browser
    browser.quit()

    print(scrape_results)
    
    return scrape_results

# Added so when file is ran, the function runs
if __name__ == "__main__":
    scrape()