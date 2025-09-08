from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        """
    <h1>Hello World! 🐍</h1>
    <p>This is a test of the home page.</p>
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
    """
    )


def about(request):
    return HttpResponse("This is the about page.")


def contact(request):
    return HttpResponse("This is the contact page.")


def name(request, name):
    return HttpResponse(
        f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Name Page</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 16px;
                line-height: 1.5;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
                background-image: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: #fff;
            }}
        </style>
    </head>
    <body>
        <div class="container">
    <h1>Hello {name}!</h1>
    <p>This is the name page.</p>
    <p>Request: {request.user}</p>
    </div>
    </body>
    </html>
    """
    )
