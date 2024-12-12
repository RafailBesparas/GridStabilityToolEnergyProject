import pandas as pd
import numpy as np

# Generate sample data for Historical Market Prices
dates = pd.date_range(start="2023-01-01", end="2023-01-31", freq="H")
market_prices = np.random.uniform(20, 200, len(dates))  # Simulated prices in €/MWh

# Generate sample data for Weather Data
temperature = np.random.uniform(-5, 30, len(dates))  # Temperature in Celsius
wind_speed = np.random.uniform(0, 25, len(dates))  # Wind speed in m/s
solar_radiation = np.random.uniform(0, 800, len(dates))  # Solar radiation in W/m^2

# Generate sample data for Renewable Energy Generation
solar_generation = solar_radiation * 0.15  # 15% efficiency for solar panels
wind_generation = wind_speed * 50  # Simulated generation from wind turbines

# Combine into a DataFrame
dataset = pd.DataFrame({
    'Timestamp': dates,
    'Market_Price_€/MWh': market_prices,
    'Temperature_C': temperature,
    'Wind_Speed_m/s': wind_speed,
    'Solar_Radiation_W/m^2': solar_radiation,
    'Solar_Generation_MW': solar_generation,
    'Wind_Generation_MW': wind_generation
})


dataset.to_csv("electricity_market_data.csv", index=False)

print("Dataset saved to 'electricity_market_data.csv'")

