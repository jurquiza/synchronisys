from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Parameter(models.Model):
	component = models.CharField(max_length=50)
	
	PROCESS = (
		('G', 'general'),
		('Comp','compartment'),
		('Kd', 'binding'),
		('TS','transcription'),
		('TL', 'translation'),
		('GL', 'gene length'),
		('TSr','transcription rate'),
		('mRdeg','mRNA degradation'),
		('CDSL','CDS Length'),
		('pDeg','protein degradation'),
		('traloc','translocation'),
	)
	INTER_TYPE = (
	('None', 'none'),
	('Prot-DNA', 'protein-DNA'),
	('Prot-Prot','protein-protein' ),


	)


	process = models.CharField(default='general', max_length=50, choices=PROCESS)
	interaction_type = models.CharField(default='none', max_length=50, choices=INTER_TYPE)
	units = models.CharField(max_length=50)
	value = models.FloatField(default=0)
	PMID = models.IntegerField(default=0)
	first_author = models.CharField(default ='First Author', max_length=200)
	URL = models.URLField(default='www.reference_urls.com',max_length=300)
	notes = models.TextField(default='comments related to the parameter')
	
	def __unicode__(self):
		return self.component

