# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `rsconstruct.toml:1` - the four `demo_*.py` scripts are not checked by any processor (no ruff/pylint, no `pyproject.toml`), and their third-party dependency `lxml` is declared nowhere; add a `pyproject.toml` declaring `lxml` (plus a dev group with the linters) and the matching `[processor.ruff]`/`[processor.pylint]` sections.
- `demo_misc.py:4` - the docstring calls `lxml.etree` "the built in" module, but `lxml` is a third-party package (the built-in one is `xml.etree`, which the next paragraph contrasts it with); fix the wording.

## Low

- `demo_namespace.py:26` - dead code kept in a bare string literal with "this does not work currently"; `lxml.etree.register_namespace` only affects serialization, not XPath prefixes, so it can never work - replace it with a working alternative (e.g. `lxml.etree.XPathEvaluator(root, namespaces=...)` or `lxml.etree.XPath('//x:bar', namespaces=...)`) or delete it.
- `demo_full_path.py:11` - comment "for bar at any level" is copy-pasted from `demo_misc.py` and wrong here (the expression is the absolute path `/html/head/title`); fix the comment.
- `unsorted/expr.xpath:1` - contains only `//`, which is an invalid XPath expression (`lxml` raises `XPathEvalError: Invalid expression`) and is referenced by nothing; complete it into a real example for `unsorted/file.xml` or delete it.
- `unsorted/doc/links.txt:2` - both links use `http://`, and the MSDN one now redirects to a `previous-versions` archive page on learn.microsoft.com; update to the current `https://` URLs.
