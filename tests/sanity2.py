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
import time


class SanityCheck2(module_framework.AvocadoTest):
    """
    :avocado: enable
    """

    def test1Port80(self):
        """
        Request to localhost inside the container to make sure that server running on port 80
        """
        
        self.start()
        time.sleep(2)
        self.run("curl 127.0.0.1:80")

    def test2WebsiteContent(self):
        """
        Check if nginx display correct content
        """

        content = "<html><body><h1>Nginx is running in container!</h1></body></html>"
        root = "/usr/share/nginx/"

        self.start()

        # create simple static  website inside the container
        self.run("touch {}/html/index.html".format(root))
        self.run("echo '{}' >> {}/html/index.html".format(content, root))

        # compare content returned by request from host with original content
        self.assertIn('{}\n'.format(content), self.runHost("curl 127.0.0.1:80").stdout)

    def test3Port443(self):
        """
        Test configure server to listen also on port 443 and make request from host.
        """

        conf_path = "/etc/nginx/nginx.conf"
        self.start()
        time.sleep(2)

        # Make the server listen on port 443.
        self.run("sed -i 's/server {}$/ server {} listen 443;/g' {}".format("{{", "{{", conf_path))
        # reload nginx to apply changes
        self.run("nginx -s reload")
        time.sleep(5)

        self.runHost("curl 127.0.0.1:443")


if __name__ == '__main__':
    main()
