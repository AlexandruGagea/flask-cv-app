import click
from flask.cli import with_appcontext
from .cv_data import cv_data

@click.command("print-cv")
@with_appcontext
def print_cv():
    """Print CV data to the console."""
    click.echo("== Personal Info ==")
    for k, v in cv_data["personal"].items():
        click.echo(f"{k.title()}: {v}")

    click.echo("\n== Education ==")
    for edu in cv_data["education"]:
        click.echo(f"- {edu['degree']} from {edu['institution']} ({edu['year']})")

    click.echo("\n== Experience ==")
    for job in cv_data["experience"]:
        click.echo(f"- {job['role']} at {job['company']} ({job['duration']})")
        click.echo(f"  {job['description']}")

    click.echo("\n== Skills ==")
    for skill in cv_data["skills"]:
        click.echo(f"- {skill}")

    click.echo("\n== Tools ==")
    for tool in cv_data["tools"]:
        click.echo(f"- {tool}")

    click.echo("\n== Certifications ==")
    for cert in cv_data["certifications"]:
        click.echo(f"- {cert['name']}: {cert['url']}")
