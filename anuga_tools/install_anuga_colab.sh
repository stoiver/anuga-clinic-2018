#!/bin/bash

cd /content

echo "(1) Install Dependencies"
echo "   Install pytest via pip"
pip -q install pytest  > /dev/null 2>&1 

echo "   Install gitpython via pip"
pip -q install gitpython  > /dev/null 2>&1 

echo "   Install pyproj via pip"
pip -q install pyproj  > /dev/null 2>&1 

echo "   Install gdal via apt-get"
apt-get -q -y install python-gdal gdal-bin  > /dev/null 2>&1 

echo "   Install python netcdf4 via apt-get"
apt-get -q -y install python-netcdf4  > /dev/null 2>&1 

echo "   Install netcdf4 via pip"
pip -q install netCDF4 > /dev/null 2>&1

echo "   Install meshpy via pip"
pip -q install meshpy > /dev/null 2>&1 

echo "   Install dill via pip"
pip -q install dill > /dev/null 2>&1 

echo "   Install pymetis via pip"
pip -q install pymetis > /dev/null 2>&1 

echo "   Install affine via pip"
pip -q install affine > /dev/null 2>&1

echo "   Install utm via pip"
pip -q install utm > /dev/null 2>&1

echo "   Install anuga via pip"
pip -q install anuga > /dev/null 2>&1

# echo "   Install meson-python via pip"
# pip -q install meson-python > /dev/null 2>&1 

# echo "   Install ninja via pip"
# pip -q install ninja > /dev/null 2>&1 

#echo "(2) Download anuga_core github repository"
#git clone --quiet https://github.com/anuga-community/anuga_core.git  > /dev/null 2>&1 

#echo "(3) Install anuga"

#cd anuga_core
#pip install --no-build-isolation .  
#cd ../

echo "(4) Ready to go"
