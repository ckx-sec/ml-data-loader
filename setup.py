from setuptools import setup, find_packages, Extension

setup(
    name="fast-dataloader",
    version="0.2.3",
    description="Fast data loading utilities for ML pipelines",
    long_description="A lightweight data loading library with optional C-accelerated CSV parsing for ML workloads.",
    packages=find_packages(),
    ext_modules=[
        Extension(
            "dataloader._accel",
            sources=["_accel.c"],
            optional=True,
        ),
    ],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
    ],
)
