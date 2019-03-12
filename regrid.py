from netCDF4 import Dataset as nc

print('#!/bin/bash')
f=open("fn.txt","r")
fns=f.read().splitlines()
for fn in fns:
   var=fn.split("_",1)[0]
   print("# variable is "+var)
   # check if vertical dimension exists (depth, z)
   dataset=nc(fn)
   dims=dataset.dimensions.keys()
   if "deptht" in dims:
       is3d=True
   elif "depthu" in dims:
       is3d=True
   elif "depthv" in dims:
       is3d=True
   elif "depth" in dims:
       is3d=True
   elif "lev" in dims:
       is3d=True
   elif "olevel" in dims:
       is3d=True
   else:
       is3d=False
   wn0=fn+"_tmp.nc"
   com0="cdo remapbil,grd.txt "+fn+" "+wn0
   if is3d:
       wn=fn+"_2x2L33_monthly.nc"
       wn1=fn+"_2x2L33_yearly.nc"
       print("# this is a 3d field, is3d="+str(is3d))
       com1="cdo intlevel,5,10,20,30,50,75,100,125,150,200,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500 "+wn0+" "+wn
   else:
       wn=fn+"_2x2L1_monthly.nc"
       wn1=fn+"_2x2L1_yearly.nc"
       com1="mv "+wn0+" "+wn
       print("# this is a 2d field,is3d="+str(is3d))
   com2="cdo yearmean "+wn+" "+wn1
   com3="rm "+wn0
   print(com0)
   print(com1)
   print(com2)
   if is3d == 1:
       print(com3)

