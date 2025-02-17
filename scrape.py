import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Remote, ChromeOptions  
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection  
from selenium.webdriver.common.by import By  
AUTH = 'Your Credentials from bigdata'  

SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'   
from bs4 import BeautifulSoup

def scrape_website(website):
    if not website:
        raise ValueError("Website URL cannot be empty")
        
    print("Launching chrome browser")
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
            with Remote(sbr_connection, options=ChromeOptions()) as driver:
                driver.get(website)
                # print('Taking page screenshot to file page.png')
                # driver.get_screenshot_as_file('./page.png')
                print('Navigated! Scraping page content...')
                
                # Wait for the page to load
                time.sleep(2)
                
                html = driver.page_source
                if not html:
                    raise ValueError("No HTML content retrieved")
                    
                return html
                
        except WebDriverException as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to scrape website after {max_retries} attempts: {str(e)}")
            print(f"Attempt {attempt + 1} failed, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

def extract_body_content(html_content):
    if not html_content or not isinstance(html_content, str):
        raise ValueError("Invalid HTML content provided")
        
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return "<body>No content found</body>"

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    clean_content = soup.get_text(separator="\n")
    clean_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )

    return clean_content

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]
