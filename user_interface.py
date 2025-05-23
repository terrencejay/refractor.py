from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self):
        self.data_fetcher = WeatherDataFetcher()
        self.data_parser = DataParser()

    def get_detailed_forecast(self, city):
       
        data = self.data_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def display_weather(self, city):
        """
        Function to display the basic weather forecast for a city.
        """
        data = self.data_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.data_parser.parse_weather_data(data)
            print(weather_report)

    def main(self):
        
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()