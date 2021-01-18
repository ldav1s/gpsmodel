import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpsmodel",
    version="0.0.1",
    author="Leo Davis",
    author_email="3577372+ldav1s@users.noreply.github.com",
    description="Simple program that sets the program model for u-blox 8 / u-blox M8 receivers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ldav1s/gpsmodel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/gpsmodel"],
    python_requires=">=3.5",
)
