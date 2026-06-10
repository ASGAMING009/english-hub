from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet # Moved to the top

# --- 1. HOME PAGE ---
class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        # Pulling both blog posts and the new events snippet
        context['blog_pages'] = BlogPage.objects.live().public().order_by('-first_published_at')
        context['upcoming_events'] = Event.objects.all()
        return context

# --- 2. BLOG PAGE ---
class BlogPage(Page):
    author = models.CharField(max_length=100)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True, help_text="A short summary of the post")
    
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,     
        blank=True,    
        on_delete=models.SET_NULL, 
        related_name='+'
    )

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title", icon="title")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('quote', blocks.BlockQuoteBlock(icon="openquote")),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('main_image'), 
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

# --- 3. CLUB PAGE ---
class ClubPage(Page):
    template = "home/club_page.html"
    president_name = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    club_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True,
        on_delete=models.SET_NULL, 
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('president_name'),
        FieldPanel('description'),
        FieldPanel('club_image'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['club_posts'] = BlogPage.objects.live().descendant_of(self)
        return context

# --- 4. SNIPPETS (Managed via Admin) ---
@register_snippet
class Event(models.Model):
    title = models.CharField(max_length=255)
    date_info = models.CharField(max_length=100, help_text="e.g., Every Wednesday  or Every Friday")
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, help_text="Optional link to a page or registration form")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_info'),
        FieldPanel('description'),
        FieldPanel('link'),
    ]

    def __str__(self):
        return self.title