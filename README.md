# pyco2
A package to access the co2signal API.

```python
import pyco2

token = "get yours from co2signal.com"

# query using the country code
pyco2.co2signal.get_latest_carbon_intensity(token, country_code='BE')

# query using the location
pyco2.co2signal.get_latest_carbon_intensity(token, longitude=50, latitude=5)
```


