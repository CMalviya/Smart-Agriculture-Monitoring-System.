print("=== Smart Agriculture Monitoring System ===")

# Taking simulated sensor inputs
soil_moisture = int(input("Enter Soil Moisture Level (0-100): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = int(input("Enter Humidity Level (0-100): "))

print("\n--- System Analysis ---")

# Soil moisture check
if soil_moisture < 30:
    print("• Soil is dry → Recommendation: Start irrigation.")
elif soil_moisture > 80:
    print("• Soil is too wet → Recommendation: Stop irrigation to avoid root rot.")
else:
    print("• Soil moisture is optimal.")

# Temperature check
if temperature < 15:
    print("• Temperature is low → Recommendation: Use protective crop cover.")
elif temperature > 35:
    print("• Temperature is high → Recommendation: Provide shading or increase watering.")
else:
    print("• Temperature is suitable for most crops.")

# Humidity check
if humidity < 40:
    print("• Low humidity → Recommendation: Mist plants or increase irrigation frequency.")
elif humidity > 85:
    print("• High humidity → Recommendation: Ensure proper ventilation to avoid fungal growth.")
else:
    print("• Humidity levels are good.")

print("\n=== Summary ===")
print("Analysis completed. Follow the recommendations above.")
