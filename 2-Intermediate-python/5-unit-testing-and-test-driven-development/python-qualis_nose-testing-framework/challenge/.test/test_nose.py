import re
import os
import sys

sys.path.append(os.getcwd())

from mytest import test_circle
import autopep8
from xml.etree import ElementTree
import pytest

@pytest.fixture
def get_xml_root_element(source):
    xml = ElementTree.parse(source)
    root = xml.getroot()
    return root


@pytest.mark.parametrize("source, expected",
                         [("nosetests.xml", 10)], ids=['test_testcase_result'])
def test_nose_testcase_result(get_xml_root_element, expected):
    test_case_success = int(get_xml_root_element.attrib["tests"]) - int(get_xml_root_element.attrib["failures"]) - int(
        get_xml_root_element.attrib["errors"]) - int(get_xml_root_element.attrib["skip"])
    assert int(get_xml_root_element.attrib["tests"]) == expected and test_case_success == expected

@pytest.mark.parametrize("source", [("coverage.xml")], ids=['test_coverage_result'])
def test_nose_coverage_result(get_xml_root_element):
    line_coverage_status = (int(get_xml_root_element.attrib["lines-valid"]) == int(get_xml_root_element.attrib["lines-covered"])) and (int(float(get_xml_root_element.attrib["line-rate"])) == 1)
    branch_coverage_status = (int(get_xml_root_element.attrib["branches-valid"]) == int(get_xml_root_element.attrib["branches-covered"])) and (int(float(get_xml_root_element.attrib["branch-rate"])) == 1)
    assert line_coverage_status and branch_coverage_status
