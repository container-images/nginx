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
import time
from avocado.core import exceptions
from moduleframework import module_framework


class ConfigurationCheck(module_framework.AvocadoTest):
    """
    :avocado: enable
    """

    def testConfChange(self):
        """
        Test change the root directory in the configuration file of running nginx.
        Then nginx is reloaded and should load website from new root directory.
        """
        
        self.start()
        conf_path = "/etc/nginx/nginx.conf"

        content = "<html><body><h1>Nginx is running in container!</h1></body></html>"
        root = "/tmp/app-root"

        # create website for testing
        self.run("mkdir {}".format(root))
        self.run("echo '{}' >> {}/index.html".format(content, root))

        # change the root directory inside conf file
        self.run("sed -i 's/root.*$/root \/tmp\/app-root\/;/g' {}".format(conf_path))
        self.run("nginx -s reload")

        time.sleep(5)

        # request content from host
        self.assertIn('{}\n'.format(content), self.runHost("curl 127.0.0.1:80").stdout)


if __name__ == '__main__':
    main()
