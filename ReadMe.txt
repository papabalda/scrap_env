Environment to deploy Scrappy spiders on scrapinghub


sudo apt install python3-pip
pip3 install Scrapy

To get started with virtual environments, see virtualenv installation instructions. To install it globally (having it globally installed actually helps here), it should be a matter of running:

$ [sudo] pip install virtualenv
Check this user guide on how to create your virtualenv https://virtualenv.pypa.io/en/stable/userguide/ 

to generate json
scrapy crawl quotes -o quotes.json
JSON Lines
scrapy crawl quotes -o quotes.jl