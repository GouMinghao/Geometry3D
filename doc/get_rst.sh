pip install ..
cd ..
python run_tests.py
cd doc
rm source/Geometry3D.*
rm source/modules.rst
sphinx-apidoc -o ./source ../Geometry3D
make html
make latex