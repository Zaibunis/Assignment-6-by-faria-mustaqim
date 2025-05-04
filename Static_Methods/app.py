class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius
    def celsius_to_fahrenheit(c):
        return (c * 1.8) + 32
    
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")