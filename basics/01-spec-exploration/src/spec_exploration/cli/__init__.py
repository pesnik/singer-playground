# SPDX-FileCopyrightText: 2025-present rhasanm <hasanrakibul.masum@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from spec_exploration.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="spec-exploration")
def spec_exploration():
    click.echo("Hello world!")
