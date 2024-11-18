# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-11-18 11:42:06
"""
import arcpy

def ComboOrphEleHotspot():  # Combined Orphaned Ele Hotspot

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx")
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Analysis Tools.tbx")
    # Model Environment settings
    with arcpy.EnvManager(scratchWorkspace="R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch", workspace="R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch"):
        Batoka_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$"
        Chama_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$"
        kavala_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$"
        Mosi_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$"
        Muso_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$"
        Rufunsa_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$"
        Tafika_move_SubsetDry_Sept_Nov_ = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$"

        # Process: Generate Tessellation (2) (Generate Tessellation) (management)
        GenerateTessellation_MG_shp = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch\\GenerateTessellation_MG.shp"
        arcpy.management.GenerateTessellation(Output_Feature_Class=GenerateTessellation_MG_shp, Extent="25.7710469 -16.2966702309534 26.3 -15.322087 GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]]", Shape_Type="HEXAGON", Size="866025.4 SquareMeters", Spatial_Reference="GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision", H3_Resolution=7)

        # Process: Merge (Merge) (management)
        Merged_OrphEle_Excel_shp = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch\\Merged_OrphEle_Excel.dbf"
        arcpy.management.Merge(inputs=[Batoka_move_SubsetDry_Sept_Nov_, Chama_move_SubsetDry_Sept_Nov_, kavala_move_SubsetDry_Sept_Nov_, Mosi_move_SubsetDry_Sept_Nov_, Muso_move_SubsetDry_Sept_Nov_, Rufunsa_move_SubsetDry_Sept_Nov_, Tafika_move_SubsetDry_Sept_Nov_], output=Merged_OrphEle_Excel_shp, field_mappings="Tag \"Tag\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Tag,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Tag,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Tag,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Tag,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Tag,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Tag,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Tag,0,254;Latitude \"Latitude\" true true false 8 Double 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Latitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Latitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Latitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Latitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Latitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Latitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Latitude,-1,-1;Longitude \"Longitude\" true true false 8 Double 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Longitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Longitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Longitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Longitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Longitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Longitude,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Longitude,-1,-1;Type \"Type\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Type,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Type,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Type,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Type,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Type,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Type,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Type,0,254;Time_Stamp \"Time#Stamp\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Time_Stamp,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Time_Stamp,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Time_Stamp,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Time_Stamp,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Time_Stamp,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Time_Stamp,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Time_Stamp,0,254;Date \"Date\" true true false 8 Date 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Date,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Date,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Date,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Date,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Date,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Date,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Date,-1,-1;Time \"Time\" true true false 8 Date 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Time,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Time,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Time,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Time,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Time,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Time,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Time,-1,-1;Month \"Month\" true true false 8 Double 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Month,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Month,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Month,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Month,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Month,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Month,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Month,-1,-1;Log_Interval \"Log#Interval\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Log_Interval,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Log_Interval,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Log_Interval,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Log_Interval,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Log_Interval,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Log_Interval,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Log_Interval,0,254;DOP \"DOP\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,DOP,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,DOP,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,DOP,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,DOP,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,DOP,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,DOP,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,DOP,0,254;Speed \"Speed\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Speed,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Speed,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Speed,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Speed,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Speed,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Speed,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Speed,0,254;Battery \"Battery\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Battery,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Battery,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Battery,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Battery,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Battery,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Battery,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Battery,0,254;Temperature \"Temperature\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Temperature,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Temperature,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Temperature,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Temperature,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Temperature,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Temperature,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Temperature,0,254;Movement \"Movement\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Movement,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Movement,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Movement,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Movement,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Movement,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Movement,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Movement,0,254;Accelerometer \"Accelerometer\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Accelerometer,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Accelerometer,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Accelerometer,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Accelerometer,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Accelerometer,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Accelerometer,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Accelerometer,0,254;RSSI \"RSSI\" true true false 8 Double 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,RSSI,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,RSSI,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,RSSI,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,RSSI,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,RSSI,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,RSSI,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,RSSI,-1,-1;Coverage \"Coverage\" true true false 255 Text 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Coverage,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Coverage,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Coverage,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Coverage,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Coverage,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Coverage,0,254,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Coverage,0,254;Retries \"Retries\" true true false 8 Double 0 0,First,#,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Batoka_move_SubsetDry_Sept_Nov.xlsx\\Batoka_move_SubsetDry_Sept_Nov$,Retries,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Chama_move_SubsetDry_Sept_Nov.xlsx\\Chama_move_SubsetDry_Sept_Nov$,Retries,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\kavala_move_SubsetDry_Sept_Nov.xlsx\\kavala_move_SubsetDry_Sept_Nov$,Retries,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Mosi_move_SubsetDry_Sept_Nov.xlsx\\Mosi_move_SubsetDry_Sept_Nov$,Retries,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Muso_move_SubsetDry_Sept_Nov.xlsx\\Muso_move_SubsetDry_Sept_Nov$,Retries,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Rufunsa_move_SubsetDry_Sept_Nov.xlsx\\Rufunsa_move_SubsetDry_Sept_Nov$,Retries,-1,-1,R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Data\\Orphan_Ele_Movement_Data\\Tafika_move_SubsetDry_Sept_Nov.xlsx\\Tafika_move_SubsetDry_Sept_Nov$,Retries,-1,-1")

        # Process: XY Table To Point (XY Table To Point) (management)
        EleMovementDataCombinedSubsetDry_ExcelToTable1_XYTableToPoint2_shp = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch\\Merged_OrphEle_Excel_XYTableToPoint6.shp"
        arcpy.management.XYTableToPoint(in_table=Merged_OrphEle_Excel_shp, out_feature_class=EleMovementDataCombinedSubsetDry_ExcelToTable1_XYTableToPoint2_shp, x_field="Longitude", y_field="Latitude", coordinate_system="GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

        # Process: Project (Project) (management)
        Merged_OrphEleNEW_shp = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch\\Merged_OrphEleNEW.shp"
        arcpy.management.Project(in_dataset=EleMovementDataCombinedSubsetDry_ExcelToTable1_XYTableToPoint2_shp, out_dataset=Merged_OrphEleNEW_shp, out_coor_system="PROJCS[\"WGS_1984_UTM_Zone_35S\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",10000000.0],PARAMETER[\"Central_Meridian\",27.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]")

        # Process: Select (Select) (analysis)
        Merged_OrphEle_NoOutliers_shp = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\Scratch\\Merged_OrphEle_NoOutliers.shp"
        arcpy.analysis.Select(in_features=Merged_OrphEleNEW_shp, out_feature_class=Merged_OrphEle_NoOutliers_shp, where_clause="Latitude < -15.55")

        # Process: Summarize Within (Summarize Within) (analysis)
        Merged_OrphEle_Hotspots = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\BassConnections_OrphanHotspots.gdb\\Merged_OrphEle_Hotspots"
        Output_Grouped_Table = ""
        arcpy.analysis.SummarizeWithin(in_polygons=GenerateTessellation_MG_shp, in_sum_features=Merged_OrphEle_NoOutliers_shp, out_feature_class=Merged_OrphEle_Hotspots, shape_unit="SQUAREKILOMETERS", out_group_table=Output_Grouped_Table)

        # Process: Minimum Bounding Geometry (Minimum Bounding Geometry) (management)
        Merged_OrphEle_MCP = "R:\\Wildlife\\GIS\\Batoka_Maia\\BassConnections_OrphanHotspots\\BassConnections_OrphanHotspots.gdb\\Merged_OrphEle_MCP"
        with arcpy.EnvManager(extent="24.5232215310188 -16.5104707575485 27.0014261251794 -14.9065151970758 GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]]"):
            arcpy.management.MinimumBoundingGeometry(in_features=Merged_OrphEle_NoOutliers_shp, out_feature_class=Merged_OrphEle_MCP, geometry_type="CONVEX_HULL")

if __name__ == '__main__':
    ComboOrphEleHotspot()
