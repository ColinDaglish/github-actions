import json

from precommit_updates import cli


def test_write_output_preserves_workflow_keys_and_json(tmp_path, monkeypatch):
    output = tmp_path / "github-output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))

    cli._write_output({"updates_found": "true", "updates_json": [{"repo": "example"}]})

    assert output.read_text().splitlines() == [
        "updates_found=true",
        'updates_json=[{"repo":"example"}]',
    ]


def test_cooldown_command_reads_workflow_environment(tmp_path, monkeypatch):
    tracking = tmp_path / "tracking.json"
    tracking.write_text(json.dumps({"hooks": {}}))
    output = tmp_path / "github-output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setenv("UPDATES_JSON", json.dumps([{"repo": "example", "semver_level": "patch"}]))

    cli.cooldown_command(type("Args", (), {"tracking": str(tracking)})())

    values = dict(line.split("=", 1) for line in output.read_text().splitlines())
    assert json.loads(values["eligible_updates"])[0]["repo"] == "example"
    assert json.loads(values["skipped_updates"]) == []


def test_validate_command_accepts_aligned_files(tmp_path, capsys):
    config = tmp_path / "pre-commit-config.yaml"
    tracking = tmp_path / "tracking.json"
    repo = "https://github.com/example/hooks"
    sha = "a" * 40
    config.write_text(f"repos:\n  - repo: {repo}\n    rev: {sha}\n")
    tracking.write_text(json.dumps({"hooks": {repo: {"current_sha": sha}}}))

    cli.validate_command(type("Args", (), {"config": str(config), "tracking": str(tracking)})())

    assert "aligned" in capsys.readouterr().out


def test_validate_command_rejects_sha_mismatch(tmp_path, capsys):
    config = tmp_path / "pre-commit-config.yaml"
    tracking = tmp_path / "tracking.json"
    repo = "https://github.com/example/hooks"
    config.write_text(f"repos:\n  - repo: {repo}\n    rev: {'a' * 40}\n")
    tracking.write_text(json.dumps({"hooks": {repo: {"current_sha": "b" * 40}}}))

    try:
        cli.validate_command(type("Args", (), {"config": str(config), "tracking": str(tracking)})())
    except SystemExit as error:
        assert error.code == 1
    else:
        raise AssertionError("expected validation to fail")

    assert "SHA mismatch" in capsys.readouterr().out


def test_validate_command_initializes_missing_tracking_file(tmp_path, capsys):
    config = tmp_path / "pre-commit-config.yaml"
    tracking = tmp_path / "tracking.json"
    repo = "https://github.com/example/hooks"
    sha = "a" * 40
    config.write_text(f"repos:\n  - repo: {repo}\n    rev: {sha}\n")

    cli.validate_command(type("Args", (), {"config": str(config), "tracking": str(tracking)})())

    state = json.loads(tracking.read_text())
    assert state["hooks"][repo]["current_sha"] == sha
    assert "not found; creating baseline" in capsys.readouterr().out