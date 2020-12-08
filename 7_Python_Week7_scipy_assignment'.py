# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:45:15 2020

@author: Kyungmin Lee
"""

import matplotlib.pyplot as plt
import cartopy
import cartopy.feature as cf
import cartopy.crs as ccrs
import xarray as xr
import numpy as np

#So, we just used Band15 as a 'cloud-mask' for our SST data. 
#There's actually a variable in this dataset called DQF - 
#Data Quality Flag - that has grades for each grid cell SST value. 
#0 is a good graded grid cell. 
#1 could be a good or could be bad, the algorithm is unsure. 
#2 is a bad graded grid cell. 
#3 is a land graded grid cell.


#1)Load dataset above.
oceanSST = xr.open_dataset("/Users/x-note/Downloads/OR_ABI-L2-SSTF-M3_G16_s20192081300453_e20192081400161_c20192081406297.nc")
oceanSST

#2)Select SST values where DQF == 0 .
oceanSST = oceanSST['SST'].where(oceanSST['DQF'] == 0)

#3)Plot SST values using the pcolormesh method above
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent((-100,-60,16,52), crs=ccrs.PlateCarree())
im = ax.pcolormesh(oceanSST['longitude'].values, oceanSST['latitude'].values, oceanSST[0].values,
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
plt.title("SST")

#4)Submit image to Canvas

