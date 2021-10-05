import requests

API_LINK = "https://www.amiiboapi.com/api/amiibo/"
REQUEST_ARG = "?name="


def get_bin_info(filename):
    amiibo_name = None  # populate at some point
    # get API info
    response = requests.get(f"{API_LINK}{REQUEST_ARG}{amiibo_name}")
    return response if response.status_code == 200 else None