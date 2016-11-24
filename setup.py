#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Panu Lahtinen

# Author(s):

#   Panu Lahtinen <plahtine@ursa.fi>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Setup for tilipullo
"""
from setuptools import setup
import imp

version = imp.load_source('laga.version', 'laga/version.py')

setup(name="laga",
      version=version.__version__,
      description='tilipullo - laga',
      author='Martin Raspaud',
      author_email='plahtine@ursa.fi',
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v3 " +
                   "or later (GPLv3+)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Scientific/Engineering"],
      url="https://github.com/pnuu/tilipullo",
      packages=['laga', ],
      scripts=[],
      data_files=[],
      zip_safe=False,
      install_requires=['pyyaml', ],
      # tests_require=['mock'],
      # test_suite='laga.tests.suite',
      )
