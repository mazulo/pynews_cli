from setuptools import setup, find_packages


long_description = """
A Python CLI to browse news from Hacker News (and others, in the near future).
Also is a Python implementation of the awesome hn-cli.
"""
author_name = 'Patrick Mazulo'
author_email = 'pmazulo@gmail.com'
dependencies = [
    'curses-menu==0.5.0',
    'requests==2.9.1',
    'tqdm==3.8.0',
]

setup(
    name='PyNews',
    version='0.1.3',
    description='PyNews is a simple Python CLI to browse news from HN website',
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
    scripts=['bin/pynews'],
    platforms='windows linux',
)
