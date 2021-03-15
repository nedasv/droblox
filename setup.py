from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="droblox",
    version="0.0.2",
    description="Simple ROBLOX api wrapper easy to use and rich in features.",
    py_modules=["dget"],
    package_dir={"": "src"},

    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License"
    ],

    long_description = long_description,
    long_description_content_type = "text/markdown",

    install_requires=[
        "requests-futures <= 1.0.0"
    ],

    extras_require = {
        "dev": [
            "requests-futures~=1.0.0",
        ],
    },

    url="https://github.com/nedasv/droblox.git",
    author="Nedas Vaupsas",
    author_email="nedasvaupsas@gmail.com"
)