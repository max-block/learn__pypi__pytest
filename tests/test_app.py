import pytest

import app


def test_will_raise_error():
    with pytest.raises(ValueError):
        app.will_raise_error()
