# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:03:49 2020

@author: Kyungmin Lee
"""

# R / Week3 Assignment

import warnings
warnings.filterwarnings("ignore")

import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

help(ccrs.PlateCarree())

# 1st figure
plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
# Above we declare our axes to be of the ccrs.PlateCarree() 
#(which is just latitude/longitude) projection. 
# On those axes defined in that projection, we can add coastlines(), 
#another cartopy function with built in coastline data.


# 2nd figure
plt.figure()
ax = plt.axes(projection=ccrs.Mollweide())
ax.stock_img()
# Above we declare our axes to be of ccrs.Mollweide() projection. 
# We use cartopy's stock_img() function to fill the axes 
# with a quasi-true color stock image from cartopy. 

# 3rd figure
ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='blue', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),
         )
plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

# 4th figure
ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),
         )

plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
         horizontalalignment='left',
         transform=ccrs.Geodetic())
# Notice the difference in how the dots are connected. 
# It all comes down the the `transform` argument within the `plt.plot` . 
# We are declaring different data projections even though they're both just points.

#By default, the coordinate system of any data added to a GeoAxes is the same 
# as the coordinate system of the GeoAxes itself, to control which coordinate system 
# that the given data is in, you can add the transform keyword with an appropriate cartopy.crs.CRS instance

# 3rd figure ver2
ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='blue', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),
         )
plt.text(ny_lon - 3, ny_lat - 12, 'Delaware',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Seoul',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

# 4th figure ver2
ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),
         )

plt.text(ny_lon - 3, ny_lat - 12, 'Delaware',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Seoul',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

# Cartopy Fundamentals - Features (cfeatures)

# 5th figure
import cartopy.feature as cf

plt.figure()
ax = plt.axes(projection = ccrs.LambertConformal())  
ax.add_feature(cf.COASTLINE)                 
ax.set_title("Title")

# 6th figure
import numpy as np
import cartopy.feature as cf

central_lat = 37.5
central_lon = -96
extent = [-120, -70, 24, 50.5]
central_lon = np.mean(extent[:2])
central_lat = np.mean(extent[2:])

plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAND, edgecolor='black')
ax.add_feature(cf.LAKES, edgecolor='black')
ax.add_feature(cf.RIVERS)
ax.gridlines()

# Hurricane Katrina Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import shapely.geometry as sgeom

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader


#HURDAT2 dataset from AOML/NOAA:
#http://www.aoml.noaa.gov/hrd/hurdat/newhurdat-all.html on 14th Dec 2012.


lons = [-75.1, -75.7, -76.2, -76.5, -76.9, -77.7, -78.4, -79.0,
        -79.6, -80.1, -80.3, -81.3, -82.0, -82.6, -83.3, -84.0,
        -84.7, -85.3, -85.9, -86.7, -87.7, -88.6, -89.2, -89.6,
        -89.6, -89.6, -89.6, -89.6, -89.1, -88.6, -88.0, -87.0,
        -85.3, -82.9]

lats = [23.1, 23.4, 23.8, 24.5, 25.4, 26.0, 26.1, 26.2, 26.2, 26.0,
        25.9, 25.4, 25.1, 24.9, 24.6, 24.4, 24.4, 24.5, 24.8, 25.2,
        25.7, 26.3, 27.2, 28.2, 29.3, 29.5, 30.2, 31.1, 32.6, 34.1,
        35.6, 37.0, 38.6, 40.1]

# Define a plotting function 
#that will vary the color of particular states 
#given the following conditions
def colorize_state(geometry):
    facecolor = (0.9375, 0.9375, 0.859375)
    if geometry.intersects(track):
        facecolor = 'red'
    elif geometry.intersects(track_buffer):
        facecolor = '#FF7E00'
    return {'facecolor': facecolor, 'edgecolor': 'black'}

#Note that this function will be called below to help color states

# 7th figure

# Chunk 1
fig = plt.figure(figsize=(12,8))
ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

shapename = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m',
                                     category='cultural', name=shapename)

# Chunk 2
ax.background_patch.set_visible(False)
ax.outline_patch.set_visible(False)
ax.set_title('US States which intersect the track of '
             'Hurricane Katrina (2005)')

# Chunk 3
track = sgeom.LineString(zip(lons, lats))
track_buffer = track.buffer(2)

# Chunk 4
ax.add_geometries(
    shpreader.Reader(states_shp).geometries(),
    ccrs.PlateCarree(),
    styler=colorize_state)

ax.add_geometries([track_buffer], ccrs.PlateCarree(),
                  facecolor='#C8A2C8', alpha=0.5)
ax.add_geometries([track], ccrs.PlateCarree(),
                  facecolor='none', edgecolor='k')

# Chunk 5
direct_hit = mpatches.Rectangle((0, 0), 1, 1, facecolor="red")
within_2_deg = mpatches.Rectangle((0, 0), 1, 1, facecolor="#FF7E00")
labels = ['State directly intersects\nwith track',
          'State is within \n2 degrees of track']
ax.legend([direct_hit, within_2_deg], labels,
          loc='lower left', bbox_to_anchor=(0.025, -0.1), fancybox=True)

#Adding data to a cartopy plot
import numpy as np

#Let's create some sample data and plot a contour plot
# 8th figure
lon = np.linspace(-80, 80, 25)
lat = np.linspace(30, 70, 25)
lon2d, lat2d = np.meshgrid(lon, lat)
data = np.cos(np.deg2rad(lat2d) * 4) + np.sin(np.deg2rad(lon2d) * 4)

plt.figure(figsize=(10,6))
plt.contourf(lon2d, lat2d, data)

#Now let's overlay this onto a cartopy plot with geospatial axes
# 9th figure
plt.figure(figsize=(12,8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data)

#We created a PlateCarree projection 
#and plot the data on it without any transform keyword. 
#This happens to work because PlateCarree is the simplest projection of lat / lon data.

#Try this with a more complex projection
#10th figure
projection = ccrs.RotatedPole(pole_longitude=-177.5, pole_latitude=37.5)

plt.figure(figsize=(12,8))
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data)

#This is wrong! why? 
#Because we need to add in the transform argument because our data comes in a different projection.
#You can plot in whatever projection you want so long as the data is transformed to the projection of the plot!

#11th figure
projection = ccrs.RotatedPole(pole_longitude=-177.5, pole_latitude=37.5)

plt.figure(figsize=(12,8))
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()
ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

# load in a built-in tutorial dataset from xarray
ds = xr.tutorial.load_dataset('air_temperature')

ds


# convert this to fahrenheit
ds['air'].values = (ds['air'].values - 273.15)*(9/5) + 32

# select one time slice - create separate object and call it airtemp
# 12th figure
airtemp = ds.air.sel(time='2013-01-01 12:00', method='nearest')


fig = plt.figure(figsize=(16,10))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
ax.gridlines()
airtemp.plot(ax=ax, transform=ccrs.PlateCarree(),
         vmin=20, vmax=50, cbar_kwargs={'shrink': 0.4}) # cbar_kwargs={'shrink': 0.4} just shrinks the colorbar

#Note that I know the initial dataset comes in ccrs.PlateCarree(), 
#hence the transform=ccrs.PlateCarree() argument . 
#We'll learn how to get python to tell us what the projection is in the future

#Let's choose a better colormap instead of blue green yellow

#13th figure
from matplotlib import cm #import colormap module from the matplotlib library


new_cmap = cm.get_cmap('YlOrRd') # Yellow orange red colormap 


fig = plt.figure(figsize=(16,10))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
ax.gridlines()
airtemp.plot(ax=ax, transform=ccrs.PlateCarree(),
         vmin=20, vmax=50, cbar_kwargs={'shrink': 0.4}, cmap=new_cmap) # notice the cmap argument

# Cartopy assignment
#1) Download treecov.nc from the datasets folder (https://github.com/jsimkins2/geog473-673/blob/master/datasets/treecov.nc)

#2) Use xarray to open dataset (xr.open_dataset).

#3) Remove bad values (values below 0%). (hint: xarray.where() function)

#4) Plot TreeCover percentage of North America with a green colormap¶

#5) Plot as ccrs.LambertConformal() (treecov.nc comes as ccrs.PlateCarree() )

#6) Submit resulting plot to Canvas - Cartopy Assignment

