#
# Copyright (c) Dell Inc., or its subsidiaries. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

from setuptools import setup

setup(
    name='p3_test_driver',
    version='2.0.3',
    description='P3 Test Driver is designed to run a variety of benchmarks using an easily expandable plug-in system.',
    url='http://github.com/pravega/p3_test_driver',
    author='Claudio Fahey',
    author_email='claudio.fahey@dell.com',
    packages=['p3_test_driver'],
    package_data={
        'p3_test_driver': ['plugins/*.py'],
    },
    install_requires=[
        'requests',
        'six',
        'PyYaml',
        'yapsy',
    ],
    entry_points={
        'console_scripts': [
            'p3_test_driver = p3_test_driver.p3_test_driver:main',
        ],
    },
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
