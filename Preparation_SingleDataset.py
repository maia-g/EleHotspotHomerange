##---------------------------------------------------------------------
## Preparation_SingleDataset.py
##
## Description: Select data to be prepared for hot spot analysis
##
## Usage: Transform Excel to Table (.dbf), make points from the XY coordinates,
# #       check the coordinate system, and make line file from points.
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
dataset = arcpy.GetParameterAsText(0) #User input in ArcPro
scratch = arcpy.GetParameterAsText(1) #Sets scratch workspace where most interim model outputs will go
gdb = arcpy.GetParameterAsText(2) #Sets geodatabase where important outputs from model will go
name = (os.path.basename(dataset).split('_')[0] + "_" + 
        "_".join(os.path.basename(dataset).split('_')[3:]).split('.')[0])  
    #Save only the ele name and the months of data

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.EnvManager(scratchWorkspace= scratch, workspace= gdb)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##------Check Path------

# Create a describe object with the dataset
dsc_dataset = arcpy.da.Describe(dataset) #Creating the "Describe" object
###print(dsc.keys()) #Uncomment to see keys if desired (for potential future tool use)

# Indicate catalogPath directory
arcpy.AddMessage(f"The dataset's catalog path is: {dsc_dataset['catalogPath']}")
arcpy.AddMessage(f"The geodatabase path is: {gdb}")
arcpy.AddMessage(f"The scratch folder path is: {scratch}")

##------Begin Processing------

# Convert selected data set using: Excel To Table
Output_Table = f"{scratch}\\{name}_Table.dbf"
arcpy.conversion.ExcelToTable(Input_Excel_File= dataset, 
                              Output_Table= Output_Table)

# Convert new table into points and save to Scratch folder using: XY Table To Point
dataset_points = f"{scratch}\\{name}_Points.shp"
arcpy.management.XYTableToPoint(in_table= Output_Table, 
                                out_feature_class= dataset_points, 
                                x_field="Longitude", y_field="Latitude")

# Check the spatial reference of the new shapefile and project if needed
dsc_points = arcpy.da.Describe(dataset_points)
spaRef = dsc_points['spatialReference'].name

if spaRef == "WGS_1984_UTM_Zone_35S":
    arcpy.AddMessage(f"The new points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
else:
    arcpy.management.Project(in_dataset= dataset_points,
                             out_dataset= dataset_points,
                             out_coor_system = "WGS_1984_UTM_Zone_35S")
    
    arcpy.AddMessage(f"The points file was reprojected to: {dsc_points['spatialReference'].name}")

##------Create Line from Points File------

# Convert points into line file and save to Geodatabase using: Points to Line
dataset_lines = f"{gdb}\\{name}_Lines"
arcpy.management.PointsToLine(
    Input_Features= dataset_points,
    Output_Feature_Class= dataset_lines,
    Line_Field="Tag",
    Sort_Field="Time_Stamp",
    Close_Line="NO_CLOSE",
    Line_Construction_Method="TWO_POINT",
    Attribute_Source="BOTH_ENDS",
    Transfer_Fields="Latitude;Longitude;Time_Stamp;Date;Month;Log_Interv;Speed;Temperatur;Movement;Accelerome"
)


