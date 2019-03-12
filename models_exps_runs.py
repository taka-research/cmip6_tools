import numpy as np
from subprocess import call
import os

#######################################
# make a list of all yearly netcdf files
dummy=os.system("ls *yearly.nc > fn.txt")
f=open("fn.txt","r")
fs=f.read().splitlines()
f.close()
# start loop over each file
N=np.size(fs)
for n in range(0,N):
    mod=fs[n].split("_")[2]
    exp=fs[n].split("_")[3]
    run=fs[n].split("_")[4]
    dir1=mod+"/"+exp+"/"+run
    # create permanent disk space for monthly and yearly data
    os.system("mkdir -p /nv/hp5/takamitsu3/data2/CMIP6/"+dir1)
    os.system("mv "+fs[n]+" /nv/hp5/takamitsu3/data2/CMIP6/"+dir1+"/.")

#######################################
# make a list of all monthly netcdf files
dummy=os.system("ls *monthly.nc > fn.txt")
f=open("fn.txt","r")
fs=f.read().splitlines()
f.close()
# start loop over each file
N=np.size(fs)
for n in range(0,N):
    mod=fs[n].split("_")[2]
    exp=fs[n].split("_")[3]
    run=fs[n].split("_")[4]
    dir1=mod+"/"+exp+"/"+run
    os.system("mv "+fs[n]+" /nv/hp5/takamitsu3/data2/CMIP6/"+dir1+"/.")

#######################################
# make a list of remaining netcdf files
dummy=os.system("ls *.nc > fn.txt")
f=open("fn.txt","r")
fs=f.read().splitlines()
f.close()
# start loop over each file
N=np.size(fs)
for n in range(0,N):
    mod=fs[n].split("_")[2]
    exp=fs[n].split("_")[3]
    run=fs[n].split("_")[4]
    dir1=mod+"/"+exp+"/"+run
    dir2="/nv/hp5/takamitsu3/scratch/CMIP6/"+dir1
    os.system("mkdir -p "+dir2)
    os.system("mv "+fs[n]+" "+dir2+"/.")

