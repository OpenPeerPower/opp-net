from setuptools import setup

VERSION = "0.1.0"

setup(
    name="opp-net",
    version=VERSION,
    license="GPL v3",
    author="Open Peer Power",
    author_email="opensource@openpeerpower.com",
    url="https://www.openpeerpower.com/",
    download_url="https://github.com/OpenPeerPower/opp-net/tarball/{}".format(VERSION),
    description=("Open Peer Power cloud integration"),
    long_description=(""),
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=["openpeerpower", "cloud"],
    zip_safe=False,
    platforms="any",
    packages=["opp_net"],
    install_requires=[
        "pycognito==0.1.5",
        "snitun==0.20",
        "acme==1.12.0",
        "cryptography>=2.8,<40.0",
        "attrs>=19.3",
        "pytz>=2019.3",
        "aiohttp>=3.6.1",
        "atomicwrites==1.4.0",
    ],
)
