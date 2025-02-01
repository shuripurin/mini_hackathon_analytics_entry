

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import descartes
import contextily as ctx

# Load denver.csv
denver = pd.read_csv('./data/denver.csv')
print(denver.head())

# Load census.csv
census = pd.read_csv('./data/census.csv')
print(census.head())

import geopandas as gpd

# Load neighborhoods.shp
neighborhoods = gpd.read_file('./data/neighborhoods.shp')
print(neighborhoods.head())

# Check denver data
print(denver.info())
print(denver.describe())

# Check census data
print(census.info())
print(census.describe())

# Check neighborhoods data
print(neighborhoods.info())
print(neighborhoods.head())

# Explore the denver dataframe
print(denver.head())
print(denver.info())
print(denver.describe())

# Explore the neighborhoods dataframe
print(neighborhoods.head())
print(neighborhoods.info())

# Explore the census dataframe
print(census.head())
print(census.info())
print(census.describe())

# Plot the neighborhoods
neighborhoods.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

# Plot the Starbucks locations
plt.scatter(denver['Longitude'], denver['Latitude'], c='red', marker='o', label='Starbucks')

plt.title('Denver Neighborhoods and Starbucks Locations')
plt.legend()
plt.show()

# Calculate the proportion of the population aged 18-34
census['PROPORTION_18_34'] = census['AGE_18_TO_34'] / census['POPULATION_2010']

# Sort neighborhoods by the proportion of 18-34 year olds
sorted_neighborhoods = census.sort_values(by='PROPORTION_18_34', ascending=False)

# Display the top neighborhoods
print(sorted_neighborhoods[['NBHD_NAME', 'PROPORTION_18_34']].head())

top_three_neighborhoods = sorted_neighborhoods.head(3)
print(top_three_neighborhoods[['NBHD_NAME', 'PROPORTION_18_34']])

# Merge the top three neighborhoods with the neighborhoods dataframe
top_three = neighborhoods.merge(top_three_neighborhoods, on='NBHD_ID')

# Plot the neighborhoods
neighborhoods.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

# Highlight the top three neighborhoods
top_three.plot(ax=plt.gca(), color='blue', edgecolor='k', alpha=0.7)

# Plot the Starbucks locations
plt.scatter(denver['Longitude'], denver['Latitude'], c='red', marker='o', label='Starbucks')

plt.title('Top Three Neighborhoods for Expansion')
plt.legend()
plt.show()

# Example: Sort by both proportion of 18-34 and high-income households
census['PROPORTION_HIGH_INCOME'] = census['NUM_HHLD_100K+'] / census['NUM_HOUSEHOLDS']
sorted_neighborhoods_combined = census.sort_values(by=['PROPORTION_18_34', 'PROPORTION_HIGH_INCOME'], ascending=[False, False])

print(sorted_neighborhoods_combined[['NBHD_NAME', 'PROPORTION_18_34', 'PROPORTION_HIGH_INCOME']].head())

print("Top three neighborhoods for expansion based on the proportion of 18-34 year olds:")
print(top_three_neighborhoods[['NBHD_NAME', 'PROPORTION_18_34']])


