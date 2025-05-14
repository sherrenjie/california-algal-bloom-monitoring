# California Coast Algal Bloom Monitoring (2014-2024)

## Project Overview
This repository contains code and documentation for monitoring and analyzing harmful algal blooms (HABs) along the California coast using satellite remote sensing data. The project examines a 10-year trend (2014-2024) of chlorophyll-a concentrations, which serve as indicators of algal bloom activity.

## Objectives
- Track and visualize harmful algal bloom events along the California coast
- Analyze 10-year trends in bloom frequency, intensity, and distribution
- Investigate correlations between algal blooms and sea surface temperature (SST)
- Identify seasonal patterns and potential environmental drivers

## Study Area
- Geographic focus: Central and Southern California coastal waters
- Coordinates: Approximately 32°N to 38°N, 118°W to 124°W
- Temporal coverage: 2014-2024

## Data Sources
- Chlorophyll-a concentration data: NASA MODIS-Aqua and VIIRS sensors
- Sea Surface Temperature (SST) data: NASA MODIS-Aqua and VIIRS sensors
- Data access via NASA OceanColor Web (https://oceancolor.gsfc.nasa.gov/)

## Methods
1. Satellite data acquisition from NASA OceanColor Web
2. Pre-processing using Python (xarray, netCDF4)
3. Bloom detection using chlorophyll-a threshold analysis
4. Time series analysis to identify trends
5. Correlation analysis with SST and other environmental factors
6. Spatial and temporal visualization using Matplotlib and Cartopy

## Required Packages
- xarray
- netCDF4
- matplotlib
- cartopy
- pandas
- numpy
- scipy

## Getting Started
1. Clone this repository
2. Install required packages using `conda` or `pip`
3. Navigate to the notebooks directory for step-by-step analysis examples
4. Follow the workflow in `notebooks/01_data_acquisition.ipynb` to begin

## License
[MIT License](LICENSE)

## Contact
Sherren Jie - sherrenjielita@brandeis.edu

## Acknowledgments
- NASA Goddard Space Flight Center, Ocean Ecology Laboratory, Ocean Biology Processing Group
