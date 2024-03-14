# 1. Create a class that encapsulates logic for converting temperatures between Celsius and Fahrenheit, Kelvin .
# Use properties with getters and setters to ensure valid temperature values and provide a user-friendly interface.


# class ConvertTemperature:
#     LOWEST_CELSIUS_TEMP = -273.15
#     KELVIN_VALUE = 273.15
#     FAHRENHEIT_VALUE = 32

#     def __init__(self, temp_in_celsius=0.0) -> None:
#         self._temp_in_celsius = temp_in_celsius

#     @property
#     def temp_in_celsius(self) -> float:
#         print("Temperature in Celsius: ")
#         return self._temp_in_celsius

#     @property
#     def celsius_to_fahrenheit(self) -> float:
#         return round(((1.8 * self._temp_in_celsius) + self.FAHRENHEIT_VALUE), 2)

#     @property
#     def celsius_to_kelvin(self) -> float:
#         return round((self._temp_in_celsius + self.KELVIN_VALUE), 2)

#     @temp_in_celsius.setter
#     def temp_in_celsius(self, value):
#         if value > self.LOWEST_CELSIUS_TEMP:
#             print("Setting temperature in Celsius...")
#             self._temp_in_celsius = value
#         else:
#             self._temp_in_celsius = self.LOWEST_CELSIUS_TEMP
#             print(
#                 "Value you've entered is below lowest temperature.\nTemperature has been set to it's lowest."
#             )


# converter = ConvertTemperature()

# print(converter.celsius_to_fahrenheit, converter.celsius_to_kelvin)

# converter.temp_in_celsius = 15.0

# print(converter.celsius_to_fahrenheit, converter.celsius_to_kelvin)

# =================================================================================================================

