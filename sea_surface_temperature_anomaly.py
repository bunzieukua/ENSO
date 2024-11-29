"""install"""
!apt-get install libproj-dev proj-data proj-bin --quiet
!apt-get install libgeos-dev --quiet
!pip install cython --quiet
!pip install cartopy --quiet
!pip install geoviews
!apt-get -qq install python-cartopy python3-cartopy  --quiet
!pip uninstall -y shapely  --quiet
!pip install shapely --no-binary shapely  --quiet
!pip install boto3 --quiet

"""import"""
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import os
import pooch
import tempfile
import holoviews
from geoviews import Dataset as gvDataset
import geoviews.feature as gf
from geoviews import Image as gvImage
from pooch import retrieve

"""
For this code to work, you will have to upload your sea surface temperature data onto GG Drive.
I did this because my laptop is so broken it cannot bear large files.
You can download 
"""

from google.colab import drive
drive.mount('/content/drive')

#define the filepath
file_path = '/content/drive/MyDrive/'"""input your file here""""'

#open dataset with xarray
dt = xr.open_dataset(
    file_path,
    chunks = {"time": 25, "latitude": 200, "longitude": 200},
)

dt

