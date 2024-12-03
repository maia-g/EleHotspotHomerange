##---------------------------------------------------------------------
## FindHotspotAndMCP.py
##
## Description: Use processed dataset to find hotspots (total count per hexagons) 
##                   and generate homerange (Minimum Convex Polygons).
##
## Usage: Create bounding box to remove outliers, generate hexagons,
##             calculate counts per hexagon, and find MCP homerange.
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
##### UNCOMMENT BELOW WHEN READY TO GO IN ARCPRO###############
scratch = arcpy.GetParameterAsText(0) #Sets scratch workspace where most interim model outputs will go
gdb = arcpy.GetParameterAsText(1) #Sets output workspace where important outputs from model will go
# scratch = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Scratch"
# gdb = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Final859_mhg29.gdb"

# Set environment settings
arcpy.env.overwriteOutput = True #Make sure to exit interaction window in VS Code before re-running code
arcpy.EnvManager(scratchWorkspace= scratch, workspace= gdb)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##### UNCOMMENT BELOW WHEN READY TO GO IN ARCPRO###############
data_points = arcpy.GetParameterAsText(2) #User input in ArcPro should be the POINTS file
data_lines = arcpy.GetParameterAsText(3) #User input in ArcPro should be the POLYLINE file
###dataset = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Scratch\\Batoka_Sept_Nov_Points.shp"
name = os.path.basename(data_points).split('.')[0].replace("_Points", "")  
    #Save only the ele name and the months of data
#print(name)

# Create bounding box/extent with user input
##### UNCOMMENT BELOW WHEN READY TO GO IN ARCPRO###############
topLat = arcpy.GetParameterAsText(4) #User input in ArcPro
bottomLat = arcpy.GetParameterAsText(5) #User input in ArcPro
leftLon = arcpy.GetParameterAsText(6) #User input in ArcPro
rightLon = arcpy.GetParameterAsText(7) #User input in ArcPro
# topLat = -15.55
# bottomLat = -26.00
# leftLon = 25.75
# rightLon = 26.15

##------Remove Outliers and Create Tessellation------

# Create bounding box to remove outliers
bounds = f""" Latitude < {topLat} AND
              Latitude > {bottomLat} AND 
              Longitude > {leftLon} AND 
              Longitude < {rightLon} 
          """

# Remove outliers for Points by only keeping data within bounding box using: Select
selectedPoints = f"{scratch}\\{name}_PointSelect.shp"
arcpy.analysis.Select(in_features= data_points, 
                      out_feature_class= selectedPoints, 
                      where_clause= bounds)

# Recreate polyline shapefile from selected points and save to Geodatabase using: Coordinate Table to Point
selectedLines = f"{gdb}\\{name}_LineSelect"
arcpy.defense.CoordinateTableToPolyline(
    in_table= selectedPoints,
    out_feature_class= selectedLines,
    x_or_lon_field="Longitude",
    in_coordinate_format="DD_2",
    y_or_lat_field="Latitude",
    line_group_field="Tag",
    sort_field="Time_Stamp",
    coordinate_system= arcpy.SpatialReference(32735)
)

# Create hexagons using: Generate Tessellation
hexGrid = f"{scratch}\\HexGrid_1km.shp"
tessExtent = arcpy.Describe(selectedPoints).extent #Extent of selected points
projection = arcpy.SpatialReference(32735) #Ensure WGS UTM Zone 35S
arcpy.management.GenerateTessellation(Output_Feature_Class= hexGrid,
                                      Extent= tessExtent,
                                      Shape_Type="HEXAGON",
                                      Size="866025.4 SquareMeters", #Makes side height 1km
                                      H3_Resolution=7,
                                      Spatial_Reference= projection #Makes sure project is correct
                                      )

##------Find Hotspots and Home Range------

# Calculate total count per hexagon using: Summarize Within
dataHotspot = f"{gdb}\\{name}_HS"
Output_Grouped_Table = ""
arcpy.analysis.SummarizeWithin(in_polygons=hexGrid,
                               in_sum_features=selectedPoints,
                               out_feature_class=dataHotspot,
                               shape_unit="SQUAREKILOMETERS",
                               out_group_table=Output_Grouped_Table)

# Find home range determined by MCPs using: Minimum Bounding Geometry
dataMCP = f"{gdb}\\{name}_MCP"
arcpy.management.MinimumBoundingGeometry(in_features=selectedPoints, 
                                         out_feature_class=dataMCP, 
                                         geometry_type="CONVEX_HULL")





