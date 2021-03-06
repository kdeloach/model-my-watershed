# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from apps.bigcz.clients import hydroshare, cuahsi, cinergi


SEARCH_FUNCTIONS = {
    hydroshare.CATALOG_NAME: hydroshare.search,
    cuahsi.CATALOG_NAME: cuahsi.search,
    cinergi.CATALOG_NAME: cinergi.search,
}
