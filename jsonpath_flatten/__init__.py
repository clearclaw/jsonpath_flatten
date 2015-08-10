#! /usr/bin/env python

from ._version import get_versions
__version__ = get_versions()['version']
__version_info__ = get_versions ()
del get_versions

import binascii, collections, fnmatch, logging, logtool, string

LOG = logging.getLogger (__name__)

@logtool.log_call
def isprintable (s):
  if isinstance (s, str):
    return (c in string.printable for c in s)
  return False

class FlattenDict (object):

  @logtool.log_call (log_args = False)
  def __init__ (self, data, patterns = None):
    self.data = data
    self.patterns = patterns if patterns else []

  # @logtool.log_call (log_args = False, log_rc = False)
  def pattern_hit (self, key):
    for pattern in self.patterns:
      if fnmatch.fnmatch (key, pattern): # Discard matches
        return True
    return False

  # @logtool.log_call (log_args = False)
  def flatten_list (self, l, parent_key = '', sep = '.'):
    items = []
    items.append ((parent_key + sep + "#" + "count", len (l)))
    for i in xrange (len (l)):
      new_key = parent_key + ("[%d]" % i if parent_key else "%d" % i)
      items.extend (self.flatten_item (l[i], new_key, sep = sep))
    return items

  # @logtool.log_call (log_args = False)
  def flatten_dict (self, d, parent_key = '', sep = '.'):
    items = []
    for k, v in d.items ():
      new_key = parent_key + sep + k if parent_key else k
      items.extend (self.flatten_item (v, new_key, sep = sep))
    return items

  # @logtool.log_call (log_args = False)
  def flatten_item (self, i, parent_key = '', sep = '.'):
    items = []
    if isinstance (i, collections.MutableMapping): # Dictionary
      items.extend (self.flatten_dict (i, parent_key, sep = sep))
    elif isinstance (i, collections.MutableSequence):
      items.extend (self.flatten_list (i, parent_key, sep = sep))
    else:
      items.append ((parent_key, i))
    return items

  @logtool.log_call (log_args = False, log_rc = False)
  def flatten (self, d, parent_key = '', sep = '.'):
    return dict (self.flatten_item (d, parent_key, sep = sep))

  @logtool.log_call (log_args = False, log_rc = False)
  def run (self):
    rc = dict ()
    discards = []
    flat = self.flatten (self.data)
    for key, value in flat.items ():
      if self.pattern_hit (key):
        discards.append (key)
        continue # Discard matches
      if isinstance (value, str) and not isprintable (value):
        value = value.encode ("hex")
      rc[key] = value
    return rc, discards

@logtool.log_call (log_args = False)
def jsonpath_flatten (data, patterns = None):
  return FlattenDict (data, patterns).run ()
