"""
Demo CLI application to reproduce Zensical mkdocs-click segfault bug.

This module provides a simple Click-based CLI application with documented
functions that can be used to test the mkdocs-click extension.
"""

import rich_click as click
import torch

# Comment below to avoid segmentation fault error
torch.set_default_device("cpu")


@click.group()
def cli():
    """Demo CLI application for testing Zensical with mkdocs-click.

    This is a minimal CLI application created to reproduce the segmentation
    fault issue when using mkdocs-click extension with Zensical.
    """
    pass


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times.

    This command demonstrates a basic Click command with options
    that can be documented using mkdocs-click.

    Args:
        count: Number of times to repeat the greeting
        name: Name of the person to greet
    """
    for _ in range(count):
        click.echo(f"Hello, {name}!")


@cli.command()
@click.argument("filename")
@click.option(
    "--format",
    type=click.Choice(["json", "yaml", "text"]),
    default="text",
    help="Output format.",
)
def process(filename, format):
    """Process a file and output in specified format.

    This command simulates file processing functionality with
    multiple output format options.

    Args:
        filename: Path to the file to process
        format: Output format (json, yaml, or text)
    """
    click.echo(f"Processing {filename} in {format} format...")

    if format == "json":
        click.echo('{"status": "processed", "file": "' + filename + '"}')
    elif format == "yaml":
        click.echo(f"status: processed\nfile: {filename}")
    else:
        click.echo(f"File {filename} has been processed successfully.")


@cli.command()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output.")
@click.option(
    "--dry-run", is_flag=True, help="Show what would be done without executing."
)
def deploy(verbose, dry_run):
    """Deploy the application with optional verbose and dry-run modes.

    This command demonstrates boolean flags and conditional logic
    in CLI applications.

    Args:
        verbose: Enable detailed output during deployment
        dry_run: Show planned actions without executing them
    """
    if dry_run:
        click.echo("DRY RUN MODE: Would perform deployment...")
        if verbose:
            click.echo("DRY RUN: Would copy files to server")
            click.echo("DRY RUN: Would restart services")
            click.echo("DRY RUN: Would verify deployment")
    else:
        click.echo("Starting deployment...")
        if verbose:
            click.echo("Copying files to server...")
            click.echo("Restarting services...")
            click.echo("Verifying deployment...")
        click.echo("Deployment completed successfully!")


if __name__ == "__main__":
    cli()
