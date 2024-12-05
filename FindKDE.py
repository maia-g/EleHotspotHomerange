##---------------------------------------------------------------------
## FindKDE.py
##
## Description: Read in elephant collar tracking data and create a
##              hotspot map using Kernel Density Estimate tool.
##
## Usage: Analyze elephant movement spatially
##
## Created: Fall 2024
## Author: maia.griffith@duke.edu (for ENV859)
##---------------------------------------------------------------------

##------Set Up------

# Load relevant packages
import os
import sys
import arcpy

# Allow user input for scratch workspace, output workspace, and dataset.
gdb = arcpy.GetParameterAsText(0) #Sets output workspace where important outputs from model will go
points = arcpy.GetParameterAsText(1) #User input in ArcPro should be the SELECTED points file
suffix = arcpy.GetParameterAsText(2) #Get user input for suffix to attach to KDE name
cellSize = arcpy.GetParameterAsText(3) #User selects output cell size (rec. range in tool)
radius = arcpy.GetParameterAsText(4) #User selects search radius in Km (rec. range in tool)

# Save only the relevant info for the base name
name = os.path.basename(points).split('.')[0].replace("_PointSelect", "")  
    

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##------Find KDE------

# Create a Kernel Density Estimate map to show areas of high activity use
dataKDE = f"{gdb}\\{name}_KDE{suffix}"
with arcpy.EnvManager(scratchWorkspace= gdb): # Work within geodatabase
    out_raster = arcpy.sa.KernelDensity(
        in_features= points, #User input
        population_field="NONE",
        cell_size= cellSize, #User input
        search_radius= radius, #User input
        area_unit_scale_factor="SQUARE_KILOMETERS",
        out_cell_values="DENSITIES",
        method="PLANAR",
        in_barriers=None
    )
    out_raster.save(dataKDE)