# Zensical Bug Reproduction

Minimal reproducible project for demonstrating a segmentation fault when using Zensical with mkdocs-click extension and PyTorch.

## Issue

When building documentation with `zensical build --clean`, a segmentation fault occurs if the CLI application imports PyTorch and calls `torch.set_default_device("cpu")`.

**Note:** The error does NOT occur when running `mkdocs build --clean` directly - the issue is specific to running through Zensical.

## Reproduction Steps

1. Install dependencies using uv:
   ```bash
   uv sync
   ```

2. Run Zensical build:
   ```bash
   zensical build --clean
   ```

3. Observe the segmentation fault error.

## Workaround

Comment out line 12 in `demo_cli.py` to avoid the segmentation fault:
```python
# torch.set_default_device("cpu")
```

## Environment

- Python: 3.12
- Zensical: 0.0.6
- mkdocs-click: 0.9.0
- PyTorch: >=2.9.0
