# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pwn

# Create your views here.


def rec(obj_str, depth, type_list, flat_list):
    try:
        obj = eval(obj_str)
    except AttributeError:
        return
    if type(obj) in type_list:
        return
    type_list.append(type(obj))
    flat_list.append({'start_node': True, 'data': obj_str})
    flat_list.append({'is_data': True, 'data': obj_str, 'link': obj_str.replace('.', '/')})
    flat_list.append({'end_node': True})
    flat_list.append({'start_nodes': True, 'data': obj_str})
    if hasattr(obj, '__dict__'):
        for child_str in obj.__dict__:
            rec(obj_str + '.' + child_str, depth + 1, type_list, flat_list)
    flat_list.append({'end_nodes': True})
    type_list.pop()


def index(request):
    context = {'flat_list': []}
    rec('pwn', 0, [], context['flat_list'])
    return render(request, 'show_docs/index.html', context)


def get_docs(request, match):
    if '.' in match:
        raise Exception
    context = {}
    context['title'] = (match.strip('/').replace('/', '.')).strip('.')
    context['docs'] = eval(context['title'] + '.__doc__')
    return render(request, 'show_docs/get_docs.html', context)


def error(request):
    context = {}
    response = render(request, 'show_docs/error.html', context)
    response.status_code = 404
    return response
