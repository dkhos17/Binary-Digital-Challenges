import pytest
import logging
from pokerdevs import event_tuple


logger = logging.getLogger(__name__)


def generate_test_events():
    yield ("0", 9999999999, "UserLongPressed", 344, 424)
    yield ("1", 1000000000, "UserClickedOnButton", "close_button")
    yield ("2", 9999999999, "UserLongPressed", 344, 424)
    yield ("3", 1000000000, "UserClickedOnButton", "close_button")
    yield ("4", 9999999999, "UserLongPressed", 344, 424)
    yield ("5", 1000000000, "UserClickedOnButton", "close_button")
    yield ("6", 9999999999, "UserLongPressed", 344, 424)
    yield ("7", 1000000000, "UserClickedOnButton", "close_button")
    yield ("8", 9999999999, "UserLongPressed", 344, 424)
    yield ("9", 1000000000, "UserClickedOnButton", "close_button")
    yield ("10", 9999999999, "UserLongPressed", 344, 424)


def serialize_event(event):
    return f"Event '{event[2]}' occurred at {event[1]} with ID: {event[0]}"



def test_event_tuple():
    logger.info(f"Starting the test !")
    for i, event in enumerate(generate_test_events()):
        assert event[0] == str(i)
        if i % 2 == 0:
            assert len(event) == 5
            assert event[1] == 9999999999
        else:
            assert len(event) == 4
            assert event[1] == 1000000000
        
        if event[2] == 'UserLongPressed':
            assert event[3] and event[4]
            assert serialize_event(event) == f"Event 'UserLongPressed' occurred at 9999999999 with ID: {i}"
        else:
            assert event[3]
            assert serialize_event(event) == f"Event 'UserClickedOnButton' occurred at 1000000000 with ID: {i}"
        

    # pytest.fail(f"YOU NEED TO FINISH THIS")