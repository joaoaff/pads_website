'''
Created on 11/10/2015

@author: joaoff
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_pt, name='main_pt'), # e.g. /pads/
    url(r'^equipe/$', views.equipe, name='equipe'), # e.g. /main_pt/equipe/
    url(r'^atividades/$', views.atividades, name='atividades'), # e.g. /main_pt/atividades/
    url(r'^publicacoes/$', views.equipe, name='publicacoes'), # e.g. /main_pt/publicacoes/
    url(r'^contato/$', views.equipe, name='contato'), # e.g. /main_pt/contato/
]