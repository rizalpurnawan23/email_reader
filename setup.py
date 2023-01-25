from setuptools import setup

from .email_reader.simple_reader import __version__

__version__ = 'dev'

setup(
    name= 'email_reader',
    version= __version__,
    description= 'A simple email reader module for my work.',
    url= 'https://github.com/rizalpurnawan23/email_reader',
    author= 'Rizal Purnawan',
    author_email= 'rizalpurnawan23@gmail.com',
    py_modules= ['email_reader']
)
