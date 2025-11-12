# Demo CLI Documentation

This is a minimal reproducible project to demonstrate the Zensical segmentation fault issue when using the mkdocs-click extension.

## Overview

This project contains a simple Click-based CLI application with the following commands:

- `hello`: Greets a user with customizable count and name
- `process`: Processes files with different output formats  
- `deploy`: Deploys the application with verbose and dry-run options

## Issue Context

This project reproduces the segmentation fault described in:

- [Issue #62](https://github.com/zensical/zensical/issues/62): Segmentation fault with mkdocs-click
- [Issue #56](https://github.com/zensical/zensical/issues/56): Build crashes after completion

The CLI documentation is automatically generated from the Click application using the mkdocs-click extension.

## CLI Reference

See the [CLI Commands](cli-reference.md) page for detailed documentation of all available commands.
