from setuptools import setup, find_packages

setup(
    name = "alxpackage",
    version = "0.1",
    packages = find_packages(exclude = ['tests*']),
    licence = "MIT",
    description = "EDSA example python package",
    long_description =open('README.md').read(),
    install_requires =['numpy'],
    url ='https://github.com/harriet-ngomo/alxpackage',
    author ='harriet',
    author_email='harriet@gmail.com'
)