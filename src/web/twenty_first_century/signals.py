from django.db import models
from django.dispatch import receiver

from .models import ScrapyModel
from .tasks import start_handler_product


@receiver(models.signals.post_save, sender=ScrapyModel)
def post_save_profile_model(sender, instance, **kwargs):
    if instance.data:
        start_handler_product.delay(pk=instance.pk)