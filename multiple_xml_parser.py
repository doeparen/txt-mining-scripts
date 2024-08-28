import xml.etree.ElementTree as ET
import requests
import os

# Define a function to extract URLs from the XML text
def extract_urls(text):
    import re
    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return url_pattern.findall(text)

# Function to download the content from a URL
def download_content(url, folder='downloads'):
    # Ensure the downloads folder exists
    os.makedirs(folder, exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Create a file name from the URL
        file_name = os.path.join(folder, url.split('/')[-1])
        
        # Write content to file
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {url} -> {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Parse the XML file
def parse_xml_and_download(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Iterate over all elements in the XML
    for elem in root.iter():
        # Check if element has text and extract URLs
        if elem.text:
            urls = extract_urls(elem.text)
            for url in urls:
                download_content(url)

# Main function
if __name__ == "__main__":
    xml_file_path = "input.xml"  # Replace with your XML file path
    parse_xml_and_download(xml_file_path)
