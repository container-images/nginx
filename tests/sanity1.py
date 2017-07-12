#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This Modularity Testing Framework helps you to write tests for modules
# Copyright (C) 2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# he Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors: Rado Pitonak <rpitonak@redhat.com>
#

from avocado import main
from avocado.core import exceptions
from moduleframework import module_framework


class SanityCheck1(module_framework.AvocadoTest):
    """
    :avocado: enable
    """

    def test2Version(self):
        """
        Check if nginx is installed in correct version
        """

        version = "1."
        self.start()

        # For some reason, nginx -v spits out the version number to stderr
        self.run("nginx -v 2>&1 | grep {}".format(version))

    def test3ServiceRunning(self):
        """
        Check if nginx is running
        """

        self.start()
        self.run('ls  /proc/*/exe -alh | grep nginx')


if __name__ == '__main__':
    main()
