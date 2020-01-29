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


class StorageBase:
    def __init__(self, config):
        self.config = config

    def configure(self):
        pass

    def get_info(self):
        pass

    def flush_cache(self):
        pass
