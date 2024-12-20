##---------------------------------------------------------------------
## Preparation_MultipleDatasets.py
##
## Description: Select multiple data files to be prepared for hot spot analysis
##
## Usage: Transform Excel to Table (.dbf), make points from the XY coordinates,
# #       check the coordinate system, and make line file from points of multiple inputs.
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
dataInputs = arcpy.GetParameterAsText(0) #User input(s) in ArcPro
scratch = arcpy.GetParameterAsText(1) #Sets scratch workspace where most interim model outputs will go
gdb = arcpy.GetParameterAsText(2) #Sets geodatabase where important outputs from model will go
suffix = arcpy.GetParameterAsText(3) #Get user input for suffix to attach to Merge name

# Set up environment
arcpy.env.overwriteOutput = True
arcpy.EnvManager(scratchWorkspace= scratch, workspace= gdb)
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS_1984_UTM_Zone_35S")

##------Convert Datasets------

# Make the user input into a list of datasets
datasets = dataInputs.split(';')

names = [] #create empty list for indiv names
tables = [] #create empty list to hold converted table names

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
        
        # Convert selected data set using: Excel To Table
        Output_Table = f"{scratch}\\{name}_Table.dbf"
        arcpy.conversion.ExcelToTable(Input_Excel_File= dataset, 
                                      Output_Table= Output_Table)
        tables.append(Output_Table)

        # Print message to confirm excel to table is working
        arcpy.AddMessage(f"Converted {dataset} to table: {Output_Table}")

else:
    arcpy.AddError("No datasets were selected!")

##------Merge Datasets------

# Merge datasets into one combined dataset
dataMerge = f"{scratch}\\Merged_Table_{suffix}.dbf"
if tables:
    try:
        # Merge the datasets
        arcpy.management.Merge(tables, dataMerge)
        
        # Print message upon successful merge
        arcpy.AddMessage(f"Merge completed successfully. Output saved to: {dataMerge}")
        
    except Exception as e:
        # Handle any errors
        arcpy.AddError(f"Error during merge: {str(e)}")
else:
    arcpy.AddError("No datasets were selected to merge!")

##------Create Points from Merged File------

# Convert merged table into points and save to Scratch folder using: XY Table To Point
merged_points = f"{scratch}\\Merged_Points{suffix}.shp"
arcpy.management.XYTableToPoint(in_table= dataMerge, 
                                out_feature_class= merged_points, 
                                x_field="Longitude", y_field="Latitude")

# Check the spatial reference of the new shapefile and project if needed
dsc_points = arcpy.da.Describe(merged_points)
spaRef = dsc_points['spatialReference'].name

if spaRef == "WGS_1984_UTM_Zone_35S":
    # If the spatial reference is correct, print the name
    arcpy.AddMessage(f"The merged points shapefile Coordinate System is: {dsc_points['spatialReference'].name}")
else:
    # If the spatital reference is incorrect, reproject
    reprojected = f"{scratch}\\Merged_PointsNEW{suffix}.shp"
    arcpy.management.Project(in_dataset= merged_points,
                             out_dataset= reprojected,
                             out_coor_system = arcpy.SpatialReference(32735))
    
    # Print the new spatial reference information
    dsc_repro = arcpy.da.Describe(reprojected)
    arcpy.AddMessage(f"The merged points file was reprojected to: {dsc_repro['spatialReference'].name}")

##------Create Polyline from Points File------

# Convert points into line file and save to Geodatabase using: Points to Line
merged_lines = f"{gdb}\\Merged_Lines{suffix}"
arcpy.management.PointsToLine(
    Input_Features= merged_points,
    Output_Feature_Class= merged_lines,
    Line_Field="Tag",
    Sort_Field="Time_Stamp",
    Close_Line="NO_CLOSE",
    Line_Construction_Method="TWO_POINT",
    Attribute_Source="BOTH_ENDS",
    Transfer_Fields="Latitude;Longitude;Time_Stamp;Date;Month;Log_Interv;Speed;Temperatur;Movement;Accelerome"
)