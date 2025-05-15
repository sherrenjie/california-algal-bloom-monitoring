import xarray as xr
import os
import glob
from typing import List, Optional, Union, Dict

def list_data_files(data_dir: str, pattern: str = "*.nc") -> List[str]:
    """
    List all NetCDF data files in a directory matching a pattern.
    
    Parameters
    ----------
    data_dir : str
        Directory containing data files
    pattern : str, default="*.nc"
        Glob pattern to match files
        
    Returns
    -------
    List[str]
        List of file paths
    """
    return sorted(glob.glob(os.path.join(data_dir, pattern)))

def load_chlorophyll_data(file_path: str) -> xr.Dataset:
    """
    Load chlorophyll data from a NetCDF file.
    
    Parameters
    ----------
    file_path : str
        Path to NetCDF file
        
    Returns
    -------
    xr.Dataset
        Xarray Dataset containing chlorophyll data
    """
    ds = xr.open_dataset(file_path)
    return ds

def load_multiple_files(file_paths: List[str]) -> xr.Dataset:
    """
    Load and merge multiple chlorophyll data files.
    
    Parameters
    ----------
    file_paths : List[str]
        List of paths to NetCDF files
        
    Returns
    -------
    xr.Dataset
        Combined dataset
    """
    datasets = [xr.open_dataset(fp) for fp in file_paths]
    combined = xr.concat(datasets, dim='time')
    return combined

def get_california_subset(ds: xr.Dataset, 
                          lat_range: tuple = (32, 38), 
                          lon_range: tuple = (-124, -118)) -> xr.Dataset:
    """
    Extract California coastal region from dataset.
    
    Parameters
    ----------
    ds : xr.Dataset
        Input dataset
    lat_range : tuple, default=(32, 38)
        Latitude range (min, max)
    lon_range : tuple, default=(-124, -118)
        Longitude range (min, max)
        
    Returns
    -------
    xr.Dataset
        Subset of data for California coast
    """
    # Handle possible different coordinate names
    lat_var = 'lat' if 'lat' in ds.coords else 'latitude'
    lon_var = 'lon' if 'lon' in ds.coords else 'longitude'
    
    # Convert longitude range if needed (-180 to 180 vs 0 to 360)
    if ds[lon_var].min() >= 0:  # 0 to 360 system
        lon_range = (360 + lon_range[0] if lon_range[0] < 0 else lon_range[0],
                     360 + lon_range[1] if lon_range[1] < 0 else lon_range[1])
    
    # Extract subset
    subset = ds.sel({lat_var: slice(lat_range[0], lat_range[1]),
                      lon_var: slice(lon_range[0], lon_range[1])})
    
    return subset