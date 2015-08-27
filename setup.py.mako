from setuptools import setup

setup(
	name="appen_utilities",
	packages=["appen_utilities"],
	description="These are some test utils",
	
	version="${version}",
	
	url="http://www.appen.com",
	author="Appen",
	author_email="it@appen.com",
	
	install_requires = [
		"simplejson",
	]
)
