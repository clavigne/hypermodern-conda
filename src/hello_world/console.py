"""CLI interface for hello world."""
import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Print hello world."""
    click.echo("Hello, world!")
