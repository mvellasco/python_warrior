import subprocess


def test_passes_level_1():
    result = subprocess.Popen("pythonwarrior -l 1", shell=True, stdout=subprocess.PIPE)
    result.wait(timeout=20)
    output, _ = result.communicate()

    assert "You have found the stairs." in output.decode()