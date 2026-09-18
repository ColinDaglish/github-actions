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