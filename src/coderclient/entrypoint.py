import click
import coderclient.settings
import coderclient.client
import coderclient.models
import yaml
import logging

settings = coderclient.settings.CoderClientSettings() # type: ignore

@click.group()
@click.option("-c","--codebook", type = click.File("r"), default = "codebook.yaml")
@click.option("--debug/--no-debug", type = bool, default = False)
@click.pass_context
def cli(ctx: click.Context, codebook, debug):
    logging.basicConfig(level = logging.DEBUG if debug else logging.WARNING)
    codebook = coderclient.models.Codebook.model_validate(yaml.safe_load(codebook))
    ctx.obj = coderclient.client.CoderClient(url = settings.llama_url, codebook = codebook)

@cli.command()
@click.argument("document", type = click.File("r"), default = "-")
@click.pass_obj
def code(client: coderclient.client.CoderClient, document):
    click.echo(client.code(document.read()))

if __name__ == "__main__":
    cli()
