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
# scratch = arcpy.GetParameterAsText(0) #Sets scratch workspace where most interim model outputs will go
# output = arcpy.GetParameterAsText(1) #Sets output workspace where important outputs from model will go
scratch = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Scratch"
output = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\BassConnections_OrphanHotspots.gdb"

# Set environment settings
arcpy.env.overwriteOutput = True #Make sure to exit interaction window in VS Code before re-running code
arcpy.EnvManager(scratchWorkspace= scratch, workspace= output)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##### UNCOMMENT BELOW WHEN READY TO GO IN ARCPRO###############
# dataset = arcpy.GetParameterAsText(2) #User input in ArcPro
dataset = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Outputs\\Batoka_move_SubsetDry_Sept_Nov_Points.shp" 
name = os.path.splitext(os.path.basename(dataset))[0].split("Nov")[0] + "Nov" 
    #Removes file extension type then ensures the file name ends with Nov regaurdless of suffix
#print(name)

# Create bounding box/extent with user input
##### UNCOMMENT BELOW WHEN READY TO GO IN ARCPRO###############
# topLat = arcpy.GetParameterAsText(3) #User input in ArcPro
# bottomLat = arcpy.GetParameterAsText(4) #User input in ArcPro
# leftLon = arcpy.GetParameterAsText(5) #User input in ArcPro
# rightLon = arcpy.GetParameterAsText(6) #User input in ArcPro
topLat = -15.55
bottomLat = -26.00
leftLon = 25.75
rightLon = 26.15

##------Remove Outliers and Create Tessellation------

# Remove outliers by only keeping data within bounding box using: Select
selectedPoints = f"{scratch}\\{name}_Select.shp"
bounds = f""" Latitude < {topLat} AND
              Latitude > {bottomLat} AND 
              Longitude > {leftLon} AND 
              Longitude < {rightLon} 
          """
arcpy.analysis.Select(in_features= dataset, 
                      out_feature_class= selectedPoints, 
                      where_clause= bounds)

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

##------Find Hotspots------

# Calculate total count per hexagon using: Summarize Within
dataHotspot = f"{output}\\{name}_Hotspots.shp"
arcpy.analysis.SummarizeWithin(hexGrid, #input polygons
                               selectedPoints, #input features
                               dataHotspot, #output file 
                               "", "", "", #skip some options
                               "SQUAREKILOMETERS")

# Check the spatial reference of hexGrid and selectedPoints to make sure they match
hexGrid_desc = arcpy.Describe(hexGrid)
selectedPoints_desc = arcpy.Describe(selectedPoints)

# Print out spatial references to ensure they match
print(f"hexGrid Spatial Reference: {hexGrid_desc.spatialReference.name}")
print(f"selectedPoints Spatial Reference: {selectedPoints_desc.spatialReference.name}")

# Process: Minimum Bounding Geometry (Minimum Bounding Geometry) (management)
Merged_OrphEle_MCP = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\BassConnections_OrphanHotspots.gdb\\Merged_OrphEle_MCP"
with arcpy.EnvManager(extent="24.5232215310188 -16.5104707575485 27.0014261251794 -14.9065151970758 GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]]"):
    arcpy.management.MinimumBoundingGeometry(in_features=Merged_OrphEle_NoOutliers_shp, out_feature_class=Merged_OrphEle_MCP, geometry_type="CONVEX_HULL")





