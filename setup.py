from setuptools import setup, find_packages

setup(
    name="step",
    version="0.1.0",
    url="",
    license="Apache License 2.0",
    author="Sanaur Asif",
    author_email="sanaurasif2@gmail.com",
    description="A python module to run tests as steps",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        "console_scripts": [
            "rocx = step.run:run_cli"
        ]
    }
)
