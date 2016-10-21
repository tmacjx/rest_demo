# coding=utf-8
"""
author: wk
version: 1.0
"""
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')