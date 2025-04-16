class DataParser:
    """
    Parses weather data.
    """
    def parse_weather_data(self, data):
        """
        Function to parse weather data.
        """
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"