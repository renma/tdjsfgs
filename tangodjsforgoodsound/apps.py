# Time-stamp: <2025-12-21 06:59:11 rene>
#
# Copyright (C) 2017 Rene Maurer
# This file is part of tangodjsforgoodsound.
#
# tangodjsforgoodsound is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# tangodjsforgoodsound is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------


from django.apps import AppConfig
from django.conf import settings

import hashlib
import logging
import os
import sys
from . import version


logger = logging.getLogger("tdjsfgs")


class TangodjsforgoodsoundConfig(AppConfig):

    name = "tangodjsforgoodsound"

    def ready(self):
        if not os.environ.get("RUN_MAIN"):
            logger.info("Server start, Version %s" % version.__version__)
            logger.info("Python Version %s" % (sys.version.split()[0]))
            try:
                dbname = "db.sqlite3"
                x = hashlib.md5(open(dbname, "rb").read()).hexdigest()
                logger.info("DB=%s, MD5=%s" % (dbname, x))
                x = os.path.isfile(settings.ENABLE_EXISTING_LOGGERS)
                logger.info("DEBUG=%s, exceptions to console=%s" % (settings.DEBUG, x))
            except Exception as e:
                logger.info(e)
            # Create a media directory
            if settings.MEDIA_ROOT and not os.path.exists(settings.MEDIA_ROOT):
                logger.info("create %s" % settings.MEDIA_ROOT)
                os.makedirs(settings.MEDIA_ROOT)
