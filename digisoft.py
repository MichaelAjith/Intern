# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:57:16 2019

@author: Mykill
"""

import dicom
import pylab
#path to file
dFile1=dicom.read_file("ttfm.dcm")
dFile2=dicom.read_file("bmode.dcm") 
# pylab readings and conversion
pylab.imshow(dFile1.pixel_array,cmap=pylab.cm.bone) 
pylab.imshow(dFile2.pixel_array,cmap=pylab.cm.bone) 
 #Display
pylab.show()