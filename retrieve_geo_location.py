def get_gps_location(address, key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': address, 'key': key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            location = results[0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None
  
