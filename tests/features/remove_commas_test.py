from __future__ import annotations

import pytest

from add_2trailing_commas._main import _fix_src


@pytest.mark.parametrize(
    ('src', 'expected'),
    (
        # can't rewrite 1-element tuple
        ('(1,)', '(1,)'),
        # but I do want the whitespace fixed!
        ('(1, )', '(1,)'),
        ('(1, 2,)', '(1, 2)'),
        ('[1, 2,]', '[1, 2]'),
        ('[1, 2,   ]', '[1, 2]'),
        ('{1, 2, }', '{1, 2}'),
        ('{1: 2, }', '{1: 2}'),
        ('f(1, 2,)', 'f(1, 2)'),
    ),
)
def test_remove_extra_comma(src, expected):
    assert _fix_src(src) == expected
