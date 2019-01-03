from django.db import models

class Name(models.Model):
	"""The name for each story."""
	text = models.CharField(max_length=300)
	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text

class Story(models.Model):
	"""Each individual story."""
	name = models.ForeignKey(Name, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'stories'

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.text) > 50:
			return self.text[:50] + "[...]"
		else: 
			return self.text
