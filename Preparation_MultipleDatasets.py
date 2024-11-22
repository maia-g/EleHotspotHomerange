##---------------------------------------------------------------------
## Preparation_MultipleDatasets.py
##
## Description: Select multiple data files to be prepared for hot spot analysis
##
## Usage: Transform Excel to Table (.dbf), make points from the XY coordinates,
# #       and check the coordinate system of multiple files.
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
# datasets = arcpy.GetParameterAsText(0) #User input(s) in ArcPro
# scratch = arcpy.GetParameterAsText(1) #Sets scratch workspace where most interim model outputs will go
# gdb = arcpy.GetParameterAsText(2) #Sets geodatabase where important outputs from model will go
scratch = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Scratch"
gdb = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Final859_mhg29.gdb"

# Get the list of datasets (e.g., feature classes or shapefiles)
arcpy.env.workspace = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Data"
datasets = arcpy.ListFiles("*.xlsx") #.xlxs files only
print(datasets)
names = [] #create empty list
# Check if any datasets were selected
if datasets:
    arcpy.AddMessage(f"Number of datasets selected: {len(datasets)}")
   
    # Iterate through each selected dataset
    for dataset in datasets:
        arcpy.AddMessage(f"Processing dataset: {dataset}")
        
        # Save name of elephant and months of data
        name = (os.path.basename(dataset).split('_')[0] + "_" + 
        "_".join(os.path.basename(dataset).split('_')[3:]).split('.')[0])  
        
        # Append extracted name to full list "names"
        names.append(name)
        

else:
    arcpy.AddError("No datasets were selected!")

# Print list of collected names
arcpy.AddMessage(f"All extracted names: {names}")
print(f"All extracted names: {names}")




name = (os.path.basename(dataset).split('_')[0] + "_" + 
        "_".join(os.path.basename(dataset).split('_')[3:]).split('.')[0])  
    #Save only the ele name and the months of data
print(name)

# Set environment settings
arcpy.env.overwriteOutput = True #Make sure to exit interaction window in VS Code before re-running code
arcpy.EnvManager(scratchWorkspace= scratch, workspace= gdb)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##------Check Path------

# Create a describe object with the dataset
dsc_dataset = arcpy.da.Describe(dataset) #Creating the "Describe" object
###print(dsc.keys()) #Uncomment to see keys

# Indicate catalogPath directory
arcpy.AddMessage(f"The dataset's catalog path is: {dsc_dataset['catalogPath']}")
arcpy.AddMessage(f"The geodatabase path is: {gdb}")
arcpy.AddMessage(f"The scratch folder path is: {scratch}")
###print(f"The dataset's catalog path is: {dsc_dataset['catalogPath']}")

##------Begin Processing------

# Convert selected data set using: Excel To Table
Output_Table = f"{scratch}\\{name}_Table.dbf"
arcpy.conversion.ExcelToTable(Input_Excel_File= dataset, Output_Table= Output_Table)

# Convert new table into points and save to Scratch folder using: XY Table To Point
dataset_points = f"{scratch}\\{name}_Points.shp"
arcpy.management.XYTableToPoint(in_table= Output_Table, 
                                out_feature_class= dataset_points, 
                                x_field="Longitude", y_field="Latitude")

    # Check the spatial reference of the new shapefile
dsc_points = arcpy.da.Describe(dataset_points)
arcpy.AddMessage(f"The new points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
###print(f"The new points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
