import pytest
from longest_common_string import *

@pytest.mark.parametrize('a, b, path', [
    ('asdf', 'sdfg', 'fds'),
    ('1a2s3d4', '0a1s2d3', 'dsa'),
    ])
def test_path(a, b, path):
    match, source = abstract_string(a, b)
    assert path == ''.join(
            [i for i in path_backward(a, match, source, len(a), len(b))]
            )
