from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class BlogPage(Page):

    description = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full")
    ]
