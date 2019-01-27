import requests
import json
from django.db import models

URL = 'https://gturnquist-quoters.cfapps.io/api/random'

class SpringService(models.Model):
    response_type = models.CharField(max_length=16, blank=True)
    response_id = models.IntegerField(blank=True)
    response_quote = models.TextField(default='', blank=True)

    def set_info_from_service(self):
        response = requests.get(URL)
        if response.status_code == 200:
            response_obj = json.loads(response.content.decode('utf-8'))
            self.response_type = response_obj.get('type', '')
            self.response_id = response_obj['value']['id']
            self.response_quote = response_obj['value']['quote']

    def save(self, *args, **kwargs):
        self.set_info_from_service()
        return super().save(*args, **kwargs)