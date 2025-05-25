from __future__ import annotations

import ast
from collections.abc import Iterable

from tokenize_rt import Offset
from tokenize_rt import Token

from add_2trailing_commas._ast_helpers import ast_to_offset
from add_2trailing_commas._data import register
from add_2trailing_commas._data import State
from add_2trailing_commas._data import TokenFunc
from add_2trailing_commas._token_helpers import find_simple
from add_2trailing_commas._token_helpers import fix_brace


def _fix_with(i: int, tokens: list[Token]) -> None:
    i += 1
    if tokens[i].name == 'UNIMPORTANT_WS':
        i += 1
    if tokens[i].src == '(':
        fix = find_simple(i, tokens)
        # only fix if outer parens are for the with items (next is ':')
        if fix is not None and tokens[fix.braces[-1] + 1].src == ':':
            fix_brace(tokens, fix, add_comma=True, remove_comma=True)


@register(ast.With)
def visit_With(
    state: State,
    node: ast.With,
) -> Iterable[tuple[Offset, TokenFunc]]:
    yield ast_to_offset(node), _fix_with
