
"""
For this code to work, you will have to upload your sea surface temperature data onto GG Drive.
I did this because my laptop is so broken it cannot bear large files.
You can download the dataset here, using the "HTTPServer": https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2/catalog.html?dataset=Datasets/noaa.oisst.v2/sst.mnmean.nc
Note: this dataset is from Optimum Interpolation Sea Surface Temperature (OISST) dataset. 
The link above contains the monthly mean of sea surface temperature only. Please visit the official website to see more data available
"""

from google.colab import drive
drive.mount('/content/drive')

#define the filepath
file_path = '/content/drive/MyDrive/'"""input your file here""""'

#open dataset with xarray
dt = xr.open_dataset(
    file_path,
    chunks = {"time": 25, "latitude": 200, "longitude": 200}, """replace this with the coordinates of your preferred locations"""
)

dt

"""
According to NOAA, the reference period for sea surface temperature anomalies should span across 30 years. 
Here I choose the 1991-2020
"""

"""choosing reference period"""
sst_30yr = dt.sst.sel(time=slice("1991-01-01", "2020-01-01"))

"""calculate the mean of each month in the period"""
sst_clim = sst_30yr.groupby("time.month").mean()

"""
calculate the sea surface temperature anomalies by substracting the mean of each month in the whole dataset
from the mean of the reference period
"""
sst_whole_dataset = dt.sst.groupby("time.month")
sst_anom = sst_whole_dataset - sst_clim

"""that's it for the calculation part, now we move onto plotting graphs"""
sst_oct2024 = sst_anom.sel(time="2024-10-01")

fig, ax = plt.subplots(
    subplot_kw={"projection": ccrs.Robinson(central_longitude=180)},
    dpi = 300
    #figsize=(9, 6)
)

ax.coastlines()
ax.gridlines()
sst_jul2016.plot(
    ax=ax,
    transform=ccrs.PlateCarree(),
    vmin=-3,
    vmax=3,
    cmap="RdBu_r",
    cbar_kwargs=dict(shrink=0.5, label="OISST Anomaly (degC)"),
)

"""interactive map for ENSO 2023-2024""""
holoviews.extension('bokeh')

dataset_plot = gvDataset(sst_anom.sel(time=slice('2023-05-01','2024-07-01')))
images = dataset_plot.to(gvImage, ['lon', 'lat'], ['sst'], 'time')
images.opts(cmap='RdBu_r',
            colorbar=True,
            width=600,
            height=400,
            projection=ccrs.Robinson(central_longitude=180),
            clim=(-3,3),
            clabel ='OISST Anomaly (degC)'
) * gf.coastline

