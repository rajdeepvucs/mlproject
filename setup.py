from setuptools import setup, find_packages

def get_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mlproject",  # Replace with your own project name
    version="0.0.1",
    author="Rajdeep Das",
    author_email="rajdeeppapai@gmail.com",
    description="A small description of your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajdeepvucs/mlproject",  # Replace with your project URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=get_requirements('requirements.txt')
)
