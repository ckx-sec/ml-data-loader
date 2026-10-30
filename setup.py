from setuptools import setup, find_packages
setup(
    name="fast-dataloader",
    version="0.2.1",
    description="Fast data loading utilities for ML pipelines",
    packages=find_packages(),
    package_data={"dataloader": ["bin/*"]},
    include_package_data=True,
    python_requires=">=3.8",
)
