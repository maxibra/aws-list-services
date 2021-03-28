from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-list-services',
    version='0.0.1',
    description='Create list of all used services',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Max Braver',
    author_email='max.braver@gmail.com',
    packages=['awsls'],
    scripts=['aws-ls'],
    entry_points={
        'console_scripts': [
            'aws-ls=awsls:main',
        ],
    },
    url='https://github.com/maxibra/aws-list-services.git',
    install_requires=['boto3']
)
