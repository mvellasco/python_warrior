import subprocess

import pytest


@pytest.mark.parametrize("level", list(range(1, 10)))
def test_passes_levels(level):
    result = subprocess.Popen(
        args=f"pythonwarrior -l {level}",
        shell=True,
        stdout=subprocess.PIPE,
    )
    result.wait(timeout=20)
    output, _ = result.communicate()
    expected_message = (
        "You have found the stairs."
        if level != 9 else
        "You have climbed to the top of the tower and rescued the fair maiden Python"
    )

    assert expected_message in output.decode()
