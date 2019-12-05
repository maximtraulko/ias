#!/usr/bin/env python
# -*- coding: utf-8 -*-
configs = {
    "prod": {
      "sso": {"login_url": "https://login.nstu.ru/ssoservice/XUI/#login/&goto=%s",
              "logout_url": "https://login.nstu.ru/ssoservice/json/sessions/%s?_action=logout",
              "validate_url": "https://login.nstu.ru/ssoservice/json/sessions/%s?_action=validate",
              "token": "NstuSsoToken"}
    }
}

CONFIG = configs["prod"]
