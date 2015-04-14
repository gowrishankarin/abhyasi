#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-04-14 14:58:27
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-04-14 22:52:57

from django import forms
from django.forms import widgets
from django.contrib.admin import widgets


from .models import Abhyasi, Sitting

class AbhyasiForm(forms.ModelForm):

	class Meta:
		model = Abhyasi
		fields = ('name', 'biography', 'id_card_number', 'date_of_birth', 
			'date_of_join', 'email', 'address')

class SittingForm(forms.ModelForm):

	class Meta:
		model = Sitting
		fields = ('date', 'findings', 'experiences')

	def __init__(self, *args, **kwargs):
		super(SittingForm, self).__init__(*args, **kwargs)
		self.fields['date'].widget = widgets.AdminSplitDateTime()