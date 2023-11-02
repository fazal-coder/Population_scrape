# Population Data Scraper

This Python script uses Selenium to scrape population data by country from the Worldometer website and stores it in an Excel file.

## Instructions

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Make sure you have Google Chrome installed and download the appropriate ChromeDriver executable for your system from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).

3. Edit the `webdriver_path` variable in the script to point to the location of the downloaded ChromeDriver executable.

4. Run the script. It will open a Chrome browser, scrape the data, and save it to an Excel file.

5. The scraped data will be saved in a file named `population_data.xlsx` in the same directory as the script.

## Requirements

- Python 3.x
- Chrome browser
- ChromeDriver executable (downloaded and specified in the script)

## Dependencies

- Selenium
- pandas

## Usage

```python
python population_scraper.py
