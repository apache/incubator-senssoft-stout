# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.staticfiles import views as vs
from exp_portal import views

urlpatterns= patterns('',
	url(r'^$', views.home_page, name='home'),
	url(r'^status$', views.view_status, name='view_status'),
	url(r'^experiments/manage$', views.manage_exps, name='manage_exps'),
	url(r'^experiments/details/(?P<exppk>.*)$', views.view_exp_details, name='view_exp_details'),
	url(r'^experiment/edit/(?P<exppk>.*)$', views.edit_exp, name='edit_exp'),
	url(r'^experiments/add$', views.add_exp, name='add_exp'),
	url(r'^data/manage$', views.manage_datasets, name='manage_datasets'),
	url(r'^data/add$', views.add_dataset, name='add_dataset'),
	url(r'^data/details/(?P<datasetpk>.*)$', views.view_dataset_details, name='view_dataset_details'),
	url(r'^data/edit/(?P<datasetpk>.*)$', views.edit_dataset, name='edit_dataset'),
	url(r'^products$', views.view_products, name='view_products'),
	url(r'^products/add$', views.add_product, name='add_product'),
	url(r'^products/new$', views.new_product, name='new_product'),
	url(r'^products/manage$', views.manage_products, name='manage_products'),
	url(r'^products/details/(?P<productname>.*)$', views.view_product_details, name='view_product_details'),
	url(r'^products/edit/(?P<productpk>.*)$', views.edit_product, name='edit_product'),
	url(r'^tasks$', views.view_tasks, name='view_tasks'),
	url(r'^tasks/add$', views.add_task, name='add_task'),
	url(r'^tasks/new$', views.new_task, name='new_task'),
	url(r'^tasks/completed$', views.view_completed, name='view_completed'), 
	url(r'^tasks/incomplete$', views.view_incomplete, name='view_incomplete'),
	url(r'^tasks/manage$', views.manage_tasks, name='manage_tasks'),
	url(r'^tasks/details/(?P<taskname>.*)$', views.view_task_details, name='view_task_details'),
	url(r'^tasks/edit/(?P<taskpk>.*)$', views.edit_task, name='edit_task'),
	url(r'^tasks/delete/(?P<taskpk>.*)$', views.delete_task, name='delete_task'), 
	url(r'^users$', views.view_users, name='view_users'), 
	url(r'^users/manage$', views.manage_users, name='manage_users'),
	url(r'^users/edit/(?P<userprofilepk>.*)$', views.edit_user, name='edit_user'),
	url(r'^users/add$', views.add_user, name='add_user'),
	url(r'^users/delete/(?P<userprofilepk>.*)$', views.delete_user, name='delete_user'),
	url(r'^users/new$', views.new_user, name='new_user'),
	url(r'^users/created$', views.user_added, name='user_added'),
	url(r'^users/tasks/add/(?P<userpk>.*)$', views.add_user_task, name='add_user_task'),
	url(r'^users/tasks/update/(?P<userpk>.*)/(?P<datasetpk>.*)/(?P<productpk>.*)/(?P<taskpk>.*)', views.update_user_tasks, name='update_user_tasks'),
	url(r'^users/tasks/viewall/(?P<profile>.*)$', views.view_user_tasks, name='view_user_tasks'),
	url(r'^experiment/products/$', views.view_experiment_products, name='view_experiment_products'),
	url(r'^email/$', views.send_email, name='send_email'),
	)

# print settings.DEBUG, settings.STATIC_ROOT
if settings.DEBUG:
    urlpatterns += url(r'^static/(?P<path>.*)$', vs.serve),