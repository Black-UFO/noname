import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api import *


@api_view(["GET"])
def getApiList(request):
    apiList = [{
        "link": "api1/"
    }, {
        "link": "api2/"
    }, {
        "link": "api3/"
    }, {
        "link": "api4/"
    }, {
        "link": "api5/"
    }, {
        "link": "api6/"
    }, {
        "link": "api7/"
    }, {
        "link": "api8/"
    }, {
        "link": "api9/"
    }, {
        "link": "api10/"
    }, {
        "link": "api11/"
    }, {
        "link": "api12/"
    }, {
        "link": "api13/"
    }, {
        "link": "api14/"
    }, {
        "link": "api15/"
    }, {
        "link": "api16/"
    }, {
        "link": "api17/"
    }, {
        "link": "api18/"
    }, {
        "link": "api19/"
    }, {
        "link": "api20/"
    }]
    return Response(apiList, status=200)


@api_view(["POST"])
def api_1(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api1(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_2(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api2(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_3(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api3(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_4(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api4(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_5(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api5(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_6(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api6(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_7(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api7(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_8(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api8(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_9(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api9(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_10(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api10(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_11(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api11(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_12(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api12(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_13(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api13(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_14(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api14(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_15(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api15(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_16(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api16(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_17(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api17(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_18(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api18(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_19(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api19(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_20(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api20(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_21(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api21(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_22(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api22(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_23(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api23(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_24(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api24(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_25(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api25(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_26(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api26(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_27(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api27(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_28(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api28(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_29(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api29(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_30(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api30(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_31(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api31(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_32(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api32(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_33(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api33(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_34(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api34(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_35(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api35(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_36(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api36(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_37(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api37(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_38(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api38(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_39(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api39(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_40(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api40(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_41(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api41(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_42(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api42(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_43(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api43(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_44(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api44(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_45(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api45(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_46(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api46(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_47(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api47(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_48(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api48(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_49(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api49(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_50(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api50(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_51(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api51(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_52(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api52(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_53(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api53(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_54(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api54(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_55(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api55(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_56(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api56(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_57(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api57(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_58(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api58(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_59(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api59(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_60(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api60(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_61(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api61(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_62(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api62(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_63(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api63(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_64(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api64(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_65(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api65(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_66(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api66(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_67(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api67(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_68(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api68(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_69(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api69(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_70(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api70(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_71(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api71(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_72(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api72(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_73(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api73(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_74(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api74(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_75(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api75(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_76(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api76(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_77(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api77(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_78(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api78(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_79(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api79(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_80(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api80(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_81(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api81(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_82(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api82(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_83(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api83(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_84(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api84(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_85(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api85(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_86(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api86(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_87(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api87(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_88(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api88(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_89(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api89(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_90(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api90(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_91(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api91(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_92(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api92(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_93(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api93(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_94(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api94(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_95(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api95(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_96(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api96(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_97(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api97(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_98(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api98(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_99(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api99(number)
    return HttpResponse("OK", status=200)


@api_view(["POST"])
def api_100(request):
    body = json.loads(request.body.decode('utf-8'))
    number = body["number"]
    repeat = body["repeat"]

    for ele in range(0, repeat):
        api100(number)
    return HttpResponse("OK", status=200)
