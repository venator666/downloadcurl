#!/usr/bin/env python3
import sys
import os
import requests

def download_file(url, output_filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        with open(output_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded successfully as {output_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: downloadcurl <URL> <output_filename>")
        sys.exit(1)

    url = sys.argv[1]
    output_filename = sys.argv[2]
    download_file(url, output_filename)
