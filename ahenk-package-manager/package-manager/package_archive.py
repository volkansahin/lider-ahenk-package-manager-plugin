#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Cemre ALPSOY <cemre.alpsoy@agem.com.tr>

from base.plugin.abstract_plugin import AbstractPlugin
from base.model.enum.ContentType import ContentType
import json


class PackageArchive(AbstractPlugin):
    def __init__(self, data, context):
        super(AbstractPlugin, self).__init__()
        self.data = data
        self.context = context
        self.logger = self.get_logger()
        self.message_code = self.get_message_code()

    def handle_task(self):
        print('Handling Package Archive Task')
        self.logger.debug('Handling Package Archive Task')
        try:
            resultMessage = ''
            package_name = str((self.data)['packageName'])
            package_version = str((self.data)['packageVersion'])
            self.logger.debug("[PACKAGE MANAGER] Installing new package... {0}".format(package_name))
            self.install_with_apt_get(package_name, package_version)
            resultMessage += 'Paket başarıyla kuruldu - {0}={1}'.format(package_name, package_version)
            self.logger.debug(resultMessage)
            self.context.create_response(code=self.message_code.TASK_PROCESSED.value,
                                         message=resultMessage)
        except Exception as e:
            self.logger.debug(str(e))
            self.context.create_response(code=self.message_code.TASK_ERROR.value, message='Önceki paket sürümü kurulumunda beklenmedik hata!', content_type=ContentType.APPLICATION_JSON.value)


def handle_task(task, context):
    print('PackageManager Plugin Task')
    print('Task Data : {}'.format(str(task)))
    plugin = PackageArchive(task, context)
    plugin.handle_task()
