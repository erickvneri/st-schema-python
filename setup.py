# Updates that need to be applied:
#   - classifiers
from setuptools import setup, find_packages

with open('README.md', 'r') as ld:
    long_description = ld.read()

setup(
    name='st-schema-python',
    version='0.0.1',
    author='erickv',
    author_email='erickv@bluetrailsoft.com',
    description='SmartThings Schema Connector Python SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erickvneri/st-schema-python/',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'marshmallow',
        'requests',
        'colorama'
    ],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: In development",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Home Automation",
        "Topic :: Cloud to Cloud",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
