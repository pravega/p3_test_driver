#
# Copyright (c) Dell Inc., or its subsidiaries. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

from __future__ import division

import logging

# P3 Libraries
from p3_test_driver import p3_plugin_manager
from p3_test_driver.p3_storage import StorageBase
from p3_test_driver.system_command import ssh


class PluginInfo(p3_plugin_manager.IP3Plugin):
    def get_plugin_info(self):
        return [
            {'class_type': 'storage', 'class_name': 'ecs', 'class': ECSStorage},
            ]

class ECSStorage(StorageBase):
    def configure(self):
        config = self.config
        self.get_info()        
        self.flush_cache()

    def get_info(self):
        config = self.config
        self.get_storage_node_info()
        config['storage_version'] = self.run_storage_command('cat /etc/issue')[1]
        config['storage_docker_ps'] = self.run_storage_command('sudo docker ps')[1]

    def run_storage_command(self, cmd, *args, **kwargs):
        config = self.config
        assert 'storage_user' in config
        assert 'storage_host' in config
        if config['noop']:
            logging.info('# ssh ' % cmd)
            return 0, ''
        else:
            return ssh(config['storage_user'], config['storage_host'], cmd, *args, **kwargs)

    def get_storage_node_info(self, force=False):
        config = self.config
        return None

    def flush_cache(self):
        config = self.config
        if not config['noop'] and config['storage_flush']:
            raise Exception('flush_cache not supported')
