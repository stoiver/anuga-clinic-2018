#!/bin/bash

cd /content

echo "Install Dependencies"
echo "   Install nose via pip"
pip -q install nose  > /dev/null 2>&1 

echo "   Install gitpython via pip"
pip -q install gitpython  > /dev/null 2>&1 

echo "   Install pyproj via pip"
pip -q install pyproj  > /dev/null 2>&1 

echo "   Install gdal via apt-get"
apt-get -q -y install python-gdal gdal-bin  > /dev/null 2>&1 

echo "   Install netcdf4 via apt-get"
apt-get -q -y install python-netcdf4  > /dev/null 2>&1 

echo "   Install netcdf4 via pip"
pip -q install netCDF4 > /dev/null 2>&1 

echo "(2) Download anuga_core github repository"
git clone --quiet https://github.com/anuga-community/anuga_core.git  > /dev/null 2>&1 

echo "(3) Install anuga"

cd anuga_core
python setup.py --quiet install  > /dev/null 2>&1 
cd ../

echo "(4) Ready to go"
