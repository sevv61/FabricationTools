# -*- coding: utf-8 -*-
"""
config.py

Configuration manager for Fabrication Tools.

Reads and writes settings stored in config/settings.json.
"""

from __future__ import print_function

import json
import os


class ConfigManager(object):
    """Loads and saves Fabrication Tools settings."""

    def __init__(self):
        extension_root = os.path.dirname(os.path.dirname(__file__))

        self.settings_file = os.path.join(
            extension_root,
            "config",
            "settings.json"
        )

        self.settings = {}

        self.load()

    def load(self):
        """Load settings from disk."""

        if not os.path.exists(self.settings_file):
            raise Exception(
                "Settings file not found:\n{}".format(self.settings_file)
            )

        with open(self.settings_file, "r") as fp:
            self.settings = json.load(fp)

    def save(self):
        """Save settings back to disk."""

        with open(self.settings_file, "w") as fp:
            json.dump(
                self.settings,
                fp,
                indent=4,
                sort_keys=True
            )

    def get(self, key, default=None):
        """Return a setting."""

        return self.settings.get(key, default)

    def set(self, key, value):
        """Update a setting."""

        self.settings[key] = value

    def reload(self):
        """Reload settings from disk."""

        self.load()

    def all(self):
        """Return the entire settings dictionary."""

        return self.settingszsxaaaaaa 