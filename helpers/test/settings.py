#-*- coding: utf-8 -*-
"""
helpers.test.settings

Settings for test utils.

* created: 2013-07-20 Kevin Chan <kefin@makedostudio.com>
* updated: 2013-10-27 kchan
"""

from garage import get_setting as _s


# template to define test users
# * each part contains a '%s' for appending a suffix to the base
# ('username_base', 'password_base', 'email_base',)
DEFAULT_TEST_USER_TEMPLATE = (
    'testuser_%s',
    'aVCYboFx3x_%s',
    'testuser_%s@example.com',
)
TEST_USER_TEMPLATE = _s('TEST_USER_TEMPLATE', DEFAULT_TEST_USER_TEMPLATE)

# divider for test diagnostic printouts (used by msg())
DIVIDER = '# ----------------------------------------------------------------------'