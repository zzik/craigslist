from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://altoona.craigslist.org/search/remote-jobs'

# Initialize the webdriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get(url)

# Wait for up to 10 seconds for the presence of the first "result-info" element
result_info_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'result-info'))
)

# Loop through each "result-info" element
for result_info in result_info_elements:
    try:
        # Try to find "supertitle" class text
        supertitle_element = result_info.find_element(By.CLASS_NAME, 'supertitle')
        supertitle_text = supertitle_element.text
    except:
        # Handle the case when "supertitle" doesn't exist
        supertitle_text = None

    # Extract information from "title-blob" element
    title_blob_element = result_info.find_element(By.CLASS_NAME, 'title-blob')
    a_tag = title_blob_element.find_element(By.TAG_NAME, 'a')
    href_attribute = a_tag.get_attribute('href')
    span_text = a_tag.find_element(By.TAG_NAME, 'span').text

    # Print the extracted information
    print('Supertitle:', supertitle_text)
    print('Title Blob Href:', href_attribute)
    print('Title Blob Span Text:', span_text)
    print('-' * 30)

# Close the browser
driver.quit()