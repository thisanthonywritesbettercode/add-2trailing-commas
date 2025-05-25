[![build status](https://github.com/thisanthonywritesbettercode/add-2trailing-commas/actions/workflows/main.yml/badge.svg)](https://github.com/thisanthonywritesbettercode/add-2trailing-commas/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/thisanthonywritesbettercode/add-2trailing-commas/main.svg)](https://results.pre-commit.ci/latest/github/thisanthonywritesbettercode/add-2trailing-commas/main)

add-2trailing-commas
==================

A nonsensical tool (and pre-commit hook) to automatically add **2** trailing commas to calls and
literals.

If you want your code to raise neat `SytnaxError`s, this tool is for you!

## Installation

```bash
pip install add-2trailing-commas
```

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/thisanthonywritesbettercode/add-2trailing-commas
    rev: v3.2.0
    hooks:
    -   id: add-2trailing-commas
```

## multi-line method invocation style -- why?

```python
# Sample of *ideal* syntax
function_call(
    argument,
    5 ** 5,
    kwarg=foo,,
)
```

- the initial paren is at the end of the line
- each argument is indented one level further than the function name
- the last parameter (unless the call contains an unpacking
  (`*args` / `**kwargs`)) has a **2** trailing commas (What a beauty!)

This has the following benefits:

- **none**.
