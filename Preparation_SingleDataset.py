##---------------------------------------------------------------------
## Preparation_SingleDataset.py
##
## Description: Select data to be prepared for hot spot analysis
##
## Usage: Transform Excel to Table (.dbf), make points from the XY coordinates,
# #       and check the coordinate system.
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
# dataset = arcpy.GetParameterAsText(0) #User input in ArcPro
# scratch = arcpy.GetParameterAsText(1) #Sets scratch workspace where most interim model outputs will go
# output = arcpy.GetParameterAsText(2) #Sets output workspace where important outputs from model will go
dataset = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx" 
scratch = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Scratch"
output = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\BassConnections_OrphanHotspots.gdb"
name = os.path.splitext(os.path.basename(dataset))[0] #Save only the base file name

# Set environment settings
arcpy.env.overwriteOutput = True #Make sure to exit interaction window in VS Code before re-running code
arcpy.EnvManager(scratchWorkspace= scratch, workspace= output)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##------Check Path------

# Create a describe object with the dataset
dsc_dataset = arcpy.da.Describe(dataset) #Creating the "Describe" object
###print(dsc.keys()) #Uncomment to see keys

# Indicate catalogPath directory
arcpy.AddMessage(f"The dataset's catalog path is: {dsc_dataset['catalogPath']}")
arcpy.AddMessage(f"The outputs path is: {output}")
arcpy.AddMessage(f"The scratch folder path is: {scratch}")
###print(f"The dataset's catalog path is: {dsc['catalogPath']}")

##------Begin Processing------

# Convert selected data set using: Excel To Table
Output_Table = f"{scratch}\\{name}_Table.dbf"
arcpy.conversion.ExcelToTable(Input_Excel_File= dataset, Output_Table= Output_Table)

# Convert new table into points and save to Outputs folder using: XY Table To Point
dataset_points = f"{output}\\{name}_Points.shp"
arcpy.management.XYTableToPoint(in_table= Output_Table, 
                                out_feature_class= dataset_points, 
                                x_field="Longitude", y_field="Latitude")

    # Check the spatial reference of the new shapefile
dsc_points = arcpy.da.Describe(dataset_points)
arcpy.AddMessage(f"The new points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
#print(f"The new points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
