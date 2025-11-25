# Smart Agriculture Monitoring System

A simple Python project that simulates a basic smart farming assistant.\
The system takes user inputs (acting as sensor readings) and provides
useful crop-care recommendations.

------------------------------------------------------------------------

## Features

-   Soil moisture analysis\
-   Temperature-based suggestions\
-   Humidity-based crop alerts\
-   Beginner-friendly logic using simple if--else\
-   No external libraries required

------------------------------------------------------------------------

## Project Objective

To demonstrate how simple programming can be applied to real-world
agriculture problems through basic decision-making.

------------------------------------------------------------------------

## How It Works

The user enters: - Soil Moisture (0--100) - Temperature (°C) - Humidity
(0--100)

The system analyzes these values and prints recommendations such as: -
When to irrigate\
- When to provide shade\
- When to increase ventilation\
- When conditions are optimal

------------------------------------------------------------------------

## Technologies Used

-   Python 3\
-   Basic programming concepts (input, conditions, print statements)

------------------------------------------------------------------------

## Code

``` python
print("=== Smart Agriculture Monitoring System ===")

soil_moisture = int(input("Enter Soil Moisture Level (0-100): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = int(input("Enter Humidity Level (0-100): "))

print("\n--- System Analysis ---")

if soil_moisture < 30:
    print("• Soil is dry → Recommendation: Start irrigation.")
elif soil_moisture > 80:
    print("• Soil is too wet → Recommendation: Stop irrigation to avoid root rot.")
else:
    print("• Soil moisture is optimal.")

if temperature < 15:
    print("• Temperature is low → Recommendation: Use protective crop cover.")
elif temperature > 35:
    print("• Temperature is high → Recommendation: Provide shading or increase watering.")
else:
    print("• Temperature is suitable for most crops.")

if humidity < 40:
    print("• Low humidity → Recommendation: Mist plants or increase irrigation frequency.")
elif humidity > 85:
    print("• High humidity → Recommendation: Ensure ventilation to prevent fungal issues.")
else:
    print("• Humidity levels are good.")

print("\n=== Summary ===")
print("Analysis completed. Follow the recommendations above.")
```

------------------------------------------------------------------------
