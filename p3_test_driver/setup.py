
from setuptools import setup

setup(
    name='p3_test_driver',
    version='0.1',
    description='P3 Test Driver is designed to run a variety of benchmarks using an easily expandble plug-in system.',
    url='http://github.com/claudiofahey/p3_test_driver',
    author='Claudio Fahey',
    author_email='claudiofahey@gmail.com',
    packages=['p3_test_driver'],
    install_requires=[
        'six',
        'PyYaml',
        'yapsy',
    ],
    entry_points = {
        'console_scripts': [
            'p3_test_driver = p3_test_driver.p3_test_driver:main',
        ],
    },
    zip_safe=False,
)