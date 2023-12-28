# interest rate differential
# Economic prospects for growth.
# Inflation or deflation rate and forecasts.
# Trade deficits or surpluses.
# The nation’s money supply.
# The nation’s credit rating.
# The security used to back the currency, if any.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_interest_rate(country):
    print(f"Getting interest rate of {country}...")

    country = country.capitalize()
    final_interest_rate = 0.0

    url = "https://tradingeconomics.com/country-list/interest-rate?continent=world"
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div/table[@class='table table-hover table-heatmap']")))
    except:
        print("Timeout (10 Seconds)")
        driver.quit()

    table_elements = table.find_elements(By.XPATH, "//tbody/tr")
    for index, row in enumerate(table_elements):
        country_name = row.find_element(By.TAG_NAME, "a").text
        country_interest_rate = row.find_element(By.XPATH, f"//td[@data-heatmap-value='{(0-index)}']").text
        # print(country_name)
        # print(country_interest_rate)
        if country_name.lower() == country.lower():
            final_interest_rate = country_interest_rate
        
    return final_interest_rate



def get_inflation_rate(country):
    print(f"Getting interest rate of {country}...")

    country = country.capitalize()
    final_inflation_rate = 0.0

    url = "https://tradingeconomics.com/country-list/inflation-rate?continent=world"
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div/table[@class='table table-hover table-heatmap']/tbody")))
    except:
        print("Timeout (10 Seconds)")
        driver.quit()

    input(">")

    table_elements = table.find_elements(by=By.XPATH, value="//tr[@class='datatable-row']")
    for index, row in enumerate(table_elements):
        country_name = row.find_element(By.TAG_NAME, "a").text
        country_inflation_rate = row.find_element(By.XPATH, f"//td[@data-heatmap-value='{(0-index)}']").text
        # print(country_name)
        # print(country_inflation_rate)
        if country_name.lower() == country.lower():
            final_inflation_rate = country_inflation_rate

    table_elements = table.find_elements(by=By.XPATH, value="//tr[@class='datatable-row-alternating']")
    for index, row in enumerate(table_elements):
        country_name = row.find_element(By.TAG_NAME, "a").text
        country_inflation_rate = row.find_element(By.XPATH, f"//td[@data-heatmap-value='{(0-index)}']").text
        # print(country_name)
        # print(country_inflation_rate)
        if country_name.lower() == country.lower():
            final_inflation_rate = country_inflation_rate

        return final_inflation_rate




if __name__ == "__main__":
    print("Please enter the country name:")
    country = input(">")

    int_rate = get_interest_rate(country)
    print(f"Interest Rate: {int_rate}")

    inf_rate = get_inflation_rate(country)
    print(f"Inflation Rate: {inf_rate}")
