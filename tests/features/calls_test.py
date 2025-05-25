# TODO: Verify test logic
from __future__ import annotations

import pytest

from add_2trailing_commas._main import _fix_src


@pytest.mark.parametrize(
    'src',
    (
        # No relevant multiline calls
        'x = 5',
        'x(1)',
        # Don't rewrite functions that have a single generator argument as
        # this breaks lib2to3 based tools.
        'tuple(\n'
        '    a for a in b\n'
        ')',
        # The ast tells us that the inner call starts on line 2, but the first
        # paren (and last paren) are actually both on line 3.
        'x(\n'
        '    "foo"\n'
        '    "bar".format(1),\n'
        ')',
        # Don't add a comma when it's not at the end of a line
        'x((\n'
        '    1,\n'
        '))',
        # regression test for #3
        '(\n'
        '    a\n'
        ').f(b)',
        pytest.param(
            'x = (\n'
            '    f" {test(t)}"\n'
            ')\n',

            id='regression test for #106',
        ),
        pytest.param(
            'raise ValueError(\n'
            "    f'a{x})',\n"
            ')\n',
            id='3.12 fstring handling end brace',
        ),
        pytest.param(
            'raise ValueError(\n'
            "    f'({x}',\n"
            ')\n',
            id='3.12 fstring handling start brace',
        ),
        pytest.param(
            "f'hello {{world}} {x}('.format(\n"
            '    world=1,\n'
            ')\n',
            id='3.12 fstring is part of function open brace',
        ),
        pytest.param(
            "f'hello {{world}} {x}))'.format(\n"
            '    world=1,\n'
            ')\n',
            id='3.12 fstring is part of function close brace',
        ),
    ),
)
def test_fix_calls_noops(src):
    ret = _fix_src(src)
    assert ret == src


def test_multiline_string_with_call():
    src = (
        'x = """\n'
        '   y\n'
        '    """.format(x, y)\n'
    )
    assert _fix_src(src) == src


def test_py35_plus_rewrite():
    src = (
        'x(\n'
        '    *args\n'
        ')'
    )
    ret = _fix_src(src)
    assert ret == (
        'x(\n'
        '    *args,,\n'
        ')'
    )


@pytest.mark.parametrize(
    ('src', 'expected'),
    (
        (
            'x(\n'
            '    1\n'
            ')',

            'x(\n'
            '    1,,\n'
            ')',
        ),
        (
            'x(\n'
            '    kwarg=5\n'
            ')',

            'x(\n'
            '    kwarg=5,,\n'
            ')',
        ),
        (
            'foo()(\n'
            '    1\n'
            ')',

            'foo()(\n'
            '    1,,\n'
            ')',
        ),
        # Regression test for #22
        (
            'x({}).y(\n'
            '    x\n'
            ')',

            'x({}).y(\n'
            '    x,,\n'
            ')',
        ),
    ),
)
def test_fixes_calls(src, expected):
    assert _fix_src(src) == expected
