from django.db import models


# Create your models here.
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    shift = models.CharField(
        max_length=20,
        choices=[
            ("morning", "Morning"),
            ("afternoon", "Afternoon"),
            ("evening", "Evening"),
        ],
    )
    time_log = models.DateTimeField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


# Example models for Dynamic Template demonstrations
class Category(models.Model):
    """Example model to demonstrate template relationships and loops"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """Example model to demonstrate template features with related objects"""

    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def get_status_display_class(self):
        """Example method for templates to demonstrate method calls"""
        status_classes = {
            "draft": "text-warning",
            "published": "text-success",
            "archived": "text-muted",
        }
        return status_classes.get(self.status, "text-secondary")


class Tag(models.Model):
    """Example model for many-to-many relationships in templates"""

    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(
        max_length=7, default="#007bff", help_text="Hex color code"
    )

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """Example model showing various field types and relationships for template demos"""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    author = models.CharField(max_length=100, default="Admin")

    # Relationships
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)

    # Status and visibility
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    # Metrics
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_reading_time(self):
        """Example method - calculate reading time based on word count"""
        word_count = len(self.content.split())
        reading_time = max(1, word_count // 200)  # Assume 200 words per minute
        return reading_time
