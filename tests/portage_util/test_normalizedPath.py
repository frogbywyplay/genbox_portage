# test_normalizePath.py -- Portage Unit Testing Functionality
# Copyright 2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

from unittest import TestCase

class NormalizePathTestCase(TestCase):
	
	def testNormalizePath(self):
		
		from portage_util import normalize_path
		path = "///foo/bar/baz"
		good = "/foo/bar/baz"
		self.assertEqual(normalize_path(path), good)
