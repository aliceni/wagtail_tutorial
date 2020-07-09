from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ColumBlock(blocks.StreamBlock):

    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = "blog/blocks/column_block.html"


class TwoColumnBlock(blocks.StructBlock):

    left_column = ColumBlock(icon="arrow-right", label="Left column content")
    right_column = ColumBlock(icon="arrow-right", label="Right column content")

    class Meta:
        template = "blog/blocks/two_column_block.html"
        icon = "placeholder"
        label = "Two Columns"
