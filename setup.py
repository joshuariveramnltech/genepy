import re
from setuptools import setup, find_packages
from os.path import abspath, dirname, join

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 4 - Beta
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python :: 3
'''.strip().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name                                = 'genepy',
    version                             = '0.0.1',
    description                         = 'Python tool for generating gitlab-ci documentation.',
    long_description                    = long_description,
    long_description_content_type       = "text/markdown",
    url                                 = 'https://github.com/MainSystemDev/kitica',
    author                              = 'Joshua Kim Rivera',
    author_email                        = 'joshuakimrivera@gmail.com',
    license                             = license,
    platforms                           = 'any',
    classifiers                         = CLASSIFIERS,
    install_requires                    = REQUIREMENTS,
    package_dir                         = {'': 'src'},
    packages                            = find_packages('src'),
    scripts                             =['bin/genepy']
)


setup(

)