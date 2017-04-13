from django.db import models

class ApprovedManager(models.Manager):

    use_for_related_fields = True

    def approved(self, **kwargs):
        return self.exclude(approved__exact=False)