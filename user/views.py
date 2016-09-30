from django.db import connection
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route, api_view, renderer_classes
from rest_framework.response import Response
from user.models import Stb, PhysicalStb
from user.serializers import StbSerializers, PhysicalSerializers

from django.core.cache import cache
from django_redis import get_redis_connection


from django.http.response import HttpResponse
from rest_framework import exceptions

# Create your views here.
# def user_page(request):
#     user_list = BUser.objects.all()
#     #print(user_list)
#
#     result_list = []
#     for user in user_list:
#         ipcd = '0';
#         if user.iptv_status_code:
#             ipcd = user.iptv_status_code
#         result_list.append({'stb_id': user.stb_id, 'iptv_status_code': ipcd})
#     return HttpResponse('Hello' + str(result_list))

class StbViewSet(viewsets.ModelViewSet):

    queryset = Stb.objects.all()
    serializer_class = StbSerializers

    # @list_route(methods=['get'])
    # def recent_users(self, request):
    #     print("get recent here")
    #     recent_users = Stb.objects.all()
    #     #recent_users = Stb.objects.get(iptv_status_code='1')
    #
    #     page = self.paginate_queryset(recent_users)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(recent_users, many=True)
    #     return Response(serializer.data)

    # @list_route(methods=['GET'])
    # def getStbFunction(self, request):
    #
    #     #print(self.get_object())
    #     print(request.data)
    #     # print(self.request.data)
    #
    #     # print(self.args.count())
    #     #some_param = self.request.query_params.get('stb_id')
    #     #if not some_param:
    #     #    raise exceptions.PermissionDenied
    #
    #     #print(self.request.stb_id)
    #
    #     cursor = connection.cursor()
    #     query = "select HANARO_SMS.FN_GET_STB_CH('{9971DC42-C5AF-11E1-95E0-B9F37246EB3C}') from dual"
    #     cursor.execute(query)
    #
    #     row = cursor.fetchall()
    #     result = row[0][0].read()
    #
    #    #print(result)
    #
    #     return Response(result)

class PhysicalViewSet(viewsets.ModelViewSet):
    queryset = PhysicalStb.objects.filter(stb__iptv_status_code=1)

    serializer_class = PhysicalSerializers

@api_view(['GET'])
def getStbFunction(request):
    sid = request.GET.get("stb_id")
    macAddr = request.GET.get("mac_addr")
    ch_auth = ''

    if sid:
        cursor = connection.cursor()
        query = "select HANARO_SMS.FN_GET_STB_CH('"+sid+"') from dual"
        cursor.execute(query)
        row = cursor.fetchall()

        result_txt = 'Ok'
        ch_auth = row[0][0].read()
    else:
        result_txt = 'Fail'
    result = {
        'channels_authority' : ch_auth,
        'stb_id' : sid,
        'result' : result_txt
    }

    return Response(result)