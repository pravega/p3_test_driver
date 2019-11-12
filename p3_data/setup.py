
from setuptools import setup

setup(
    name='p3_data',
    version='0.1',
    description='A variety of utility functions to analyze results data produced by the P3 Test Driver.',
    url='http://github.com/claudiofahey/p3_test_driver',
    author='Claudio Fahey',
    author_email='claudio.fahey@dell.com',
    packages=['p3_data'],
    install_requires=[
        'IPython',
        'ipywidgets',
        'pandas',
        'PyYaml',
        'matplotlib',
        'numpy',
        'scipy',
        'six',
        'sklearn',
    ],
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
