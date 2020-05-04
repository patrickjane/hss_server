# -----------------------------------------------------------------------------
# HSS - Hermes Skill Server
# Copyright (c) 2020 - Patrick Fial
# -----------------------------------------------------------------------------
# http.py
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import logging
import requests

# -----------------------------------------------------------------------------
# class Http
# temporary HTTP bridge for TTS to rhasspy
# -----------------------------------------------------------------------------


class Http:

    # --------------------------------------------------------------------------
    # ctor
    # --------------------------------------------------------------------------

    def __init__(self, url):
        self.log = logging.getLogger(__name__)
        self.url = url

        logging.getLogger("requests").setLevel(logging.ERROR)
        logging.getLogger("urllib3").setLevel(logging.ERROR)

    # --------------------------------------------------------------------------
    # post
    # --------------------------------------------------------------------------

    def post(self, message):
        try:
            self.log.info("POST response to '{}'".format(self.url))
            self.log.debug("Response '{}'".format(message))

            headers = { "Content-Type": "text/plain; charset=utf-8" }

            req = requests.post(self.url, data = message.encode('utf8'), headers=headers)
        except Exception as e:
            self.log.error(
                "Failed to POST message to url '{}' ({})".format(self.url, e))

        if req.status_code != 200:
            self.log.error("HTTP POST failed ({})".format(req.status_code))
            return None

