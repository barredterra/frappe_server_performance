from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in server_performance/__init__.py
from server_performance import __version__ as version

setup(
	name="server_performance",
	version=version,
	description="Monitor the performance of the server running your frappe site",
	author="Raffael Meyer",
	author_email="-",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
