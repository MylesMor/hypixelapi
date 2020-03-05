import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypixelapi",
    version="0.1.0",
    author="MylesMor",
    author_email="hello@mylesmor.dev",
    description="A Python 3 wrapper for the HypixelAPI OpenAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MylesMor/hypixelapi",
    packages=setuptools.find_packages(exclude=("tests","examples",)),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
