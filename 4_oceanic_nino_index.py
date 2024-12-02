"""
This will calculate the ONI from 1980 to 2024 using the dataset downloaded in
the sea_surface_temperature_anomaly file. Note that the coordinates of the 
Nino 3.4 region is 5N-5S, 120W-170W. 
We will first calculate the sea surface temperature anomalies of this region, 
then use that anomalies to calculate ONI
"""

"""choose the SST data for the Nino 3.4 region"""
sst_nino34 = sst_anom.sel(lat=slice(-5, 5), lon=slice(190, 240))

"""calculate the mean of sea surface temperature data for this region"""
nino34_mean = sst_nino34.mean(dim=("lat", "lon"))

"""plotting time series data"""
fig, ax = plt.subplots(dpi = 300)
nino34_mean.plot(ax=ax)
ax.set_xlabel("Time (months)")
ax.set_ylabel("Nino3.4 Anomaly (°C)")
ax.axhline(y=0, color="k", linestyle="dashed")

"""calculate ONI"""
oni = nino34_mean.rolling(time=3, center=True).mean()

"""plot ONI data"""
fig, ax = plt.subplots(figsize=(12,6), dpi = 300)
nino34_mean.plot(label = "Nino 3.4", ax=ax)
oni.plot(color='k', label = "ONI", ax=ax)
ax.set_xlabel("Time (months)")
ax.set_ylabel("Anomaly (°C)")
ax.axhline(y=0, color="k", linestyle="dashed")
ax.legend()

"""visualize ONI with indicators of ENSO"""
fig, ax = plt.subplots(dpi = 300)
ax.fill_between(
    oni.time.data,
    oni.where(oni >= 0.5).data,
    0.5,
    color="red",
    alpha=0.9,
) """this generates indicators of El Nino, when ONI is >= +0.5"""

ax.fill_between(
    oni.time.data,
    oni.where(oni <= -0.5).data,
    -0.5,
    color="blue",
    alpha=0.9,
) """this generates indicators of La Nina, when ONI is <= -0.5"""

oni.plot(color="black", ax=ax)
ax.axhline(0, color="black", lw=0.5)
ax.axhline(0.5, color="red", linewidth=0.5, linestyle="dotted")
ax.axhline(-0.5, color="blue", linewidth=0.5, linestyle="dotted")
ax.set_title("Oceanic Niño Index")
ax.set_xlabel('Time (months)')
ax.set_ylabel('ONI')

