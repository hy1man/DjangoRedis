from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from redis import StrictRedis


def aa(request):
    # sr = StrictRedis(host='localhost',port=6739,db=0)
    # 如果参数host。port.db都是默认的情况下可以简写成下面这样的
    # sr = StrictRedis(decode_responses='Ture')  # decode_responses='Ture'编码

    sr=get_redis_connection()

    sr.set("aa", '111')

    sr.set("bb", '222')
    sr.set("e", '中国')
    result = sr.set("cc", '333')
    # print(result)  # 打印ture表示添加成功
    a = sr.get('aa')
    b = sr.get('bb')
    c = sr.get('cc')  # sr是StrictaRedis的对象，
    # 具有很多属性，set。get等get（‘aa’）是就求aa的值
    e = sr.get('e')
    # print('%s%s%s' % (a, b, c), e)
    # print(a, b, c)
    text='aa=%s,bb=%s,cc=%s,e=%s'%(a,b,c,e)



    return HttpResponse(text)


def set_session(request):
    """"保存session数据"""

    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存session数据成功')


def get_session(request):
    """获取session数据"""

    username = request.session.get('username')
    verify_code = request.session.get('verify_code')
    text = 'username=%s, verify_code=%s' % (username, verify_code)
    return HttpResponse(text)