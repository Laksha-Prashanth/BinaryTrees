import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="binaryTrees-lakshaprashanth@gmail.com", # Replace with your own username
    version="0.0.1",
    author="laksha",
    author_email="lakshaprashanth@gmail.com",
    description="Binary Search Trees implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Laksha-Prashanth/BinaryTrees",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
