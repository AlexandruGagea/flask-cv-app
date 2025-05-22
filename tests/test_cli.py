from click.testing import CliRunner
from app.cli import print_cv

def test_cli_output():
    runner = CliRunner()
    result = runner.invoke(print_cv)
    assert result.exit_code == 0
    assert "Personal" in result.output
