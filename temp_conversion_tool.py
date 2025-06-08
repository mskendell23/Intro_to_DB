# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius: float) -> float:
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 

 # User Interaction
 def temperature_conversion():
     temp_input = input("Enter the temperature (e.g., 100): ").strip()
     unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

     try:
         temperature = float(temp_input)
         except ValueError:
             raise ValueError("Invalid temperature. Please enter a numeric value.")
            
        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F")
        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.") 

 # Run the conversion function
 try:
     temperature_conversion()
except ValueError as e:
    print(e)
