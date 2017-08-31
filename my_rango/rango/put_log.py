#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import Project




def put_log(opj_project,old_tag, new_tag, msg):
    content = opj_project.log

    if old_tag == new_tag:
        content = content + msg
    else:
        content = content + timezone.now + new_tag


