#  This file is part of the myhdl library, a Python package for using
#  Python as a Hardware Description Language.
#
#  Copyright (C) 2003 Jan Decaluwe
#
#  The myhdl library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation; either version 2.1 of the
#  License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

""" Module that implements enum.

"""

__author__ = "Jan Decaluwe <jan@jandecaluwe.com>"
__revision__ = "$Revision$"
__date__ = "$Date$"

from types import StringType


def enum(*args):

    # args = args
    # only default encoding for now
    argdict = {}
    encoding = {}
    i = 0
    for arg in args:
        if type(arg) is not StringType:
            raise TypeError
        if encoding.has_key(arg):
            raise ValueError("enum literals should be unique")
        argdict[i] = arg
        encoding[arg] = i
        i += 1
        
    class EnumItem(object):
        def __init__(self, arg):
            self._val = encoding[arg]
        def __repr__(self):
            return argdict[self._val]
        __str__ = __repr__

    class Enum(object):
        def __init__(self):
            for slot in args:
                self.__dict__[slot] = EnumItem(slot)
        def __setattr__(self, attr, val):
            raise AttributeError("Cannot assign to enum attributes")
        def __len__(self):
            return len(args)
        def __repr__(self):
            return "<Enum: %s>" % ", ".join(args)
        __str__ = __repr__
        
    return Enum()




    
        