from django.db import models

def PublicManager(models.Manager):
	def get_query_set(self):
		return super(PublicManager, self).get_query_set().filter(public=True)
