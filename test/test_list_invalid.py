# -*- coding: utf-8 -*-
"""
    test_list_invalid
    ~~~~~~~~~~~~~~~~~

    Test invalid ``:list:`` option.
"""

from six import StringIO
import re

from sphinx_testing.util import path, with_app

srcdir = path(__file__).dirname().joinpath('list_invalid').abspath()
warnfile = StringIO()


def teardown_module():
    (srcdir / '_build').rmtree(True)


@with_app(srcdir=srcdir, warning=warnfile)
def test_list_invalid(app, status, warning):
    app.builder.build_all()
    warnings = warnfile.getvalue()
    assert re.search(
        "unknown bibliography list type 'thisisintentionallyinvalid'",
        warnings)
