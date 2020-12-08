# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:31:32 2020

@author: Kyungmin Lee
"""

# Cartopy assignment
#1) Download treecov.nc from the datasets folder (https://github.com/jsimkins2/geog473-673/blob/master/datasets/treecov.nc)

#2) Use xarray to open dataset (xr.open_dataset).


# ignore the warnings
import warnings
warnings.filterwarnings('ignore')

import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd

from matplotlib import cm
import xarray as xr


treeData = xr.open_dataset("/Users/x-note/Downloads/treecov.nc")
treeData

#3) Remove bad values (values below 0%). (hint: xarray.where() function)


treeData_sub = treeData["treecov"].where(treeData["treecov"] >= 0)
len(treeData_sub)

#4) Plot TreeCover percentage of North America with a green colormap¶

fig = plt.figure(figsize=(16,10))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
ax.gridlines()
treeData_sub.plot(ax=ax, transform=ccrs.PlateCarree(), 
                vmin=0, vmax=100, cbar_kwargs={'shrink':0.4})

#5) Plot as ccrs.LambertConformal() (treecov.nc comes as ccrs.PlateCarree() )

projection = ccrs.RotatedPole(pole_longitude=-177.5, pole_latitude=37.5)

plt.figure(figsize=(12,8))
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data, transform=ccrs.LambertConformal())

#6) Submit resulting plot to Canvas - Cartopy Assignment
