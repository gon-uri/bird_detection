import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bird_detection",
    version="0.0.1",
    author="Gonzalo Uribarri",
    description="Machine learning algorithm to identify the presence and location of birds.",
    long_description_content_type="text/markdown",
    url="https://github.com/gon-uri/bird_detection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.7',
)
