from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

browser_options = Options()
webdriver_path = r'path\to\chromedriver.exe' # Mention Here Chrome Driver path
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=browser_options)
url = 'https://www.worldometers.info/world-population/population-by-country/'
driver.get(url)

# Initialize a list to store the table data
table_data = []

rows = driver.find_elements(By.XPATH, '//*[@id="example2"]/tbody/tr')

for row in rows:
    columns = row.find_elements(By.TAG_NAME, 'td')

    # Extract data from each column and convert to text
    country = columns[1].find_element(By.TAG_NAME, 'a').text
    population = columns[2].text
    yearly_change = columns[3].text
    net_change = columns[4].text
    density = columns[5].text
    land_area = columns[6].text
    migrants = columns[7].text

    # Append the extracted data as a list to table_data
    table_data.append([country, population, yearly_change,
                      net_change, density, land_area, migrants])

#table header
headers = ["Country", "Population", "Yearly Change",
           "Net Change", "Density", "Land Area", "Migrants"]


# DataFrame
df = pd.DataFrame(table_data, columns=headers)

# Export the DataFrame to an Excel filecls
df.to_excel('population_data.xlsx', index=False)

# Close the Selenium WebDriver
driver.quit()

print("Data saved to population_data.xlsx")
