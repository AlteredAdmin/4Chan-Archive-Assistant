import os
import requests
import basc_py4chan

# Constants
SAVE_DIRECTORY = os.path.join(os.path.expanduser('~'), '4chan')
URL_LOG_FILE = os.path.join(SAVE_DIRECTORY, 'url_log.txt')


def download_file(url, folder):
    """Downloads a file from the specified URL and saves it to the specified folder."""
    local_filename = os.path.join(folder, url.split('/')[-1])
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def download_from_thread(thread_url):
    """Downloads all files from a given 4chan thread URL."""
    board_name = thread_url.split('/')[3]
    thread_id = int(thread_url.split('/')[-1].split('.')[0])

    board = basc_py4chan.Board(board_name)
    thread = board.get_thread(thread_id)
    if not thread:
        print("Thread not found!")
        return

    title = thread.topic.subject if thread.topic.subject else ' '.join(thread.topic.text.split()[:5])
    folder_name = title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    full_save_path = os.path.join(SAVE_DIRECTORY, folder_name)

    if not os.path.exists(full_save_path):
        os.makedirs(full_save_path)

    for post in thread.all_posts:
        if post.has_file:
            download_file(post.file_url, full_save_path)
            print(f"Downloaded {post.file_url}")


def log_url_to_file(thread_url):
    """Logs the provided thread URL to a text file if it doesn't already exist."""
    if thread_url in get_urls_from_file():
        print(f"URL {thread_url} is already logged. Skipping.")
        return
    with open(URL_LOG_FILE, 'a') as file:
        file.write(thread_url + '\n')


def get_urls_from_file():
    """Retrieve all thread URLs from the log file."""
    if os.path.exists(URL_LOG_FILE):
        with open(URL_LOG_FILE, 'r') as file:
            return [url.strip() for url in file.readlines()]
    return []


if __name__ == "__main__":
    thread_url = input("Please enter the 4chan thread URL: ")
    process_from_log = False
    choice = input("Do you wish to read and process URLs from the log file? (yes/no): ").strip().lower()
    if choice == 'yes':
        process_from_log = True

    # Process the user-given URL first
    download_from_thread(thread_url)
    log_url_to_file(thread_url)

    if process_from_log:
        urls = get_urls_from_file()
        for url in urls:
            print(f"Processing URL from log file: {url}")
            download_from_thread(url)
