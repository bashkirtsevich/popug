from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="popug",
    version="0.0.1",
    description="Parrot arg parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python"],
    keywords="CLI argv",
    author="D.Bashkirtsevich",
    author_email="bashkirtsevich@gmail.com",
    url="https://github.com/bashkirtsevich/popug",
    license="GPL3 License",
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'popug = popug.__main__:main',
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.0",
)

