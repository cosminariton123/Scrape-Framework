def assert_equals(expected, result):
    assert expected == result, f"Expected result is {expected}, actual result is {result}"


def assert_array_equals(expected, result):
    assert len(result) == len(expected), f"Expected size {len(expected)}, actual size {len(result)}"

    for idx, (ex, res) in enumerate(zip(expected, result)):
        assert ex == res, f"Elements on position {idx} are not the same"


def assert_not_none(result):
    assert result is not None, f"Expected is not {repr(None)}, actual result is {repr(result)}"


def assert_none(result):
    assert result is None, f"Expected result is {repr(None)}, actual result is {repr(result)}"


def assert_not_same(expected, result):
    assert result is not expected, f"Expected result is {repr(expected)}, actual result is {repr(result)}"


def assert_same(expected, result):
    assert result is expected, f"Expected result is {repr(expected)}, actual result is {repr(result)}"


def assert_true(result):
    assert result is True, f"Expected result is {repr(True)}, actual result is {repr(result)}"


def assert_false(result):
    assert result is False, f"Expected result is {repr(False)}, actual result is {repr(result)}"
