import requests
import os

# Base URL for fetching the dataset metadata
metadata_url = "https://decision.cs.taltech.ee/electricity/api/"

# Base URL for downloading the CSV files
csv_base_url = "https://decision.cs.taltech.ee/electricity/data/"

# Directory to save downloaded CSV files
save_directory = "./csv_files/"

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

def fetch_metadata():
    """Fetch the metadata JSON that contains the dataset hashes"""
    try:
        response = requests.get(metadata_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Return the metadata in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch metadata: {e}")
        return []

def download_csv(hash_code):
    """Download a CSV file using the provided hash"""
    try:
        # Construct the full URL to the CSV file
        csv_url = f"{csv_base_url}{hash_code}.csv"
        
        # Send the request to download the CSV file
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Save the file to the local directory
        file_path = os.path.join(save_directory, f"{hash_code}.csv")
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {hash_code}: {e}")

def main():
    """Main function to handle the downloading process"""
    # Step 1: Fetch metadata
    metadata = fetch_metadata()
    
    # Step 2: Extract the dataset hashes from the metadata
    for dataset in metadata:
        hash_code = dataset.get("dataset")  # Extract the hash of each dataset
        if hash_code:
            print(f"Found dataset: {hash_code} - Downloading...")
            # Step 3: Download the corresponding CSV file
            download_csv(hash_code)
        else:
            print("No hash found for a dataset.")

# Run the main function
if __name__ == "__main__":
    main()
