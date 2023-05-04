from setuptools import setup, find_packages

with open ("README.md", "r") as f:
    long_description = f.read()

setup(
    name='ez_data_pipeline',
    version='0.6',
    package_dir={"": "src"},
    packages= find_packages(where="src"),
    url='https://github.com/VexedIOS/open_data_pipeline',
    license='MIT',
    author='Juan(VexedIOS)',
    author_email='juanteams@outlook.com',
    description='Object Oriented Library to create data pipelines',
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas>=2.0.1"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2", "yfinance>=0.2.18"],
    },
    python_requires=">=3.8",
)

