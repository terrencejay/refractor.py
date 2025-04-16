class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"},
            "Chicago": {"temperature": 65, "condition": "Partly Cloudy", "humidity": 55, "city": "Chicago"}
        }
        return weather_data.get(city, {})