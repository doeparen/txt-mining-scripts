import os
import re
import requests

# Function to extract URLs from the input file
def extract_urls(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Regular expression to find URLs within <url> </url> tags
    urls = re.findall(r'<url>(https://data\.riksdagen\.se/dataset/.+?)</url>', content)
    return urls

# Function to download files from the URLs and save them with the correct filename
def download_files(urls):
    for url in urls:
        # Extract the filename from the URL
        filename = url.split("/")[-1]
        print(f"Downloading {filename} from {url}")
        
        # Download the file
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Save the file to the current directory
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Saved {filename}")

# Main function to run the script
def main():
    input_file = 'input.txt'
    if not os.path.exists(input_file):
        print(f"{input_file} does not exist.")
        return
    
    # Extract URLs from the input file
    urls = extract_urls(input_file)
    
    if not urls:
        print("No URLs found in the input file.")
        return
    
    # Download the files from the URLs
    download_files(urls)

# Run the script
if __name__ == "__main__":
    main()
