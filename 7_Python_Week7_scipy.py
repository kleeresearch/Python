# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:12:48 2020

@author: Kyungmin Lee
"""


import matplotlib.pyplot as plt
import cartopy
import cartopy.feature as cf
import cartopy.crs as ccrs
import xarray as xr
import numpy as np


oceanSST = xr.open_dataset("/Users/x-note/Downloads/OR_ABI-L2-SSTF-M3_G16_s20192081300453_e20192081400161_c20192081406297.nc")
oceanSST

#Band 15 (IR (“Dirty IR Longwave Band”) of GOES-R Satellite Data
oceanSST["Band15"]

#Grab the only timestamp (zeroth index)
oceanSST["Band15"][0]

#Check out Lat/Lon values
oceanSST['longitude'].values, oceanSST['latitude'].values

# Plot up the 'Old-Fashioned Way' - Using matplotlib.pyplot pcolormesh
import numpy as np
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent((-100,-60,16,52), crs=ccrs.PlateCarree())
im = ax.pcolormesh(oceanSST['longitude'].values, oceanSST['latitude'].values, oceanSST['Band15'][0].values,
                   cmap='jet', transform=ccrs.PlateCarree(), vmin=250,vmax=300)
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.BORDERS)
plt.colorbar(im, label="Degrees Kelvin")
# Plot lat / lon ticks
plt.xticks(np.arange(np.min(oceanSST['longitude'].values), np.max(oceanSST['longitude'].values), 10))
plt.yticks(np.arange(np.min(oceanSST['latitude'].values), np.max(oceanSST['latitude'].values), 10))
# Plot x/y labels
plt.xlabel("Longitude")
plt.ylabel("Latitude")
# Plot Title
plt.title("Band 15 Brightness Temperature")

# What about SST?
# This time we'll plot with the handy-dandy xarray plotting function
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
oceanSST['SST'][0].plot(cmap='jet', vmin=273, vmax=300)
ax.add_feature(cf.COASTLINE, color='Gray', edgecolor='Black')
ax.add_feature(cf.BORDERS, color='Gray', edgecolor='Black')
ax.add_feature(cf.STATES, edgecolor='Black')
#Alright, so the clouds are getting right in the way of our SST data! We have satellite returns over cloudy locations, but they are invalid! Let's get rid of this bad data

#Now use Xarray to plot the SST data where there are no clouds (only SST data where Band15 > 280 Kelvin)
oceanSST_rev = oceanSST['SST'].where(oceanSST['Band15'] > 280)

# Let's plot up our cleaned SST image!
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
oceanSST_rev.plot(cmap='jet', vmin=273, vmax=300)
ax.add_feature(cf.COASTLINE, color='gray', edgecolor='Black')
ax.add_feature(cf.BORDERS, color='gray', edgecolor='Black')
ax.add_feature(cf.STATES, edgecolor='Black')

