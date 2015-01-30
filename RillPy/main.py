#! /usr/bin/env python
#coding=utf-8
"""
@Created   : 2015-1-6
@Revised   : 2015-1-28 Divided into seperate files for better version control
          
@author    : Liangjun Zhu
@summary   : Delineating and Extracting hillslopes and real rill from DEM.
@param     : DEMsrc, rootdir, streamTHR
@requires  : ArcGIS 10.x, gdal, Scipy
@references: Detail information will be found in README.txt.
@contract  : zlj@lreis.ac.cn
"""
import os
import Util
import Subbasin
import Hillslope
import Rill
import ShoulderLine

if __name__ == '__main__':
    ## Input params
    DEMsrc = r'E:\MasterBNU\RillMorphology\test\testdem'
    rootdir = r'E:\MasterBNU\RillMorphology\20150130'
    streamTHR = 0.01

    ## Run algorithms
    tempDir,PreprocessDir,RillExtDir,StatsDir = Util.makeResultFolders(rootdir)
#    DEMbuf,DEMfil,SlopeFile,AspectFile,FlowDirFile,FlowAccFile,CurvProfFile,CurvPlanFile = Util.UtilHydroFiles(DEMsrc, PreprocessDir)
#    StreamFile,StreamOrderFile,WatershedFile = Subbasin.GenerateStreamNetByTHR(DEMbuf,FlowDirFile,FlowAccFile,streamTHR,tempDir)
#    Subbasin.RillIndexCalc(StreamOrderFile,DEMbuf,tempDir,StatsDir)

    HillslpFile = RillExtDir + os.sep + "HillSlp.asc"
    #Hillslope.DelineateHillslopes(StreamFile,FlowDirFile,HillslpFile)    

    DEMfil = PreprocessDir + os.sep + "DEMfil"
    StreamFile = tempDir + os.sep + "StreamLinks"
    WatershedFile = tempDir + os.sep + "watershed"
    AspectFile = PreprocessDir + os.sep + "aspect"
    SlopeFile = PreprocessDir + os.sep + "slope"
    CurvProfFile = PreprocessDir + os.sep + "curvprof"
    FlowDirFile = PreprocessDir + os.sep + "flowdir"
    FlowAccFile = PreprocessDir + os.sep + "flowacc"
    
    Rill.UpStreamRoute(WatershedFile,HillslpFile,StreamFile,FlowDirFile,RillExtDir)
    #Rill.IdentifyRillRidges(HillslpFile,StreamFile,FlowDirFile,FlowAccFile,WatershedFile,DEMfil,RillExtDir)
    
    #alpha = 25
    #beta = 5
    #ShoulderPtsOrig = RillExtDir + os.sep + "ShoulderPtsOrig.asc"
    #ShoulderLine.IdentifyRillShoulderPts(AspectFile,SlopeFile,CurvProfFile,alpha,beta,ShoulderPtsOrig)
    #num = 50
    #ShoulderPts = RillExtDir + os.sep + "ShoulderPts.asc"
    #Util.RemoveLessPts(ShoulderPtsOrig,num,ShoulderPts)
    #Basin = PreprocessDir + os.sep + "basin"
    #Watershed = tempDir + os.sep + "watershed"
    #basinID = [1,4,25,26]
    #BasinBoundary = PreprocessDir + os.sep + "basinBounday.asc"
    #Subbasin.ExtractBasinBoundary(Basin,basinID,BasinBoundary)
    #Shoulder = RillExtDir + os.sep + "Shoulder.asc"
    #ShoulderLine.RillShoulderSegement(BasinBoundary,FlowDirFile,ShoulderPts,Shoulder)
    #ShoulderLine.RillShoulder(Watershed,FlowDirFile,ShoulderPts,tempDir,Shoulder)