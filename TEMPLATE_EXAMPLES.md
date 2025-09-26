# Django Dynamic Templates - Practical Examples

This file contains practical examples and common use cases for Django dynamic templates, building upon the concepts covered in the main guide.

## Table of Contents

1. [Real-World Template Scenarios](#real-world-template-scenarios)
2. [E-commerce Template Examples](#e-commerce-template-examples)
3. [Blog Template Examples](#blog-template-examples)
4. [Dashboard Template Examples](#dashboard-template-examples)
5. [Form Template Examples](#form-template-examples)
6. [API Response Templates](#api-response-templates)
7. [Email Template Examples](#email-template-examples)
8. [Performance Optimization Examples](#performance-optimization-examples)

## Real-World Template Scenarios

### 1. Product Listing with Filtering

```html
<!-- products/product_list.html -->
{% extends 'base.html' %}
{% load custom_filters %}

{% block content %}
<div class="container">
    <div class="row">
        <!-- Filters Sidebar -->
        <div class="col-md-3">
            <div class="card">
                <div class="card-header">
                    <h5>Filters</h5>
                </div>
                <div class="card-body">
                    <!-- Category Filter -->
                    <h6>Categories</h6>
                    {% for category in categories %}
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" 
                                   value="{{ category.id }}" id="cat{{ category.id }}"
                                   {% if category.id|stringformat:"s" in selected_categories %}checked{% endif %}>
                            <label class="form-check-label" for="cat{{ category.id }}">
                                {{ category.name }} ({{ category.products.count }})
                            </label>
                        </div>
                    {% endfor %}
                    
                    <!-- Price Range Filter -->
                    <h6 class="mt-3">Price Range</h6>
                    <div class="mb-3">
                        <input type="range" class="form-range" id="priceRange" 
                               min="{{ min_price }}" max="{{ max_price }}" 
                               value="{{ current_price_filter|default:max_price }}">
                        <div class="d-flex justify-content-between">
                            <small>${{ min_price|floatformat:0 }}</small>
                            <small>${{ max_price|floatformat:0 }}</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Product Grid -->
        <div class="col-md-9">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h2>Products ({{ products|length }} items)</h2>
                <div class="dropdown">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button" 
                            data-bs-toggle="dropdown">
                        Sort by: {{ current_sort|default:"Name" }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="?sort=name">Name</a></li>
                        <li><a class="dropdown-item" href="?sort=price_low">Price: Low to High</a></li>
                        <li><a class="dropdown-item" href="?sort=price_high">Price: High to Low</a></li>
                        <li><a class="dropdown-item" href="?sort=rating">Rating</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="row">
                {% for product in products %}
                    <div class="col-lg-4 col-md-6 mb-4">
                        {% include '_product_card.html' with product=product show_quick_view=True %}
                    </div>
                {% empty %}
                    <div class="col-12">
                        <div class="alert alert-info text-center">
                            <h4>No products found</h4>
                            <p>Try adjusting your filters or search terms.</p>
                            <a href="{% url 'product_list' %}" class="btn btn-primary">
                                Clear Filters
                            </a>
                        </div>
                    </div>
                {% endfor %}
            </div>
            
            <!-- Pagination -->
            {% if is_paginated %}
                {% include '_pagination.html' %}
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
```

### 2. User Dashboard with Dynamic Widgets

```html
<!-- dashboard/dashboard.html -->
{% extends 'base.html' %}
{% load custom_filters %}

{% block content %}
<div class="container-fluid">
    <!-- Welcome Header -->
    <div class="row mb-4">
        <div class="col-12">
            <div class="card bg-primary text-white">
                <div class="card-body">
                    <div class="row align-items-center">
                        <div class="col">
                            <h2>Welcome back, {{ user.get_full_name|default:user.username }}!</h2>
                            <p class="mb-0">
                                Last login: {{ user.last_login|timesince }} ago
                                {% if user.last_login.date == today %}
                                    <span class="badge bg-success">Today</span>
                                {% endif %}
                            </p>
                        </div>
                        <div class="col-auto">
                            <div class="text-center">
                                <h3>{{ user.profile.points|default:0 }}</h3>
                                <small>Points</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Stats Cards -->
    <div class="row mb-4">
        {% for stat in user_stats %}
            <div class="col-xl-3 col-md-6 mb-3">
                <div class="card border-left-{{ stat.color }}">
                    <div class="card-body">
                        <div class="row align-items-center">
                            <div class="col">
                                <h6 class="text-muted mb-1">{{ stat.title }}</h6>
                                <h4 class="mb-0">
                                    {% if stat.is_currency %}
                                        {{ stat.value|currency }}
                                    {% else %}
                                        {{ stat.value|floatformat:0 }}
                                    {% endif %}
                                </h4>
                                {% if stat.change_percent %}
                                    <small class="text-{% if stat.change_percent > 0 %}success{% else %}danger{% endif %}">
                                        {{ stat.change_percent|floatformat:1 }}% 
                                        {% if stat.change_percent > 0 %}↑{% else %}↓{% endif %}
                                    </small>
                                {% endif %}
                            </div>
                            <div class="col-auto">
                                <i class="fas {{ stat.icon }} fa-2x text-{{ stat.color }}"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
    
    <!-- Dynamic Content Rows -->
    <div class="row">
        <!-- Recent Activity -->
        <div class="col-lg-8 mb-4">
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="mb-0">Recent Activity</h5>
                    <a href="{% url 'activity_log' %}" class="btn btn-sm btn-outline-primary">
                        View All
                    </a>
                </div>
                <div class="card-body p-0">
                    {% for activity in recent_activities %}
                        <div class="d-flex align-items-center p-3 border-bottom">
                            <div class="avatar me-3">
                                <div class="rounded-circle bg-{{ activity.type_color }} d-flex align-items-center justify-content-center" 
                                     style="width: 40px; height: 40px;">
                                    <i class="fas {{ activity.icon }} text-white"></i>
                                </div>
                            </div>
                            <div class="flex-grow-1">
                                <p class="mb-1">{{ activity.description }}</p>
                                <small class="text-muted">
                                    {{ activity.created_at|timesince }} ago
                                </small>
                            </div>
                            {% if activity.value %}
                                <div class="text-end">
                                    <strong class="text-{{ activity.value_color|default:'primary' }}">
                                        {{ activity.value }}
                                    </strong>
                                </div>
                            {% endif %}
                        </div>
                    {% empty %}
                        <div class="p-4 text-center text-muted">
                            <i class="fas fa-history fa-3x mb-3"></i>
                            <p>No recent activity to show.</p>
                        </div>
                    {% endfor %}
                </div>
            </div>
        </div>
        
        <!-- Quick Actions & Notifications -->
        <div class="col-lg-4">
            <!-- Quick Actions -->
            <div class="card mb-4">
                <div class="card-header">
                    <h5 class="mb-0">Quick Actions</h5>
                </div>
                <div class="card-body">
                    <div class="d-grid gap-2">
                        {% for action in quick_actions %}
                            {% if action.visible %}
                                <a href="{{ action.url }}" 
                                   class="btn btn-outline-{{ action.color|default:'primary' }}">
                                    <i class="fas {{ action.icon }} me-2"></i>
                                    {{ action.label }}
                                </a>
                            {% endif %}
                        {% endfor %}
                    </div>
                </div>
            </div>
            
            <!-- Notifications -->
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="mb-0">Notifications</h5>
                    {% if unread_notifications_count > 0 %}
                        <span class="badge bg-danger">{{ unread_notifications_count }}</span>
                    {% endif %}
                </div>
                <div class="card-body p-0">
                    {% for notification in notifications %}
                        <div class="d-flex align-items-start p-3 border-bottom {% if not notification.is_read %}bg-light{% endif %}">
                            <i class="fas {{ notification.icon }} text-{{ notification.type }} me-3 mt-1"></i>
                            <div class="flex-grow-1">
                                <p class="mb-1 {% if not notification.is_read %}fw-bold{% endif %}">
                                    {{ notification.title }}
                                </p>
                                <small class="text-muted">
                                    {{ notification.created_at|timesince }} ago
                                </small>
                            </div>
                            {% if not notification.is_read %}
                                <span class="badge bg-primary rounded-pill">New</span>
                            {% endif %}
                        </div>
                    {% empty %}
                        <div class="p-4 text-center text-muted">
                            <i class="fas fa-bell-slash fa-3x mb-3"></i>
                            <p>No notifications.</p>
                        </div>
                    {% endfor %}
                </div>
                {% if notifications %}
                    <div class="card-footer text-center">
                        <a href="{% url 'notifications' %}" class="btn btn-sm btn-outline-primary">
                            View All Notifications
                        </a>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
{{ block.super }}
<script>
    // Auto-refresh dashboard data every 5 minutes
    setInterval(() => {
        fetch('{% url "dashboard_refresh" %}')
            .then(response => response.json())
            .then(data => {
                // Update dynamic content
                if (data.notifications_count) {
                    document.querySelector('.badge.bg-danger').textContent = data.notifications_count;
                }
            });
    }, 300000);
</script>
{% endblock %}
```

## E-commerce Template Examples

### 3. Advanced Product Detail Page

```html
<!-- products/product_detail.html -->
{% extends 'base.html' %}
{% load custom_filters %}

{% block title %}{{ product.name }} - {{ block.super }}{% endblock %}

{% block content %}
<div class="container">
    <!-- Breadcrumb -->
    <nav aria-label="breadcrumb" class="mb-4">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
            <li class="breadcrumb-item"><a href="{% url 'product_list' %}">Products</a></li>
            <li class="breadcrumb-item"><a href="{% url 'category_detail' product.category.slug %}">{{ product.category.name }}</a></li>
            <li class="breadcrumb-item active">{{ product.name }}</li>
        </ol>
    </nav>
    
    <div class="row">
        <!-- Product Images -->
        <div class="col-lg-6 mb-4">
            <div class="product-images">
                <!-- Main Image -->
                <div class="main-image mb-3">
                    <img src="{{ product.main_image.url|default:'/static/img/no-image.jpg' }}" 
                         alt="{{ product.name }}" 
                         class="img-fluid rounded shadow"
                         id="mainProductImage">
                </div>
                
                <!-- Image Thumbnails -->
                {% if product.images.count > 1 %}
                    <div class="row">
                        {% for image in product.images.all %}
                            <div class="col-3 mb-2">
                                <img src="{{ image.thumbnail.url }}" 
                                     alt="{{ product.name }}"
                                     class="img-fluid rounded cursor-pointer thumbnail-img {% if forloop.first %}active{% endif %}"
                                     onclick="changeMainImage('{{ image.url }}')">
                            </div>
                        {% endfor %}
                    </div>
                {% endif %}
            </div>
        </div>
        
        <!-- Product Information -->
        <div class="col-lg-6">
            <div class="product-info">
                <!-- Product Title & Rating -->
                <div class="mb-3">
                    <h1 class="h2">{{ product.name }}</h1>
                    <div class="d-flex align-items-center mb-2">
                        <!-- Star Rating -->
                        <div class="star-rating me-2">
                            {% for i in "12345"|make_list %}
                                <i class="fas fa-star {% if i|add:0 <= product.average_rating %}text-warning{% else %}text-muted{% endif %}"></i>
                            {% endfor %}
                        </div>
                        <span class="text-muted">
                            ({{ product.reviews.count }} review{{ product.reviews.count|pluralize }})
                        </span>
                    </div>
                </div>
                
                <!-- Price -->
                <div class="price-section mb-4">
                    {% if product.on_sale %}
                        <div class="d-flex align-items-center">
                            <h3 class="text-danger me-3 mb-0">
                                {{ product.sale_price|currency }}
                            </h3>
                            <span class="text-muted text-decoration-line-through h5">
                                {{ product.regular_price|currency }}
                            </span>
                            <span class="badge bg-danger ms-2">
                                {{ product.discount_percentage }}% OFF
                            </span>
                        </div>
                    {% else %}
                        <h3 class="text-primary mb-0">{{ product.price|currency }}</h3>
                    {% endif %}
                </div>
                
                <!-- Stock Status -->
                <div class="stock-status mb-3">
                    {% if product.in_stock %}
                        {% if product.stock_quantity <= 10 %}
                            <span class="badge bg-warning">
                                <i class="fas fa-exclamation-triangle"></i>
                                Only {{ product.stock_quantity }} left!
                            </span>
                        {% else %}
                            <span class="badge bg-success">
                                <i class="fas fa-check"></i>
                                In Stock
                            </span>
                        {% endif %}
                    {% else %}
                        <span class="badge bg-danger">
                            <i class="fas fa-times"></i>
                            Out of Stock
                        </span>
                    {% endif %}
                </div>
                
                <!-- Product Description -->
                <div class="description mb-4">
                    <h5>Description</h5>
                    <p>{{ product.description|linebreaks }}</p>
                </div>
                
                <!-- Product Attributes -->
                {% if product.attributes.all %}
                    <div class="attributes mb-4">
                        <h5>Specifications</h5>
                        <div class="table-responsive">
                            <table class="table table-sm">
                                {% for attr in product.attributes.all %}
                                    <tr>
                                        <td class="fw-bold">{{ attr.name }}:</td>
                                        <td>{{ attr.value }}</td>
                                    </tr>
                                {% endfor %}
                            </table>
                        </div>
                    </div>
                {% endif %}
                
                <!-- Add to Cart Form -->
                {% if product.in_stock %}
                    <form method="post" action="{% url 'add_to_cart' %}" class="add-to-cart-form">
                        {% csrf_token %}
                        <input type="hidden" name="product_id" value="{{ product.id }}">
                        
                        <!-- Quantity Selector -->
                        <div class="row mb-3">
                            <div class="col-md-4">
                                <label for="quantity" class="form-label">Quantity:</label>
                                <div class="input-group">
                                    <button type="button" class="btn btn-outline-secondary" onclick="decreaseQuantity()">-</button>
                                    <input type="number" class="form-control text-center" 
                                           id="quantity" name="quantity" value="1" min="1" 
                                           max="{{ product.stock_quantity }}">
                                    <button type="button" class="btn btn-outline-secondary" onclick="increaseQuantity()">+</button>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Action Buttons -->
                        <div class="d-grid gap-2 d-md-flex">
                            <button type="submit" class="btn btn-primary btn-lg me-md-2">
                                <i class="fas fa-shopping-cart"></i>
                                Add to Cart
                            </button>
                            <button type="button" class="btn btn-outline-secondary btn-lg" 
                                    onclick="addToWishlist({{ product.id }})">
                                <i class="far fa-heart"></i>
                                Wishlist
                            </button>
                        </div>
                    </form>
                {% else %}
                    <div class="alert alert-warning">
                        <i class="fas fa-exclamation-triangle"></i>
                        This product is currently out of stock. 
                        <a href="#" onclick="notifyWhenAvailable({{ product.id }})">
                            Notify me when available
                        </a>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
    
    <!-- Product Tabs -->
    <div class="row mt-5">
        <div class="col-12">
            <ul class="nav nav-tabs" id="productTabs" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="description-tab" data-bs-toggle="tab" 
                            data-bs-target="#description" type="button">
                        Description
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="reviews-tab" data-bs-toggle="tab" 
                            data-bs-target="#reviews" type="button">
                        Reviews ({{ product.reviews.count }})
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="shipping-tab" data-bs-toggle="tab" 
                            data-bs-target="#shipping" type="button">
                        Shipping Info
                    </button>
                </li>
            </ul>
            
            <div class="tab-content mt-3" id="productTabContent">
                <!-- Description Tab -->
                <div class="tab-pane fade show active" id="description">
                    <div class="p-3">
                        <h5>Product Details</h5>
                        {{ product.long_description|default:product.description|linebreaks }}
                        
                        {% if product.features.all %}
                            <h6 class="mt-4">Key Features</h6>
                            <ul>
                                {% for feature in product.features.all %}
                                    <li>{{ feature.description }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                </div>
                
                <!-- Reviews Tab -->
                <div class="tab-pane fade" id="reviews">
                    <div class="p-3">
                        {% include '_product_reviews.html' with reviews=product.reviews.all %}
                    </div>
                </div>
                
                <!-- Shipping Tab -->
                <div class="tab-pane fade" id="shipping">
                    <div class="p-3">
                        {% include '_shipping_info.html' with product=product %}
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Related Products -->
    {% if related_products %}
        <div class="row mt-5">
            <div class="col-12">
                <h4 class="mb-4">You May Also Like</h4>
                <div class="row">
                    {% for related_product in related_products|slice:":4" %}
                        <div class="col-lg-3 col-md-6 mb-4">
                            {% include '_product_card.html' with product=related_product %}
                        </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    {% endif %}
</div>
{% endblock %}

{% block extra_js %}
{{ block.super }}
<script>
    function changeMainImage(imageUrl) {
        document.getElementById('mainProductImage').src = imageUrl;
        // Update active thumbnail
        document.querySelectorAll('.thumbnail-img').forEach(img => img.classList.remove('active'));
        event.target.classList.add('active');
    }
    
    function increaseQuantity() {
        const input = document.getElementById('quantity');
        const max = parseInt(input.getAttribute('max'));
        if (parseInt(input.value) < max) {
            input.value = parseInt(input.value) + 1;
        }
    }
    
    function decreaseQuantity() {
        const input = document.getElementById('quantity');
        if (parseInt(input.value) > 1) {
            input.value = parseInt(input.value) - 1;
        }
    }
</script>
{% endblock %}
```

## Performance Optimization Examples

### 4. Template Fragment Caching

```html
<!-- blog/post_list.html -->
{% extends 'base.html' %}
{% load cache custom_filters %}

{% block content %}
<div class="container">
    <!-- Cache the entire post list for 15 minutes -->
    {% cache 900 post_list request.GET.urlencode %}
        <div class="row">
            <div class="col-lg-8">
                <h2 class="mb-4">Latest Blog Posts</h2>
                
                {% for post in posts %}
                    <!-- Cache individual post cards for 1 hour -->
                    {% cache 3600 post_card post.id post.updated_at %}
                        <article class="card mb-4">
                            <div class="card-body">
                                <div class="row align-items-center">
                                    <div class="col-md-8">
                                        <h3 class="card-title">
                                            <a href="{% url 'post_detail' post.slug %}">
                                                {{ post.title }}
                                            </a>
                                        </h3>
                                        <p class="card-text">{{ post.excerpt|default:post.content|truncatewords:30 }}</p>
                                        
                                        <div class="post-meta text-muted small">
                                            <span class="me-3">
                                                <i class="fas fa-user"></i>
                                                {{ post.author.get_full_name|default:post.author.username }}
                                            </span>
                                            <span class="me-3">
                                                <i class="fas fa-calendar"></i>
                                                {{ post.published_at|date:"M d, Y" }}
                                            </span>
                                            <span class="me-3">
                                                <i class="fas fa-clock"></i>
                                                {{ post.get_reading_time }} read
                                            </span>
                                            <span>
                                                <i class="fas fa-eye"></i>
                                                {{ post.view_count }} views
                                            </span>
                                        </div>
                                    </div>
                                    {% if post.featured_image %}
                                        <div class="col-md-4">
                                            <img src="{{ post.featured_image.url }}" 
                                                 alt="{{ post.title }}"
                                                 class="img-fluid rounded">
                                        </div>
                                    {% endif %}
                                </div>
                            </div>
                            
                            {% if post.tags.count > 0 %}
                                <div class="card-footer bg-transparent">
                                    {% for tag in post.tags.all %}
                                        <span class="badge bg-secondary me-1">{{ tag.name }}</span>
                                    {% endfor %}
                                </div>
                            {% endif %}
                        </article>
                    {% endcache %}
                {% empty %}
                    <div class="alert alert-info">
                        <h4>No posts yet</h4>
                        <p>Check back soon for new content!</p>
                    </div>
                {% endfor %}
                
                <!-- Pagination (don't cache this as it's dynamic) -->
                {% if is_paginated %}
                    {% include '_pagination.html' %}
                {% endif %}
            </div>
            
            <!-- Sidebar -->
            <div class="col-lg-4">
                <!-- Cache sidebar for 30 minutes -->
                {% cache 1800 blog_sidebar %}
                    {% include '_blog_sidebar.html' %}
                {% endcache %}
            </div>
        </div>
    {% endcache %}
</div>
{% endblock %}
```

This comprehensive examples file shows practical, real-world usage of Django dynamic templates in various scenarios. The examples demonstrate advanced patterns, performance optimizations, and complex UI interactions that you might encounter in production applications.

## Running the Examples

To see these examples in action:

1. **Set up the models**: Run the migrations for the example models
2. **Create sample data**: Use Django admin or fixtures to create test data
3. **Configure URLs**: Add the example URL patterns to your project
4. **Test the templates**: Navigate to the demo pages to see the dynamic templates in action

## Next Steps

- Experiment with the custom template tags and filters
- Modify the examples to fit your specific use cases
- Add more complex business logic to the views
- Implement caching strategies for better performance
- Add JavaScript interactions for enhanced user experience
