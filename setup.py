from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in property_rental/__init__.py
from property_rental import __version__ as version

setup(
	name="property_rental",
	version=version,
	description="property rental management",
	author="alantechnologies",
	author_email="jayakumar@alantechnologies.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
