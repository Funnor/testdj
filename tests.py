#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import reverse
from django.test import TestCase


class ScoreTests(TestCase):
    def test_score_view_status_code(self):
        url = reverse('score')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)