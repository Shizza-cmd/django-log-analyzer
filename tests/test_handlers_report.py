import pytest
from reports.handlers_report import HandlersReport


def test_report_aggregation():
    report = HandlersReport()

    input1 = {"/a": {"INFO": 3, "DEBUG": 1}}
    input2 = {"/a": {"INFO": 2}, "/b": {"ERROR": 5}}

    report.update(input1)
    report.update(input2)

    assert report.data["/a"]["INFO"] == 5
    assert report.data["/a"]["DEBUG"] == 1
    assert report.data["/b"]["ERROR"] == 5
    assert report.total == 5 + 1 + 5
