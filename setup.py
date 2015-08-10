#! /usr/bin/env python

from setuptools import setup, find_packages
import glob, versioneer

setup (
    name = "jsonpath_flatten",
    version = versioneer.get_version (),
    description = "Flatten a dictionary into a single layer with JSONPath keys",
    long_description = file ("README.rst").read (),
    cmdclass = versioneer.get_cmdclass (),
    classifiers = [
      "Development Status :: 4 - Beta",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: "
      + "GNU Lesser General Public License v3 or later (LGPLv3+)",
      "Topic :: Utilities",
    ],
    keywords = "celery event logger",
    author = "J C Lawrence",
    author_email = "claw@kanga.nu",
    url = "https://github.com/clearclaw/jsonpath_flatten",
    license = "LGPL v3",
    test_suite = "tests",
    packages = find_packages (exclude = ["tests",]),
    package_data = {},
    data_files = [],
    zip_safe = False,
    install_requires = [line.strip ()
                        for line in file ("requirements.txt").readlines ()],
    entry_points = {
        "console_scripts": [],
    },
)
