from setuptools import setup

setup(
    name="fastapi_app",
    version="1.0",
    packages=["fastapi_app"],
    package_dir={"": "src"},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)