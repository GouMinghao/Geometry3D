pip install ..
cd ..
python run_tests.py
cd docs
rm source/Geometry3D.*
rm source/modules.rst
sphinx-apidoc -o ./source ../Geometry3D
make clean
make html
make latex
cd build/latex
make
