import setuptools
import os


basedir = os.path.abspath(os.path.dirname(__file__))

with open(basedir + '/README.md', 'r') as ld:
    long_description = ld.read()


setuptools.setup(
    name='st-schema-python',
    version='1.0.1',
    author='erickvneri',
    author_email='erickv@bluetrailsoft.com',
    description='SmartThings Schema Connector Python SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erickvneri/st-schema-python/',
    packages=setuptools.find_packages(),
    install_requires=[
        'pytest',
        'marshmallow',
        'requests',
        'colorama'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Home Automation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
