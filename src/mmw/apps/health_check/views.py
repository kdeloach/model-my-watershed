# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from rest_framework.response import Response
from rest_framework import decorators
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer


@decorators.api_view(['GET'])
@decorators.permission_classes((AllowAny, ))
@decorators.renderer_classes((JSONRenderer,))
def health_check(request):
    return Response({
        'status': 'OK'
    })
