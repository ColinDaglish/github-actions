from precommit_updates.models import is_sha_like_version


def test_sha_detection_does_not_depend_on_repository_names():
    assert is_sha_like_version("0123456789abcdef" * 2 + "01234567")