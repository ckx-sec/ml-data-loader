"""Fast data loading utilities for ML pipelines."""

def load_csv(path, batch_size=32):
    """Load CSV file in batches."""
    import csv
    with open(path) as f:
        reader = csv.reader(f)
        batch = []
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

__version__ = "0.2.3"
