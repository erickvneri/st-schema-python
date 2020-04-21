from setuptools import setup, find_packages

setup(
    name='pystschema',
    version='0.0.1',
    author='erickv',
    author_email='erickv@bluetrailsoft.com',
    description='Python ST-Schema SDK',
    url='https://github.com/erickvneri/py-st-schema/',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'marshmallow'
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
