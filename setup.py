from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in one/__init__.py
from one import __version__ as version

setup(
	name="one",
	version=version,
	description="hj",
	author="jj",
	author_email="iu",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
