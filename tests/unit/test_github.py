from types import SimpleNamespace

from precommit_updates.github import GitHubClient, parse_repository_url


def test_parse_repository_url_accepts_git_suffix_and_rejects_other_hosts():
    assert parse_repository_url("https://github.com/example/hook.git").path == "example/hook"
    assert parse_repository_url("https://gitlab.com/example/hook") is None


def test_commit_messages_use_compare_range():
    calls = []

    def runner(command, **kwargs):
        calls.append((command, kwargs))
        return SimpleNamespace(returncode=0, stdout="abc\ndef\n", stderr="")

    commits = GitHubClient(runner=runner).commit_messages(
        "https://github.com/example/hook", "oldsha", "newsha"
    )

    assert commits == ["abc", "def"]
    assert calls[0][0] == [
        "gh",
        "api",
        "repos/example/hook/compare/oldsha...newsha",
        "-q",
        ".commits[].sha",
    ]


def test_failed_github_command_is_treated_as_missing_data():
    def runner(command, **kwargs):
        return SimpleNamespace(returncode=1, stdout="", stderr="failure")

    assert GitHubClient(runner=runner).latest_release("https://github.com/example/hook") is None