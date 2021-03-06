#!/usr/bin/env python

# Copyright (c) 2013 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Verifies that IPHONEOS_DEPLOYMENT_TARGET works.
"""

import TestGyp

import sys

import TestMac

if sys.platform != 'darwin':
  print('Test only for macOS')
  sys.exit(2)

if not TestMac.Xcode.HasIPhoneSDK():
  print('IPhone SDK not installed')
  sys.exit(2)

test = TestGyp.TestGyp(formats=['make', 'ninja', 'xcode'])

test.run_gyp('deployment-target.gyp', chdir='deployment-target')

test.build('deployment-target.gyp', test.ALL, chdir='deployment-target')

test.pass_test()

