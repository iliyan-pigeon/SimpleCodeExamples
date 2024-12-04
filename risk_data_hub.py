import requests


def retrieve_jwt_token(api_key, key):

    # URL for obtaining the JWT token
    url = "https://drmkc.jrc.ec.europa.eu/risk-data-hub-api/gen_token"

    # Parameters for the API ke
    params = {
        "key": key
    }

    # Headers containing the API key
    headers = {
        "apikey": api_key
    }

    # Making a GET request to retrieve the JWT token
    response = requests.get(url, headers=headers, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Printing the raw response text
        print("JWT Token:", response.text)
        return response.text
    else:
        # Printing the error if the request failed
        print("Failed to retrieve JWT Token:", response.status_code, response.text)


def get_administrative_division(jwt_token, lat, lon, bbox_size=0.0):

    url = "https://drmkc.jrc.ec.europa.eu/risk-data-hub-api/collections/admin/division/items"
    bbox = f"{lon - bbox_size},{lat - bbox_size},{lon + bbox_size},{lat + bbox_size}"

    headers = {"Authorization": f"Bearer {jwt_token}"}
    params = {"f": "json", "bbox": bbox, "limit": 10}

    response = requests.get(url, headers=headers, params=params)

    print(response.json()["features"][0]["properties"])

    return response.json()["features"][0]["properties"]["admin_unit_code"]


def fetch_data_vulnerability(jwt_token, lat, lon, admin_unit_code, bbox_size=0.1):
    base_url = "https://drmkc.jrc.ec.europa.eu/risk-data-hub-api/collections/risks/vulnerability/items"
    bbox = f"{lon - bbox_size},{lat - bbox_size},{lon + bbox_size},{lat + bbox_size}"

    print(bbox)
    headers = {"Authorization": f"Bearer {jwt_token}"}
    params = {"f": "json",
              "limit": 10,
              "admin_unit_code": admin_unit_code,}
    print(params)
    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=30)
        print(response.json())
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    return response


def fetch_data_asset(jwt_token, lat, lon, admin_unit_code, bbox_size=0.1):
    url = "https://drmkc.jrc.ec.europa.eu/risk-data-hub-api/collections/admin/asset/items"
    bbox = f"{lon - bbox_size},{lat - bbox_size},{lon + bbox_size},{lat + bbox_size}"

    headers = {"Authorization": f"Bearer {jwt_token}"}
    params = {"f": "json",
              "limit": 10,
              "admin_unit_code": admin_unit_code, }

    response = requests.get(url, headers=headers, params=params)

    print(response.text)
    return response.json()


def fetch_data_losses(jwt_token, lat, lon, admin_unit_code, bbox_size=0.1):
    url = "https://drmkc.jrc.ec.europa.eu/risk-data-hub-api/collections/losses/losses/items"
    bbox = f"{lon - bbox_size},{lat - bbox_size},{lon + bbox_size},{lat + bbox_size}"

    headers = {"Authorization": f"Bearer {jwt_token}"}
    params = {"f": "json",
              "limit": 10,
              "admin_unit_code": admin_unit_code, }

    response = requests.get(url, headers=headers, params=params)

    print(response.text)
    return response.json()

