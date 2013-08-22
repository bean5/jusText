# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import re
import os
import sys
import pkgutil


MULTIPLE_WHITESPACE_PATTERN = re.compile(r"\s+", re.UNICODE)
def normalize_whitespace(string):
    """Translates multiple white-space into single space."""
    return MULTIPLE_WHITESPACE_PATTERN.sub(" ", string)


def is_blank(string):
    """
    Returns `True` if string contains only white-space characters
    or is empty. Otherwise `False` is returned.
    """
    return not bool(string.lstrip())


def get_stoplists():
    """Returns a collection of built-in stop-lists."""
    path_to_stoplists = os.path.dirname(sys.modules["justext"].__file__)
    path_to_stoplists = os.path.join(path_to_stoplists, "stoplists")

    stoplist_names = []
    for filename in os.listdir(path_to_stoplists):
        name, extension = os.path.splitext(filename)
        if extension == ".txt":
            stoplist_names.append(name)

    return tuple(stoplist_names)


def get_stoplist(language):
    """Returns an built-in stop-list for the language as a set of words."""
    file_path = os.path.join("stoplists", "%s.txt" % language)
    try:
        stopwords = pkgutil.get_data("justext", file_path)
    except IOError:
        raise ValueError("Stoplist for language %s is missing. Please use function 'get_stoplists' for complete list of stoplists and feel free to contribute by your own stoplist." % language)

    return frozenset(w.decode("utf8") for w in stopwords.splitlines())