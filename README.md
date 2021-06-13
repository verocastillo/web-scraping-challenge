# Mission to Mars! Advanced Web Scraping
<img width="1220" alt="ss1" src="https://user-images.githubusercontent.com/77795761/121796375-1f1b6780-cbde-11eb-8eff-d566ca4afb24.png">

In this repository, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Navigating Through The Repository

The structure of the repository is simple:

1. In the main repo page, you can find the jupyter notebook, the python files for the scrape function and the app.
2. In templates, you can find the html document, along with the css file for the styling.
3. In screenshots, you can find screenshots of the functioning application.

## What Does The App Do?

It scraps data from several pages in order to obtain relevant information regarding the Mission to Mars. It scrapes the Mars News Site to collect the latest News Title and Paragraph Text, it gets the url for the Featured Space Image, it gets information about Mars from the Mars Facts in form of a table, and finally, it obtains the names and image urls for each of the Mars Hemispheres.

## What Tools Were Used?
I used MongoDB with Flask templating to create the HTML page that displays all of the information that was scraped from the pages described above.
