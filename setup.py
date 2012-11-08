from setuptools import setup, find_packages

setup(
    name = "sheepdog_tables",
    version = "0.5",
    author = "Alex Hart, Adam Thurlow",
    author_email = "alex@sheepdoginc.ca, adam@sheepdoginc.ca",
    description = ("Easy to use tables API for Django"),
    license = "BSD",
    keywords = "tables",
    url = "https://github.com/SheepDogInc/sheepdog_tables",
    packages=find_packages(),
    include_package_data=True,
    long_description="",
    classifiers=
        [
            "Environment :: Web Environment",
            "Framework :: Django",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: CoffeeScript",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)
