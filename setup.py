import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timelogger",
    version="0.0.2",
    author="Brandon M. Pace",
    author_email="brandonmpace@gmail.com",
    description="A time logger for Python programs",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    keywords="debug time logging logger log stopwatch timer",
    license="GNU Lesser General Public License v3 or later",
    platforms=['any'],
    python_requires=">=3.6.5",
    url="https://github.com/brandonmpace/timelogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ]
)
