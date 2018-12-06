import requests

# API
API_DOCUMENTATION_URL = "https://docs.co2signal.com/"
API_BASE_URL = "https://api.co2signal.com/v1/"
API_ENDPOINTS = {"latest_country_code": API_BASE_URL + "latest?countryCode={country_code}",
                 "latest_coordinates": API_BASE_URL + "latest?lon={longitude}&lat={latitude}",
                 }


def get_latest(token, country_code = None, latitude = None, longitude = None):
    """Get latest data from the APIs.
    :param token: the token as received from co2signal.com.
    :param country_code: (optional) the country code of the country (either the country code or both coordinates should
                         be given.
    :param latitude: (optional) the latitude of the location (either the country code or both coordinates should
                     be given.
    :param longitude: (optional) the longitude of the location (either the country code or both coordinates should
                      be given.
    :return: a json object containing the latest values.
    """
    latest_data = None
    header = {'auth-token': token}

    if country_code is not None:
        latest_data = (requests
                           .get(API_ENDPOINTS["latest_country_code"]
                                .format(country_code = country_code),
                                headers = header)
                           .json())
    if (latitude is not None) & (longitude is not None):
        latest_data = (requests
                           .get(API_ENDPOINTS["latest_coordinates"]
                                .format(longitude = longitude, latitude = latitude))
                           .json())

    if latest_data is None:
        raise ValueError("No inputs defined")

    return latest_data

def get_latest_carbon_intensity(token, country_code = None, latitude = None, longitude = None):
    """Get latest carbon intensity.
    :param token: the token as received from co2signal.com.
    :param country_code: (optional) the country code of the country (either the country code or both coordinates should
                         be given.
    :param latitude: (optional) the latitude of the location (either the country code or both coordinates should
                     be given.
    :param longitude: (optional) the longitude of the location (either the country code or both coordinates should
                      be given.
    :return: the latest carbon intensity in gCO2eq/kWh.
    """

    latest_data = get_latest(token, country_code, latitude, longitude)

    latest_carbon_intensity = latest_data['data']['carbonIntensity']

    return latest_carbon_intensity
