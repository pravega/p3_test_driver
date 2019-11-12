
from setuptools import setup

setup(
    name='p3_test_driver',
    version='2.0',
    description='P3 Test Driver is designed to run a variety of benchmarks using an easily expandable plug-in system.',
    url='http://github.com/claudiofahey/p3_test_driver',
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
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
