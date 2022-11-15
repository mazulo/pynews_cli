from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()
description = "PyNews is a simple Python CLI to browse news from HN website"
author_name = "Patrick Mazulo"
author_email = "pmazulo@gmail.com"
dependencies = [
    "curses-menu==0.6.7",
    "requests==2.28.1",
    "alive-progress==2.4.1",
]
__version__ = "0.2.2"

setup(
    name="PyNews",
    version=__version__,
    description=description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/mazulo/pynews_cli",
    author=author_name,
    author_email=author_email,
    maintainer=author_name,
    maintainer_email=author_email,
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
        "Topic :: System :: Shells",
    ],
    keywords="pynews cli shell news hackernews",
    download_url="https://github.com/mazulo/pynews_cli/archive/master.zip",
    packages=find_packages(exclude=["tests*"]),
    install_requires=dependencies,
    entry_points={"console_scripts": ["pynews = pynews.pynews:main"]},
    platforms="windows linux",
)
