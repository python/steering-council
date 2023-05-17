#! /usr/bin/env python
"""Destructively* link PEPs in the given Markdown document.

"PEP nnnn" or "PEP nnnn (title)" are converted to "[PEP nnnn](url) (title)".

* The document is changed "destructively". Make a backup (e.g. `git add`)
  before runnig the tool.

This is just a simple helper for simple cases. Always check its work.
"""

import re
import fileinput
import urllib.request
import json

PEP_RE = re.compile(
    r'''
        (?<!\[)          # Don't process links (square bracket before 'PEP')
        PEP              # 'PEP'
        (\s|-)*          # Whitespace or dash(es)
        (?P<num>\d+)     # PEP number
        \s*              # Optional whitespace
        (                # Optionally:
          \(             #  parenthesized
            (?P<title>   #   title
              [^)]+      #    (anything except end-parenthesis)
            )
          \)
        )?
    ''',
    re.VERBOSE,
)

def linkify(match):
    number = int(match['num'])
    title = match['title'] or get_title(number)
    return f'[PEP {number}](https://peps.python.org/pep-{number:04}/) ({title})'

def get_title(number):
    global pep_info
    try:
        pep_info
    except NameError:
        with urllib.request.urlopen('https://peps.python.org/api/peps.json') as response:
            pep_info = json.load(response)
    return pep_info[str(number)]['title']


for line in fileinput.input(inplace=True):
    print(PEP_RE.sub(linkify, line.rstrip()))
