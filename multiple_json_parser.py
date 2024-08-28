import json
import requests
import os

# Define a function to download content from a URL
def download_content(url, folder='downloads'):
    # Ensure the downloads folder exists
    os.makedirs(folder, exist_ok=True)

    # Handle relative URLs (assuming HTTP protocol)
    if url.startswith("//"):
        url = "https:" + url

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

# Function to parse the JSON file and download URLs
def parse_json_and_download(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Loop through each document in the JSON structure
        documents = data.get('dokumentlista', {}).get('dokument', [])
        for document in documents:
            # Extract URLs
            url_text = document.get('dokument_url_text')
            url_html = document.get('dokument_url_html')

            # Download content if URLs are available
            if url_text:
                download_content(url_text)
            if url_html:
                download_content(url_html)

# Main function
if __name__ == "__main__":
    json_file_path = "input.json"  # Replace with your JSON file path
    parse_json_and_download(json_file_path)
