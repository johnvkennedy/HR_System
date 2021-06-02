# This is for the functions SEPARATED from
# the primary project. Don't work otherwise
from HR_System_Testing.py import capture_ssn

def test_1():
    assert Processor.capture_ssn("22-222-2222") is True