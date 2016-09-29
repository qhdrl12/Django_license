from django.http.response import HttpResponse
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from user.models import Stb, PhysicalStb
from user.serializers import StbSerializers, PhysicalSerializers

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

    @list_route(methods=['get'])
    def recent_users(self, request):
        recent_users = Stb.objects.all()
        #recent_users = Stb.objects.get(iptv_status_code='1')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

class PhysicalViewSet(viewsets.ModelViewSet):
    queryset = PhysicalStb.objects.filter(stb__iptv_status_code=1)

    serializer_class = PhysicalSerializers

    # @list_route(methods=['get'])
    # def recent_phystbs(self, request):
    #     recent_phystbs = PhysicalStb.objects.select_related()
    #
    #     page = self.paginate_queryset(recent_phystbs)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(recent_phystbs, many=True)
    #     return Response(serializer.data)

# class searchStbChAuthorityViewSet(viewsets.ModelViewSet):
#     cursor = connection.cursor()
#     queryset = "select HANARO_SMS.FN_GET_STB_CH('{9971DC42-C5AF-11E1-95E0-B9F37246EB3C}') from dual"
#     cursor.execute(queryset)
#
#     row = cursor.fetchall()
#     result = row[0][0].read()
#
#     print(result)
