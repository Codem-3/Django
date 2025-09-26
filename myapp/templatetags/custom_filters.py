"""
Custom template tags and filters for Django Dynamic Templates Demo

This file demonstrates how to create custom template tags and filters
for use in Django templates. These examples show various patterns and
best practices for extending Django's template system.
"""

from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe
import random
import re

# Create a template library instance
register = template.Library()


# =============================================================================
# CUSTOM FILTERS
# =============================================================================


@register.filter
def multiply(value, arg):
    """
    Multiply a value by an argument.
    Usage: {{ price|multiply:1.2 }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def currency(value):
    """
    Format a number as currency.
    Usage: {{ price|currency }}
    """
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return "$0.00"


@register.filter
def truncate_chars(value, length):
    """
    Truncate a string to a specific character length.
    Usage: {{ long_text|truncate_chars:50 }}
    """
    try:
        length = int(length)
        if len(str(value)) > length:
            return str(value)[:length] + "..."
        return str(value)
    except (ValueError, TypeError):
        return str(value)


@register.filter
def percentage(value, total):
    """
    Calculate percentage of value from total.
    Usage: {{ count|percentage:total_count }}
    """
    try:
        value = float(value)
        total = float(total)
        if total == 0:
            return "0%"
        return f"{(value / total * 100):.1f}%"
    except (ValueError, TypeError, ZeroDivisionError):
        return "0%"


@register.filter
def highlight_search(text, search_term):
    """
    Highlight search terms in text.
    Usage: {{ content|highlight_search:search_query }}
    """
    if not search_term or not text:
        return text

    pattern = re.compile(re.escape(str(search_term)), re.IGNORECASE)
    highlighted = pattern.sub(
        f'<mark class="bg-warning">{search_term}</mark>', str(text)
    )
    return mark_safe(highlighted)


@register.filter
def dict_get(dictionary, key):
    """
    Get a value from a dictionary using a variable key.
    Usage: {{ my_dict|dict_get:dynamic_key }}
    """
    try:
        return dictionary.get(key, "")
    except (AttributeError, TypeError):
        return ""


@register.filter
def split_string(value, delimiter=","):
    """
    Split a string into a list.
    Usage: {{ "apple,banana,cherry"|split_string:"," }}
    """
    try:
        return str(value).split(delimiter)
    except (AttributeError, TypeError):
        return [value]


# =============================================================================
# SIMPLE TAGS
# =============================================================================


@register.simple_tag
def current_time(format_string="%Y-%m-%d %H:%M:%S"):
    """
    Return current time in specified format.
    Usage: {% current_time "%Y-%m-%d" %}
    """
    return timezone.now().strftime(format_string)


@register.simple_tag
def random_number(min_val=1, max_val=100):
    """
    Generate a random number in the specified range.
    Usage: {% random_number 1 10 %}
    """
    try:
        min_val = int(min_val)
        max_val = int(max_val)
        return random.randint(min_val, max_val)
    except (ValueError, TypeError):
        return random.randint(1, 100)


@register.simple_tag
def multiply_values(val1, val2):
    """
    Multiply two values together.
    Usage: {% multiply_values 5 3 %}
    """
    try:
        return float(val1) * float(val2)
    except (ValueError, TypeError):
        return 0


@register.simple_tag
def range_list(start, end, step=1):
    """
    Generate a range of numbers.
    Usage: {% range_list 1 10 2 %}
    """
    try:
        start = int(start)
        end = int(end)
        step = int(step)
        return list(range(start, end, step))
    except (ValueError, TypeError):
        return []


@register.simple_tag
def get_verbose_name(instance, field_name):
    """
    Get the verbose name of a model field.
    Usage: {% get_verbose_name object "field_name" %}
    """
    try:
        return instance._meta.get_field(field_name).verbose_name
    except (AttributeError, Exception):
        return field_name.replace("_", " ").title()


# =============================================================================
# INCLUSION TAGS
# =============================================================================


@register.inclusion_tag("_alert.html")
def render_alert(message, alert_type="info", dismissible=True):
    """
    Render a Bootstrap alert component.
    Usage: {% render_alert "Success message" "success" True %}
    """
    alert_classes = {
        "info": "alert-info",
        "success": "alert-success",
        "warning": "alert-warning",
        "danger": "alert-danger",
        "primary": "alert-primary",
        "secondary": "alert-secondary",
    }

    return {
        "message": message,
        "alert_class": alert_classes.get(alert_type, "alert-info"),
        "dismissible": dismissible,
        "icon_map": {
            "info": "fa-info-circle",
            "success": "fa-check-circle",
            "warning": "fa-exclamation-triangle",
            "danger": "fa-times-circle",
        },
    }


@register.inclusion_tag("_progress_bar.html")
def progress_bar(current, total, show_percentage=True, color="primary"):
    """
    Render a progress bar.
    Usage: {% progress_bar 75 100 True "success" %}
    """
    try:
        current = float(current)
        total = float(total)
        percentage = (current / total * 100) if total > 0 else 0
    except (ValueError, TypeError, ZeroDivisionError):
        percentage = 0

    return {
        "current": current,
        "total": total,
        "percentage": round(percentage, 1),
        "show_percentage": show_percentage,
        "color": color,
    }


# =============================================================================
# ASSIGNMENT TAGS (using simple_tag with assignment)
# =============================================================================


@register.simple_tag
def calculate_reading_time(content):
    """
    Calculate estimated reading time for content.
    Usage: {% calculate_reading_time article.content as reading_time %}
    """
    words_per_minute = 200
    word_count = len(str(content).split())
    minutes = max(1, round(word_count / words_per_minute))
    return f"{minutes} min read"


@register.simple_tag
def get_social_links():
    """
    Return a dictionary of social media links.
    Usage: {% get_social_links as social %}
    """
    return {
        "twitter": "https://twitter.com/example",
        "facebook": "https://facebook.com/example",
        "linkedin": "https://linkedin.com/in/example",
        "github": "https://github.com/example",
    }


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================


def _safe_int(value, default=0):
    """Convert value to integer safely."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def _safe_float(value, default=0.0):
    """Convert value to float safely."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default
