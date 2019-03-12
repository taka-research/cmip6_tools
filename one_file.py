import os
import subprocess
import glob

# creates 1 file for all yearly data and for each variable for monthly data 
model="IPSL-CM6A-LR"
exp="1pctCO2"
run="r1i1p1f1"

#------------------------------
vars3d=["agessc","chl","dfe","dissic","ph","o2","po4","pp","no3","thetao","so","uo","vo"]
vars2d=["chlos","fgco2","dpco2","fgo2","epc100","epcalc100","tos","zos"]
dir="/nv/hp5/takamitsu3/data2/CMIP6/"+model+"/"+exp+"/"+run+"/"

for v in vars3d:
   print("# working on "+v)
   nf=glob.glob(dir+v+"*yearly.nc")
   wf=dir+v+"_Oyr_"+model+"_"+exp+"_"+run+"_2x2L33.nc" 
#   wfm=dir+v+"_"+model+"_"+exp+"_"+run+"_2x2L33_mon.nc" 
   if len(nf) > 1:
      print("# there are multiple files, combining into one")
      com="cdo -O mergetime "+dir+v+"_*yearly.nc"+" "+wf
      os.system(com)  
# Do not mergetime monthly fields
#      com="cdo -O mergetime "+dir+v+"_*monthly.nc"+" "+wfm
#      os.system(com)  
   else:
      print("# there is only single file")
      com="cp "+dir+v+"_*yearly.nc"+" "+wf
      os.system(com)
#      com="cp "+dir+v+"_*monthly.nc"+" "+wfm
#      os.system(com)

for v in vars2d:
   print("# working on "+v)
   nf=glob.glob(dir+v+"*yearly.nc") 
   wf=dir+v+"_Oyr_"+model+"_"+exp+"_"+run+"_2x2L33.nc" 
   wfm=dir+v+"_"+model+"_"+exp+"_"+run+"_2x2L33_mon.nc" 
   if len(nf) > 1:
      print("# there are multiple files, combining into one")  
      com="cdo -O mergetime "+dir+v+"_*yearly.nc"+" "+wf
      os.system(com)
      com="cdo -O mergetime "+dir+v+"_*monthly.nc"+" "+wfm
      os.system(com)
   else:
      print("# there is only single file")
      com="cp "+dir+v+"_*yearly.nc"+" "+wf
      os.system(com)
      com="cp "+dir+v+"_*monthly.nc"+" "+wfm
      os.system(com)

# finally combine all yearly output
out1file=dir+model+"_"+exp+"_"+run+"_2x2L33_ann.nc"
com="cdo -O merge "+dir+"*Oyr*.nc "+out1file
os.system(com)

# delete intermediate files
# Do not delete monthly fields - these are final products!
#dlist1=dir+"*_monthly.nc"
#com="rm "+dlist1
#os.system(com)
dlist2=dir+"*_yearly.nc"
com="rm "+dlist2
os.system(com)

