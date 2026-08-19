import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, backoff_factor=0.3):
    """
    Makes an HTTP GET request to the specified URL with retry logic.
    :param url: The URL to fetch.
    :param max_retries: Maximum number of retries allowed.
    :param backoff_factor: Factor by which to increase the wait time between retrials.
    :return: The response object if successful; else None.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < max_retries - 1:
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                print('Max retries reached. Exiting.')
                return None
    
def example_usage():
    url = 'https://api.example.com/data'
    response = retry_request(url)
    if response:
        print('Response received:', response.json())
    else:
        print('Failed to retrieve data.')

if __name__ == '__main__':
    example_usage()