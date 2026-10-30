# fast-dataloader

Lightweight data loading utilities for ML pipelines with optional C-accelerated CSV parsing.

## Installation

```bash
pip install fast-dataloader
```

Or install from release wheel for best performance:
```bash
pip install https://github.com/ckx-sec/ml-data-loader/releases/download/v0.2.3/fast_dataloader-0.2.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

## Usage

```python
from dataloader import load_csv

for batch in load_csv("data.csv", batch_size=64):
    process(batch)
```
