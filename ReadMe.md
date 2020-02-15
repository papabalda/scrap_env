

Environment to deploy Scrappy spiders on scrapinghub. This project is intented to be educative about different things that can be accomplished with 
scrapy.


## Table of Contents

- [__Initializing Environment__](#initializing-environment)
- [__Creating Spiders__](#creating-spiders)
- [__Running Spiders__](#running-spiders)
- [__Folder Structure__](#folder-structure)
- [__Types of Crawlers__](#types-of-crawlers)
    - [__Basic Template__](#basic-template)
    - [__CrawlSpider__](#crawlspider)
    - [__Database Connected__](#database-connected)
- [__Tips__](#tips)

## Initializing Environment

Here's all the information regarding the proper setup and initialization
of the project.

- Clone scrap_env repository.
- Switch to `release` branch.
- Install Python3.
- Install pip3. `apt install python3-pip`
- Install Scrapy. `pip3 install Scrapy`

To get started with virtual environments, see virtualenv installation instructions. To install it globally (having it globally installed actually helps here), it should be a matter of running:

  $ [sudo] pip install virtualenv

Check this user guide on how to create your virtualenv https://virtualenv.pypa.io/en/stable/userguide/ 

## Creating Spiders
bla bla bla
start new spiders
scrapy genspider -t crawl spidername mydomain.com

## Running Spiders

To run the spiders via console, navigate to the `scrap_env` 
folder and use any of the commands written below.

##### commands

- Delimited by scraped items = `scrapy crawl spidername --set CLOSESPIDER_ITEMCOUNT=50`
- All = `scrapy crawl spidername`
- Generating json output = `scrapy crawl quotes -o quotes.json`
- Generating json lines output = `scrapy crawl quotes -o quotes.jl`


## Folder Structure

    scrap_env
          - scrap_env
                  - spiders
                          - __init__.py
                          - ExampleSpider1.py
                          - ExampleSpider2.py
                          - ... 
                  - __init__.py
                  - items.py
                  - middlewares.py
                  - pipelines.py
                  - settings.py
          .gitignore
          README.md
          scrapy.cfg

The structure remains the same as the one you get when creating a new scrapy project.

## Types of Crawlers

#### Basic Template

To be included
  
#### CrawlSpider

To be included

#### Database Connected

To be included

## Tips

To be included