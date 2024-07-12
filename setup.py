#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup

directory = Path(__file__).resolve().parent

setup(name='logipy',
      version='0.0.1',
      description='logic simulator',
      author='Dominik Kormann',
      license='MIT',

      packages = ['logic'],
      classifiers=[
        "Programming Language :: Python :: 3",
      ],
      install_requires=[],
      python_requires='>=3.8',
      extras_require={},
      include_package_data=True)
