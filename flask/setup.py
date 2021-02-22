from setuptools import setup

setup(
    name="flask_app",
    version="1.0",
    packages=["flask_app"],
    package_dir={"": "src"},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)