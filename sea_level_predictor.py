import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa_sea_level.csv')
    print(df.head(10))

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue', alpha=0.5)

    # Create first line of best fit (using all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_series = pd.Series(range(1800, 2076))  # from 1800 to 2076
    sea_level_predicted = intercept + slope * years_series
    plt.plot(years_series, sea_level_predicted, 'r', label='Fit: Toda la data')  # Use red color for this line

    # Create second line of best fit (using data from 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_series_2000 = pd.Series(range(2000, 2076))  # from 2000 to 2076
    sea_level_predicted_2000 = intercept_2000 + slope_2000 * years_series_2000
    plt.plot(years_series_2000, sea_level_predicted_2000, 'g', label='Fit: A partir del año 2000')  # Use green color for this line

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()