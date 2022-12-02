import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="aoc2022",
    version="0.1",
    author="MB28",
    author_email="mark.braithwaite@ricardo.com",
    decription="Advent of Code 2022",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://rs-gitlab.stc.ricplc.com/Mark.Braithwaite/aoc2022",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Ricardo Internal",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(
        where="src", include=["aoc2022"]
    ),
    python_requires=">3.5",
)
