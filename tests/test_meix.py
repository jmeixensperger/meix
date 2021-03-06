#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `meix` package."""

import pytest

from click.testing import CliRunner

from meix import meix
from meix import cli

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Hello pretend person!' in result.output
    result = runner.invoke(cli.main, ['Jack'])
    assert result.exit_code == 0
    assert 'Hello Jack!' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_message(capsys):
    """We use capsys to capture printing to stdout"""
    """The message function only prints to stdout,
       it does not return anything"""
    assert meix.message("") == None
    out, err = capsys.readouterr()
    assert "Hello pretend person!" in out
