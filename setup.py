"""
Upload your package to PyPi.org so that others can install your package using pip install yourpackage.

First step is to claim your package name & space in pypi using:
$ python setup.py register

Once your package name is registered, nobody can claim or use it. After successful registration,
you have to upload your package there (to the cloud):
$ python setup.py upload

Optionally, you can also sign your package with GPG by,
$ python setup.py --sign upload

"""


from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='netops',
   version='1.0',
   description='A suite of Network Engineering tools',
   license="GNU",
   long_description=long_description,
   author='Dexter Park',
   author_email='ddexterpark@icloud.com',
   url="https://www.linkedin.com/in/dexterpark/",
   packages=['neteng'],
   install_requires=['paramiko', 'netaddr'],
   scripts=[
            'neteng/dmodel',
            'neteng/subnetd',
           ]
)