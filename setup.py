# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def read(name):
    with open(name, "r") as fd:
        return fd.read()

setup(
        name="shape3d",
        version="0.0.1",

        description="a 3d geometry lib",
        long_description=read("README.md"),

        url="http://github.com/GouMinghao/shape3d",

        author="Daniel Schadt",
        author_email="gouminghao@gmail.com",

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

        keywords="analytic geometry 3d",

        install_requires=['matplotlib','numpy'],
)
