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