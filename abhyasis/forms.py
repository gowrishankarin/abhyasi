#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-04-14 14:58:27
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-04-14 15:01:27

from django import forms

from .models import Abhyasi

class AbhyasiForm(forms.ModelForm):

	class Meta:
		model = Abhyasi
		fields = ('name', 'biography', 'id_card_number', 'date_of_birth', 
			'date_of_join', 'email', 'address')