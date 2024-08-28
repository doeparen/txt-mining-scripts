import os
import zipfile

# Function to unzip all zip files in a specified folder
def unzip_all_files_in_folder(folder_path):
    # List all files in the directory
    files = os.listdir(folder_path)
    
    # Filter the list to include only .zip files
    zip_files = [file for file in files if file.endswith('.zip')]
    
    if not zip_files:
        print("No zip files found in the folder.")
        return
    
    for zip_file in zip_files:
        zip_file_path = os.path.join(folder_path, zip_file)
        
        # Define the extraction path (same name as the zip file, but without the .zip extension)
        extract_folder_name = os.path.splitext(zip_file)[0]
        extract_folder_path = os.path.join(folder_path, extract_folder_name)
        
        # Create the extraction directory if it doesn't exist
        if not os.path.exists(extract_folder_path):
            os.makedirs(extract_folder_path)
        
        # Unzip the file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder_path)
        
        print(f"Unzipped {zip_file} into {extract_folder_path}")

# Main function to run the script
def main():
    folder_path = '.'  # You can change this to the desired folder path
    unzip_all_files_in_folder(folder_path)

# Run the script
if __name__ == "__main__":
    main()
