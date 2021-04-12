import pytest

from aestoolbox.core.aes_schedule import KeySchedule
from .test_vectors import test_vectors_128


@pytest.mark.parametrize("test_vector", test_vectors_128)
def test_aes_128_schedule(test_vector):
    xk_test = test_vector["round_keys"]
    ks = KeySchedule(test_vector["key"])
    ks.expand_key()
    xk = list(int(x, 16) for x in ks.hkeys["xk"].values())
    assert len(xk) == 11
    assert len(xk) == len(xk_test)
    for (xkg, xke) in zip(xk, xk_test):
        assert xkg == xke
