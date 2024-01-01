from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
import html

def test_xss(url):
    # Example of malicious JavaScript code
    xss_test_script = "<script>alert('XSS')</script>"

    # Encoding the malicious script for URL
    payload = quote(xss_test_script)

    # Creating the malicious URL
    malicious_url = f"{url}?name={payload}"

    # Setting up Chrome in headless mode
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Opening the malicious URL in the headless browser
    driver.get(malicious_url)

    # Extracting the page source from the browser and decoding HTML entities
    page_source = html.unescape(driver.page_source)

    print("Page source:")
    print(page_source)
    print("------------------------------------------")

    # Checking if the alert is present in the page source
    if xss_test_script in page_source:
        print("The page is vulnerable to XSS attacks!")
    else:
        print("The page seems to be safe.")

    # Closing the browser
    driver.quit()

# Use this function to test a specific URL
test_xss('http://127.0.0.1:8080')
