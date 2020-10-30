# -*- coding: utf-8 -*-
"""
    pygments.lexers.bibtex
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for BibTeX bibliography data and styles

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, default, \
    words
from pygments.token import Name, Comment, String, Error, Number, Text, \
    Keyword, Punctuation

__all__ = ['BibTeXLexer', 'BSTLexer']


class BibTeXLexer(ExtendedRegexLexer):
    """
    A lexer for BibTeX bibliography data format.

    .. versionadded:: 2.2
    """

    name = 'BibTeX'
    aliases = ['bib', 'bibtex']
    filenames = ['*.bib']
    mimetypes = ["text/x-bibtex"]
    flags = re.IGNORECASE

    ALLOWED_CHARS = r'@!$&*+\-./:;<>?\[\\\]^`|~'
    IDENTIFIER = '[{0}][{1}]*'.format('a-z_' + ALLOWED_CHARS, r'\w' + ALLOWED_CHARS)

    def open_brace_callback(self, match, ctx):
        opening_brace = match.group()
        ctx.opening_brace = opening_brace
        yield match.start(), Punctuation, opening_brace
        ctx.pos = match.end()

    def close_brace_callback(self, match, ctx):
        closing_brace = match.group()
        if (
            ctx.opening_brace == '{' and closing_brace != '}' or
            ctx.opening_brace == '(' and closing_brace != ')'
        ):
            yield match.start(), Error, closing_brace
        else:
            yield match.start(), Punctuation, closing_brace
        del ctx.opening_brace
        ctx.pos = match.end()

    tokens = {
        'root': [
            include('whitespace'),
            ('@comment', Comment),
            ('@preamble', Name.Class, ('closing-brace', 'value', 'opening-brace')),
            ('@string', Name.Class, ('closing-brace', 'field', 'opening-brace')),
            ('@' + IDENTIFIER, Name.Class,
             ('closing-brace', 'command-body', 'opening-brace')),
            ('.+', Comment),
        ],
        'opening-brace': [
            include('whitespace'),
            (r'[{(]', open_brace_callback, '#pop'),
        ],
        'closing-brace': [
            include('whitespace'),
            (r'[})]', close_brace_callback, '#pop'),
        ],
        'command-body': [
            include('whitespace'),
            (r'[^\s\,\}]+', Name.Label, ('#pop', 'fields')),
        ],
        'fields': [
            include('whitespace'),
            (',', Punctuation, 'field'),
            default('#pop'),
        ],
        'field': [
            include('whitespace'),
            (IDENTIFIER, Name.Attribute, ('value', '=')),
            default('#pop'),
        ],
        '=': [
            include('whitespace'),
            ('=', Punctuation, '#pop'),
        ],
        'value': [
            include('whitespace'),
            (IDENTIFIER, Name.Variable),
            ('"', String, 'quoted-string'),
            (r'\{', String, 'braced-string'),
            (r'[\d]+', Number),
            ('#', Punctuation),
            default('#pop'),
        ],
        'quoted-string': [
            (r'\{', String, 'braced-string'),
            ('"', String, '#pop'),
            ('[^\{\"]+', String),
        ],
        'braced-string': [
            (r'\{', String, '#push'),
            (r'\}', String, '#pop'),
            ('[^\{\}]+', String),
        ],
        'whitespace': [
            (r'\s+', Text),
        ],
    }


class BSTLexer(RegexLexer):
    """
    A lexer for BibTeX bibliography styles.

    .. versionadded:: 2.2
    """

    name = 'BST'
    aliases = ['bst', 'bst-pybtex']
    filenames = ['*.bst']
    flags = re.IGNORECASE | re.MULTILINE

    tokens = {
        'root': [
            include('whitespace'),
            (words(['read', 'sort']), Keyword),
            (words(['execute', 'integers', 'iterate', 'reverse', 'strings']),
             Keyword, ('group')),
            (words(['function', 'macro']), Keyword, ('group', 'group')),
            (words(['entry']), Keyword, ('group', 'group', 'group')),
        ],
        'group': [
            include('whitespace'),
            (r'\{', Punctuation, ('#pop', 'group-end', 'body')),
        ],
        'group-end': [
            include('whitespace'),
            (r'\}', Punctuation, '#pop'),
        ],
        'body': [
            include('whitespace'),
            (r"\'[^#\"\{\}\s]+", Name.Function),
            (r'[^#\"\{\}\s]+\$', Name.Builtin),
            (r'[^#\"\{\}\s]+', Name.Variable),
            (r'"[^\"]*"', String),
            (r'#-?\d+', Number),
            (r'\{', Punctuation, ('group-end', 'body')),
            default('#pop'),
        ],
        'whitespace': [
            ('\s+', Text),
            ('%.*?$', Comment.SingleLine),
        ],
    }
