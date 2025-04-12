from parser import parse_log_file
import tempfile
import os


def test_parse_log_file():
    content = """\
INFO 2023-04-10 12:00:00,000 django.request path=/api/items
ERROR 2023-04-10 12:01:00,000 django.request path=/api/items
DEBUG 2023-04-10 12:02:00,000 django.request path=/api/status
"""
    with tempfile.NamedTemporaryFile("w+", delete=False) as f:
        f.write(content)
        temp_path = f.name

    result = parse_log_file(temp_path)

    assert result["/api/items"]["INFO"] == 1
    assert result["/api/items"]["ERROR"] == 1
    assert result["/api/status"]["DEBUG"] == 1

    os.unlink(temp_path)
