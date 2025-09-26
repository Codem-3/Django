# Dynamic Templates in Django - Complete Guide

## Table of Contents

1. [What are Dynamic Templates?](#what-are-dynamic-templates)
2. [Template Context](#template-context)
3. [Template Variables](#template-variables)
4. [Template Tags](#template-tags)
5. [Template Filters](#template-filters)
6. [Template Inheritance](#template-inheritance)
7. [Template Includes](#template-includes)
8. [Conditional Rendering](#conditional-rendering)
9. [Loops and Iteration](#loops-and-iteration)
10. [Custom Template Tags and Filters](#custom-template-tags-and-filters)
11. [Best Practices](#best-practices)

## What are Dynamic Templates?

Dynamic Templates in Django are HTML templates that can display different content based on the data passed from views. Unlike static HTML files, dynamic templates can:

- Display database content
- Show different content based on conditions
- Repeat sections for lists of data
- Include reusable template components
- Inherit from base templates for consistent layouts

## Template Context

The template context is the data passed from your Django view to the template. It's a dictionary-like object containing variables that can be accessed in the template.

### In your view

```python
def my_view(request):
    context = {
        'title': 'Dynamic Content',
        'user': request.user,
        'items': ['apple', 'banana', 'cherry'],
        'show_footer': True,
        'count': 42
    }
    return render(request, 'my_template.html', context)
```

### In your template

```html
<h1>{{ title }}</h1>
<p>Welcome, {{ user.username }}!</p>
```

## Template Variables

Template variables are enclosed in double curly braces `{{ variable }}` and are replaced with their values from the context.

### Basic Usage

- `{{ variable }}` - Displays the variable
- `{{ variable.attribute }}` - Accesses object attributes
- `{{ variable.method }}` - Calls object methods (no arguments)
- `{{ dict.key }}` - Accesses dictionary values
- `{{ list.0 }}` - Accesses list items by index

### Example

```html
<h1>{{ post.title }}</h1>
<p>By {{ post.author.username }} on {{ post.created_date }}</p>
<p>{{ post.content|truncatewords:50 }}</p>
```

## Template Tags

Template tags provide logic and control structures. They're enclosed in `{% %}`.

### Common Template Tags

#### 1. `{% if %}` - Conditional rendering

```html
{% if user.is_authenticated %}
    <p>Welcome back, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

#### 2. `{% for %}` - Loops

```html
<ul>
{% for item in items %}
    <li>{{ item.name }} - ${{ item.price }}</li>
{% empty %}
    <li>No items available</li>
{% endfor %}
</ul>
```

#### 3. `{% url %}` - URL generation

```html
<a href="{% url 'contact_detail' contact.id %}">View Contact</a>
```

#### 4. `{% csrf_token %}` - CSRF protection

```html
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

#### 5. `{% load %}` - Load template tag libraries

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
```

## Template Filters

Filters modify variable output. They use the pipe symbol `|`.

### Common Filters

- `{{ value|default:"Nothing" }}` - Default value if empty
- `{{ text|truncatewords:30 }}` - Truncate to 30 words
- `{{ date|date:"F d, Y" }}` - Format date
- `{{ text|upper }}` - Uppercase
- `{{ text|lower }}` - Lowercase
- `{{ number|floatformat:2 }}` - Format float to 2 decimal places
- `{{ list|length }}` - Get list length
- `{{ html|safe }}` - Mark as safe HTML

### Chaining Filters

```html
{{ post.content|truncatewords:30|upper }}
```

## Template Inheritance

Template inheritance allows you to build a base template with blocks that child templates can override.

### Base Template (base.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <nav>
            <!-- navigation -->
        </nav>
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        {% block footer %}
            <p>&copy; 2024 My Site</p>
        {% endblock %}
    </footer>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Child Template

```html
{% extends 'base.html' %}

{% block title %}Contact List - {{ block.super }}{% endblock %}

{% block content %}
    <h1>Contacts</h1>
    <!-- page content -->
{% endblock %}
```

## Template Includes

Include allows you to insert one template into another.

### Partial Template (_contact_card.html)

```html
<div class="contact-card">
    <h3>{{ contact.name }}</h3>
    <p>{{ contact.email }}</p>
    <p>{{ contact.phone }}</p>
</div>
```

### Main Template

```html
{% for contact in contacts %}
    {% include '_contact_card.html' with contact=contact %}
{% endfor %}
```

## Conditional Rendering

### Multiple Conditions

```html
{% if user.is_authenticated and user.is_staff %}
    <a href="{% url 'admin:index' %}">Admin Panel</a>
{% elif user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

### Using `{% ifequal %}` and `{% ifnotequal %}`

```html
{% ifequal user.role "admin" %}
    <button>Delete</button>
{% endifequal %}
```

## Loops and Iteration

### Advanced For Loop Features

```html
<ul>
{% for contact in contacts %}
    <li class="{% if forloop.first %}first{% endif %} {% if forloop.last %}last{% endif %}">
        {{ forloop.counter }}. {{ contact.name }}
        {% if not forloop.last %} | {% endif %}
    </li>
{% empty %}
    <li>No contacts found</li>
{% endfor %}
</ul>
```

### For Loop Variables

- `forloop.counter` - Current iteration (1-indexed)
- `forloop.counter0` - Current iteration (0-indexed)
- `forloop.first` - True if first iteration
- `forloop.last` - True if last iteration
- `forloop.parentloop` - Parent loop in nested loops

## Custom Template Tags and Filters

### Creating Custom Filters

```python
# In myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def currency(value):
    return f"${value:,.2f}"
```

### Using Custom Filters

```html
{% load custom_filters %}
<p>Total: {{ price|multiply:quantity|currency }}</p>
```

## Best Practices

### 1. Template Organization

- Keep templates in app-specific directories
- Use descriptive names
- Group related templates in subdirectories

### 2. Context Optimization

- Only pass necessary data to templates
- Use select_related() and prefetch_related() for database queries
- Consider using template fragments for reusable components

### 3. Security

- Always use `{% csrf_token %}` in forms
- Use `|safe` filter carefully with trusted content
- Validate and sanitize user input

### 4. Performance

- Use template caching for expensive operations
- Minimize database queries in templates
- Use template fragments for partial updates

### 5. Maintainability

- Use consistent naming conventions
- Document complex template logic
- Avoid business logic in templates
- Use template inheritance for consistent layouts

## Advanced Features

### 1. Template Context Processors

Add common variables to all templates automatically.

### 2. Template Caching

```html
{% load cache %}
{% cache 300 contact_list %}
    <!-- expensive template code -->
{% endcache %}
```

### 3. Internationalization

```html
{% load i18n %}
<h1>{% trans "Welcome" %}</h1>
```

### 4. Static Files

```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

This guide covers the fundamental concepts and advanced features of Django's dynamic template system. The accompanying example files demonstrate these concepts in practical scenarios.
