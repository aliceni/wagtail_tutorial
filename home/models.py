from django.db import models

from wagtail.core.models import Page

from blog.models import BlogPage


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["blog_page"] = BlogPage.objects.first()
        return context
