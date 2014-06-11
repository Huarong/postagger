#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

ROOT = os.path.dirname(os.path.dirname(__file__))


def abs_path(path):
    return os.path.join(ROOT, path)
