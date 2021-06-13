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
    scrape_results['Most_Recent_Article_Title'] = first_news_title
    scrape_results['Most_Recent_Article_Text'] = first_news_text

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

    # Add to dictionary
    scrape_results['Featured_Image_URL'] = featured_image_url

    #
    # Mars Facts
    #

    # Setup url and browser
    marsfacts_url = 'https://galaxyfacts-mars.com'             
    browser.visit(marsfacts_url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Get table as DataFrame
    mars_facts = pd.read_html(marsfacts_url)[0]
    mars_facts.columns = ['Mars - Earth Comparison', 'Mars', 'Earth'] 
    mars_facts = mars_facts.iloc[1:]                              
    mars_facts.set_index('Mars - Earth Comparison', inplace=True)      
    mars_facts.head()

    # Export to html 
    table_mars = mars_facts.to_html()

    # Add to dictionary
    scrape_results['Facts_Table'] = table_mars

    #
    # Mars Hemispheres
    #

    # Setup url and browser
    marshemis_url = 'https://marshemispheres.com'             
    browser.visit(marshemis_url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Get image titles
    titles = []
    word = 'Hemisphere'
    titles_hem = soup.find_all('h3')
    for title in titles_hem:
        if word in title.text: 
            titles.append(title.text)

    # Get image urls
    imgurls = []
    ft_images = soup.find_all('img', class_='thumb')
    for img in ft_images:
        imgurls.append(f"{marshemis_url}/{img['src']}")
    
    # Create python dictionaries
    ce_hem = {'title': titles[0], 'img_url': imgurls[0]}
    sc_hem = {'title': titles[1], 'img_url': imgurls[1]}
    sy_hem = {'title': titles[2], 'img_url': imgurls[2]}
    va_hem = {'title': titles[3], 'img_url': imgurls[3]}

    # Append to list
    hemisphere_image_urls = [ce_hem,sc_hem,sy_hem,va_hem]

    # Add to dictionary
    scrape_results['Hemisphere_Info'] = hemisphere_image_urls

    #   Close browser
    browser.quit()

    print(scrape_results)
    
    return scrape_results

# Added so when file is ran, the function runs
if __name__ == "__main__":
    scrape()