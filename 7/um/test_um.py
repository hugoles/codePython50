import um
import pytest

def test():
    assert um.count('umbicious dog um') == 1
    assert um.count('i donow, um, i mean um...') == 2
    assert um.count('a um was expected') == 1
    assert um.count('IM ANGRY AND UM, OMG UM') == 2

