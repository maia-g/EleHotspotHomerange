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
dataset = arcpy.GetParameterAsText(0) #User input in ArcPro
scratch = arcpy.GetParameterAsText(1) #Sets scratch workspace where most interim model outputs will go
gdb = arcpy.GetParameterAsText(2) #Sets geodatabase where important outputs from model will go
# dataset = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx" 
# scratch = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Scratch"
# gdb = "V:\\859FinalProject_mhg29\\Final859_mhg29\\Final859_mhg29.gdb"
name = (os.path.basename(dataset).split('_')[0] + "_" + 
        "_".join(os.path.basename(dataset).split('_')[3:]).split('.')[0])  
    #Save only the ele name and the months of data
#print(name)

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

# Check the spatial reference of the new shapefile and project if needed
dsc_points = arcpy.da.Describe(dataset_points)
spaRef = dsc_points['spatialReference'].name

if spaRef == "WGS_1984_UTM_Zone_35S":
    arcpy.AddMessage(f"The new points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
    print(f"The new points shapefile Coordinate System is:{dsc_points['spatialReference'].name}")
else:
    arcpy.management.Project(in_dataset= dataset_points,
                             out_dataset= dataset_points,
                             out_coor_system = "WGS_1984_UTM_Zone_35S")
    
    arcpy.AddMessage(f"The points file was reprojected to: {dsc_points['spatialReference'].name}")
    print(f"The new points file was reprojected to: {dsc_points['spatialReference'].name}")

##------Create Polyline from Points File------

# Convert points into polyline file and save to Geodatabase using: Coordinate Table to Point
dataset_lines = f"{gdb}\\{name}_Lines"
arcpy.defense.CoordinateTableToPolyline(
    in_table= dataset_points,
    out_feature_class= dataset_lines,
    x_or_lon_field="Longitude",
    in_coordinate_format="DD_2",
    y_or_lat_field="Latitude",
    line_group_field="Tag",
    sort_field="Time_Stamp",
    coordinate_system= arcpy.SpatialReference(32735)
)

###### MAYBE TRY WITH POINT TO LINE TOOL INSTEAD####
arcpy.management.PointsToLine(
    Input_Features="kavala_Sept_Nov_Points",
    Output_Feature_Class=r"V:\859FinalProject_mhg29\Final859_mhg29\Final859_mhg29.gdb\kavala_Sept_Nov_LinesNEWTOOL",
    Line_Field="Tag",
    Sort_Field="Time_Stamp",
    Close_Line="NO_CLOSE",
    Line_Construction_Method="TWO_POINT",
    Attribute_Source="BOTH_ENDS",
    Transfer_Fields="Latitude;Longitude;Time_Stamp;Date;Time;Month;Log_Interv;Speed;Temperatur;Movement;Accelerome"
)



