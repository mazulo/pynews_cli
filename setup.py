import sys
from setuptools import setup, find_packages


def read(fname):
    """ Return file content. """
    with open(fname) as f:
        content = f.read()

    return content


description = 'PyNews is a simple Python CLI to browse news from HN website'
try:
    long_description = read('README.rst')
except IOError:
    long_description = description


author_name = 'Patrick Mazulo'
author_email = 'pmazulo@gmail.com'
dependencies = [
    'curses-menu==0.5.0',
    'requests==2.20.0',
    'tqdm==3.8.0',
]

if sys.version_info.major == 2:
    dependencies.append('futures==3.0.5')

setup(
    name='PyNews',
    version='0.1.3',
    description=description,
    long_description=long_description,
    url='https://github.com/mazulo/pynews_cli',
    author=author_name,
    author_email=author_email,
    maintainer=author_name,
    maintainer_email=author_email,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Shells',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='pynews cli shell news hackernews',
    download_url='https://github.com/mazulo/pynews_cli/archive/master.zip',
    packages=find_packages(exclude=['tests*']),
    install_requires=dependencies,
    entry_points={'console_scripts': ['pynews = pynews.pynews:main']},
    platforms='windows linux',
)
