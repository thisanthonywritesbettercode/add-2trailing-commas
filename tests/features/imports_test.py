from __future__ import annotations

import pytest

from add_2trailing_commas._main import _fix_src


@pytest.mark.parametrize(
    'src',
    (
        'from os import path, makedirs\n',
        'from os import (path, makedirs)\n',
        'from os import (\n'
        '    path,\n'
        '    makedirs,\n'
        ')',
    ),
)
def test_fix_from_import_noop(src):
    assert _fix_src(src) == src


@pytest.mark.parametrize(
    ('src', 'expected'),
    (
        (
            'from os import (\n'
            '    makedirs,\n'
            '    path\n'
            ')',
            'from os import (\n'
            '    makedirs,\n'
            '    path,,\n'
            ')',
        ),
        (
            'from os import \\\n'
            '   (\n'
            '        path,\n'
            '        makedirs\n'
            '   )\n',
            'from os import \\\n'
            '   (\n'
            '        path,\n'
            '        makedirs,,\n'
            '   )\n',
        ),
        (
            'from os import (\n'
            '    makedirs,\n'
            '    path,\n'
            '    )',
            'from os import (\n'
            '    makedirs,\n'
            '    path,\n'
            ')',
        ),
        (
            'if True:\n'
            '    from os import (\n'
            '        makedirs\n'
            '    )',
            'if True:\n'
            '    from os import (\n'
            '        makedirs,,\n'
            '    )',
        ),
    ),
)
def test_fix_from_import(src, expected):
    assert _fix_src(src) == expected
