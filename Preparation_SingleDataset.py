##---------------------------------------------------------------------
## Preparation_SingleDataset.py
##
## Description: Select data to be prepared for hot spot analysis
##
## Usage: Transform Excel to Table (.dbf), make points from the XY coordinates, and project.
##
## Created: Fall 2024
## Author: maia.griffith@duke.edu (for ENV859)
##---------------------------------------------------------------------

##------Set Up------

# Load relevant packages
import sys
import arcpy

# Allow user input for scratch workspace, output workspace, and dataset.
##### UNCOMMENT BELOW WHEN READY TO GO IN ARCPRO###############
# dataset = arcpy.GetParameterAsText(0) #User input in ArcPro
# scratch = arcpy.GetParameterAsText(1) #Sets scratch workspace where most interim model outputs will go
# output = arcpy.GetParameterAsText(2) #Sets output workspace where important outputs from model will go
dataset = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx" 
scratch = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Scratch"
output = "V:\\859FinalProject_mhg29\\BassConnections_OrphanHotspots\\Outputs"

# Set environment settings
arcpy.env.overwriteOutput = True #Make sure to exit interaction window in VS Code before re-running code
arcpy.EnvManager(scratchWorkspace= scratch, workspace= output)

# Create a describe object with the dataset
dsc = arcpy.da.Describe(dataset) #Creating the "Describe" object
##print(dsc.keys()) #Uncomment to see keys

# Indicate catalogPath directory
arcpy.AddMessage(f"The dataset's catalog path is: {dsc['catalogPath']}")