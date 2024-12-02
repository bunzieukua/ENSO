"""
In this file, we will download the precipitation dataset from NOAA using s3fs and pooch packages.
Again, I highly recommend you to look at the dataset on the official webpage to familiarize yourself with the
data structure and the naming system.
Not all files are named the same, and you will have to make modification in file names so as to get the desired data
"""

fs = s3fs.S3FileSystem(anon=True)
file_pattern = "noaa-cdr-precip-gpcp-monthly-pds/data/*/gpcp_v02r03_monthly_*.nc" 
file_location = fs.glob(file_pattern)
file_location = sorted(file_location)
file_ob = [
    pooch.retrieve(f"http://s3.amazonaws.com/{file}", known_hash=None)
    for file in file_location
]
ds = xr.open_mfdataset(file_ob, combine="nested", concat_dim="time")

"""visualize global precipitation at a specific time point"""

precip = ds.precip
data = precip.sel(time="2024-07-01", method="nearest")
fig, ax = plt.subplots(subplot_kw={"projection": ccrs.Robinson(central_longitude=-160)},
                       dpi=300)
ax.coastlines()
ax.gridlines()
data.plot(
    ax=ax,
    transform=ccrs.PlateCarree(),
    robust = True,
        cbar_kwargs=dict(shrink=0.5, label="GPCP Monthly Precipitation \n(mm/day)"),
)


"""Visualize time series precipitation at a specific location"""

#I'm visualizing data for Hanoi, Vietnam here, hence the name and the coordinates. Please adjust the code for your preferred location

grid_hn = metadata.precip.sel(latitude=21, longitude=105, method="nearest") 
grid_hn = grid_hn.sel(time=slice("2020-01-01", "2024-01-01"))
fig, ax = plt.subplots(dpi=300)
grid_hn.plot(ax=ax)

ax.set_title("GPCP Monthly Precipitation in Hanoi, Vietnam")
ax.grid(True)
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (mm/day)")
