# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def read(name):
    with open(name, "r") as fd:
        return fd.read()

setup(
        name="sgl",
        version="0.0.1",

        description="A small analytic geometry lib",
        long_description=read("README.md"),

        url="http://github.com/Kingdread/sgl",

        author="Daniel Schadt",
        author_email="daniel@kingdread.de",

        license="GPL",

        packages=find_packages(),
    
        classifiers=[
            "Developement Status :: 3 - Alpha",

            "Intended Audience :: Developers",
            "Intended Audience :: Education"

            "Topic :: Education",
            "Topic :: Scientific/Engineering :: Mathematics",

            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",

            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ],

        keywords="analytic geometry",

        install_requires=['matplotlib','numpy'],
)
