"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    return (celsius*9/5)+32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    while True:
        try:
            temp = float(input("Temperature: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value")

    while True:
        unit = input("Unit (C or F): ").strip().upper()
        if unit in ["C","F"]:
            break
        print("Invalide unit. Pleaser enter C or F")

    if unit=="C":
        temp=celsius_to_fahrenheit(temp)
        temp=round(temp,2)
        print("Converted temperature:", temp, "F")

    elif unit=="F":
        temp=fahrenheit_to_celsius(temp)
        temp=round(temp,2)
        print("Converted temperature:", temp, "C")

    return temp


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()
