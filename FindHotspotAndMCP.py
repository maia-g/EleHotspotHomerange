##---------------------------------------------------------------------
## FindHotspotAndMCP.py
##
## Description: Use processed dataset to find hotspots (total count per hexagons) 
##                   and generate home range (Minimum Convex Polygons).
##
## Usage: Create bounding box to remove outliers, generate hexagons,
##             calculate counts per hexagon, and find MCP home range.
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
scratch = arcpy.GetParameterAsText(0) #Sets scratch workspace where most interim model outputs will go
gdb = arcpy.GetParameterAsText(1) #Sets output workspace where important outputs from model will go
data_points = arcpy.GetParameterAsText(2) #User input in ArcPro should be the POINTS file
data_lines = arcpy.GetParameterAsText(3) #User input in ArcPro should be the LINE file
name = os.path.basename(data_points).split('.')[0].replace("_Points", "")  
    #Save only the ele name and the months of data

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.EnvManager(scratchWorkspace= scratch, workspace= gdb)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

# Create bounding box/extent with user input
topLat = arcpy.GetParameterAsText(4) #User input in ArcPro
bottomLat = arcpy.GetParameterAsText(5) #User input in ArcPro
leftLon = arcpy.GetParameterAsText(6) #User input in ArcPro
rightLon = arcpy.GetParameterAsText(7) #User input in ArcPro

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

# Recreate line shapefile from selected points and save to Geodatabase using: Points to Line
selectedLines = f"{gdb}\\{name}_LineSelect"
arcpy.management.PointsToLine(
    Input_Features= selectedPoints,
    Output_Feature_Class= selectedLines,
    Line_Field="Tag",
    Sort_Field="Time_Stamp",
    Close_Line="NO_CLOSE",
    Line_Construction_Method="TWO_POINT",
    Attribute_Source="BOTH_ENDS",
    Transfer_Fields="Latitude;Longitude;Time_Stamp;Date;Month;Log_Interv;Speed;Temperatur;Movement;Accelerome"
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