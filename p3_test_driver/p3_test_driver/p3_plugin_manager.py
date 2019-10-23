# Written by Claudio Fahey (claudio.fahey@emc.com)

from __future__ import division
import logging
import os
from yapsy.PluginManager import PluginManager
from yapsy.PluginFileLocator import PluginFileLocator, PluginFileAnalyzerMathingRegex
from yapsy.IPlugin import IPlugin

from . import p3_test_driver

_plugin_toc = {}

def _get_item_key(class_type, class_name):
    return '%s:%s' % (class_type, class_name)

def _get_plugin_dirs():
    logging.info(p3_test_driver.__file__)
    maindir = os.path.dirname(os.path.realpath(p3_test_driver.__file__))
    return [
        os.path.join(maindir, 'plugins'),
        os.path.join(os.getcwd(), 'p3_test_driver_plugins'),
    ]

def scan_plugins():
    global _plugin_toc
    _plugin_toc = {}

    # Load the plugins from the plugin directory.
    analyzer = PluginFileAnalyzerMathingRegex('', '.*\\.py$')
    plugin_locator = PluginFileLocator(analyzers=[analyzer])
    manager = PluginManager(plugin_locator=plugin_locator)
    plugin_dirs = _get_plugin_dirs()
    logging.info('Loading plugins in %s' % str(plugin_dirs))
    manager.setPluginPlaces(plugin_dirs)
    manager.collectPlugins()

    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        plugin_info = plugin.plugin_object.get_plugin_info()
        for item in plugin_info:
            k = _get_item_key(item['class_type'], item['class_name'])
            _plugin_toc[k] = item
    logging.debug('p3_plugin_manager: _plugin_toc=%s' % _plugin_toc)

def get_class_property(class_type, class_name, property_name, default=None):
    global _plugin_toc
    k = _get_item_key(class_type, class_name)
    print('k=%s, property_name=%s' % (k, property_name))
    value = _plugin_toc[k].get(property_name, default)
    print('value=%s' % value)
    return value

def get_class(class_type, class_name):
    global _plugin_toc
    k = _get_item_key(class_type, class_name)
    return _plugin_toc[k]['class']

class IP3Plugin(IPlugin):
    def get_plugin_info(self):
        return []
