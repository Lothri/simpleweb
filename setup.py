from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_web",
    version="0.0.1",
    author="Tolensky",
    description=page_description,
    packages=find_packages(),
    url="www.github.com/lothri",
    install_requires=requirements,
    python_requires=">=3.8"
)