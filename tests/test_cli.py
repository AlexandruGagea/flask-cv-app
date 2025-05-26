from click.testing import CliRunner
from app.cli import print_cv

def test_cli_output_personal():
    runner = CliRunner()
    result = runner.invoke(print_cv)
    assert result.exit_code == 0
    assert "Personal" in result.output

def test_cli_output_experience():
    runner = CliRunner()
    result = runner.invoke(print_cv)
    assert result.exit_code == 0
    assert "Experience" in result.output

def test_cli_output_education():
    runner = CliRunner()
    result = runner.invoke(print_cv)
    assert result.exit_code == 0
    assert "Education" in result.output