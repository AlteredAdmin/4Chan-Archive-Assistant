# 4Chan Archive Assistant

`4ChanArchiveAssistant` is a Python-based utility that allows users to easily download and archive media content from 4chan threads. It offers features such as saving media content from a provided 4chan thread URL, logging thread URLs for future retrieval, and processing previously logged thread URLs.

## Features

- **Download Media**: The tool fetches all media content (images, videos, etc.) from the provided 4chan thread URL and saves it in a dedicated folder.
- **URL Logging**: All processed thread URLs are logged to avoid duplication and to serve as a record for future use.
- **Batch Processing**: The user can choose to process multiple threads from previously logged URLs in a single run.

## Requirements

- Python 3.x
- `requests`
- `basc_py4chan`

You can install the necessary libraries using:
```
pip install requests basc_py4chan
```

## Usage

1. Clone the repository or download the `4ChanArchiveAssistant.py` script.
2. Run the script:
   ```
   python 4ChanArchiveAssistant.py
   ```
3. Input the 4chan thread URL when prompted.
4. Choose whether to process previously logged URLs.

## How It Works

- On running the script, the user is prompted to input a 4chan thread URL.
- After providing the URL, the user is asked if they wish to process previously logged URLs.
- The script then downloads the content from the provided URL and logs it if it hasn't been logged before.
- If the user opts to process from the log, the script fetches and processes each logged URL sequentially.
