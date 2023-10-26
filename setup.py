#!/usr/bin/env python
# pylint: disable=missing-docstring
import os
from setuptools import setup, find_packages


def get_version():
    """Get version from __init__.py file."""
    filename = os.path.join(os.path.dirname(__file__), "lib", "laflem", "__init__.py")
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])  # pylint: disable=eval-used

    raise ValueError(f"No __version__ defined in {filename}")


setup(
    name="laflem",
    version=get_version(),
    description="Tools collection",
    long_description=open(  # pylint: disable=consider-using-with
        "README.md", encoding="UTF-8"
    ).read(),
    long_description_content_type="text/markdown",
    author="Guillaume MARTINEZ",
    author_email="lunik@tiwabbit.fr",
    maintainer="Guillaume MARTINEZ",
    maintainer_email="lunik@tiwabbit.fr",
    url="https://github.com/Lunik/laflem",
    download_url="https://pypi.org/project/laflem/",
    license_files=("LICENSE",),
    package_dir={"": "lib"},
    packages=find_packages(where="lib"),
    include_package_data=True,
    data_files=[
        (
            "configs/laflem",
            [
                os.path.join(root, file)
                for root, _, files in os.walk("configs")
                for file in files
            ],
        ),
    ],
    entry_points={
        "console_scripts": ["lf = laflem:main", "laflem = laflem:main"],
    },
    python_requires=">=3.8.0",
    install_requires=[
        "rich==13.*",
        "importlib_metadata==6.*",
        "requests==2.*",
    ],
    extras_require={
        "dev": [
            "pylint",
            "black",
            "twine",
            "build",
            "pytest",
            "pytest-cov",
            "pytest-html",
            "pytest-xdist",
            "pytest-helpers-namespace",
            "pytest-order",
            "wheel",
        ],
        "git": [
            "gitpython==3.*",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
