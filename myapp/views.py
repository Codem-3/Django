from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

# Create your views here.


def handler404(request, exception):
    return HttpResponseNotFound(
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page Not Found - 404</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow: hidden;
            }
            
            body::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(255, 107, 107, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
                pointer-events: none;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                border-radius: 20px;
                padding: 3rem;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
                width: 90%;
                position: relative;
                z-index: 1;
                animation: slideUp 0.8s ease-out;
            }
            
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .error-code {
                font-size: 8rem;
                font-weight: bold;
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                line-height: 1;
                margin-bottom: 1rem;
                animation: bounce 2s infinite;
            }
            
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% {
                    transform: translateY(0);
                }
                40% {
                    transform: translateY(-10px);
                }
                60% {
                    transform: translateY(-5px);
                }
            }
            
            h1 {
                color: #333;
                font-size: 2rem;
                margin-bottom: 1rem;
            }
            
            p {
                color: #666;
                font-size: 1.2rem;
                margin-bottom: 2rem;
                line-height: 1.6;
            }
            
            .home-btn {
                display: inline-block;
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                color: white;
                text-decoration: none;
                padding: 1rem 2.5rem;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .home-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
            }
            
            .emoji {
                font-size: 3rem;
                margin: 1rem 0;
                display: block;
                animation: wiggle 2s ease-in-out infinite;
            }
            
            @keyframes wiggle {
                0%, 7% {
                    transform: rotateZ(0);
                }
                15% {
                    transform: rotateZ(-15deg);
                }
                20% {
                    transform: rotateZ(10deg);
                }
                25% {
                    transform: rotateZ(-10deg);
                }
                30% {
                    transform: rotateZ(6deg);
                }
                35% {
                    transform: rotateZ(-4deg);
                }
                40%, 100% {
                    transform: rotateZ(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="error-code">404</div>
            <span class="emoji">🤔</span>
            <h1>Oops! Page Not Found</h1>
            <p>The page you're looking for seems to have wandered off into the digital wilderness.</p>
            <a href="/" class="home-btn">Take Me Home 🏠</a>
        </div>
    </body>
    </html>
    """
    )


def handler500(request):
    return HttpResponseServerError(
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Server Error - 500</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow: hidden;
            }
            
            body::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(231, 76, 60, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
                pointer-events: none;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                border-radius: 20px;
                padding: 3rem;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
                width: 90%;
                position: relative;
                z-index: 1;
                animation: slideUp 0.8s ease-out;
            }
            
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .error-code {
                font-size: 8rem;
                font-weight: bold;
                background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                line-height: 1;
                margin-bottom: 1rem;
                animation: shake 1s ease-in-out infinite;
            }
            
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                10%, 30%, 50%, 70%, 90% { transform: translateX(-3px); }
                20%, 40%, 60%, 80% { transform: translateX(3px); }
            }
            
            h1 {
                color: #333;
                font-size: 2rem;
                margin-bottom: 1rem;
            }
            
            p {
                color: #666;
                font-size: 1.2rem;
                margin-bottom: 2rem;
                line-height: 1.6;
            }
            
            .home-btn {
                display: inline-block;
                background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
                color: white;
                text-decoration: none;
                padding: 1rem 2.5rem;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .home-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(231, 76, 60, 0.4);
            }
            
            .emoji {
                font-size: 3rem;
                margin: 1rem 0;
                display: block;
                animation: pulse 2s ease-in-out infinite;
            }
            
            @keyframes pulse {
                0%, 100% {
                    transform: scale(1);
                }
                50% {
                    transform: scale(1.1);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="error-code">500</div>
            <span class="emoji">⚠️</span>
            <h1>Internal Server Error</h1>
            <p>Something went wrong on our end. Our team has been notified and is working to fix this issue.</p>
            <a href="/" class="home-btn">Go Back Home 🏠</a>
        </div>
    </body>
    </html>
    """
    )


@csrf_protect
def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        if name:
            return redirect("name", name=name)

    csrf_token = get_token(request)
    return HttpResponse(
        f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome Home</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow-x: hidden;
            }}
            
            body::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(120, 119, 198, 0.2) 0%, transparent 50%);
                pointer-events: none;
            }}
            
            .container {{
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(20px);
                border-radius: 20px;
                padding: 3rem;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 500px;
                width: 90%;
                position: relative;
                z-index: 1;
                animation: slideUp 0.8s ease-out;
            }}
            
            @keyframes slideUp {{
                from {{
                    opacity: 0;
                    transform: translateY(30px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            h1 {{
                color: #333;
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: fadeInDown 1s ease-out 0.2s both;
            }}
            
            @keyframes fadeInDown {{
                from {{
                    opacity: 0;
                    transform: translateY(-20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            p {{
                color: #666;
                font-size: 1.1rem;
                margin-bottom: 2rem;
                line-height: 1.6;
                animation: fadeIn 1s ease-out 0.4s both;
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            
            .nav-links {{
                margin-bottom: 2rem;
                animation: fadeIn 1s ease-out 0.6s both;
            }}
            
            .nav-links a {{
                display: inline-block;
                color: #667eea;
                text-decoration: none;
                margin: 0 1rem;
                padding: 0.5rem 1rem;
                border-radius: 25px;
                transition: all 0.3s ease;
                font-weight: 500;
            }}
            
            .nav-links a:hover {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }}
            
            form {{
                margin-top: 2rem;
                animation: fadeInUp 1s ease-out 0.8s both;
            }}
            
            @keyframes fadeInUp {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            .form-group {{
                margin-bottom: 1.5rem;
            }}
            
            input[type="text"] {{
                width: 100%;
                padding: 1rem 1.5rem;
                border: 2px solid #e1e5e9;
                border-radius: 50px;
                font-size: 1rem;
                outline: none;
                transition: all 0.3s ease;
                background: rgba(255, 255, 255, 0.9);
            }}
            
            input[type="text"]:focus {{
                border-color: #667eea;
                transform: scale(1.02);
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }}
            
            button {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 1rem 2.5rem;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }}
            
            button:hover {{
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            }}
            
            button:active {{
                transform: translateY(-1px);
            }}
            
            @media (max-width: 600px) {{
                .container {{
                    padding: 2rem;
                    margin: 1rem;
                }}
                
                h1 {{
                    font-size: 2rem;
                }}
                
                .nav-links a {{
                    display: block;
                    margin: 0.5rem 0;
                }}
            }}
            
            .decorative-element {{
                position: absolute;
                width: 100px;
                height: 100px;
                border-radius: 50%;
                background: linear-gradient(45deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
                animation: float 3s ease-in-out infinite;
            }}
            
            .decorative-element:nth-child(1) {{
                top: 10%;
                left: 10%;
                animation-delay: 0s;
            }}
            
            .decorative-element:nth-child(2) {{
                top: 20%;
                right: 10%;
                animation-delay: 1s;
            }}
            
            .decorative-element:nth-child(3) {{
                bottom: 10%;
                left: 15%;
                animation-delay: 2s;
            }}
            
            @keyframes float {{
                0%, 100% {{
                    transform: translateY(0px);
                }}
                50% {{
                    transform: translateY(-20px);
                }}
            }}
        </style>
    </head>
    <body>
        <div class="decorative-element"></div>
        <div class="decorative-element"></div>
        <div class="decorative-element"></div>
        
        <div class="container">
            <h1>Hello World! 🐍</h1>
            <p>Welcome to our Django application!</p>
            
            <div class="nav-links">
                <a href="/about/">About</a>
                <a href="/contact/">Contact</a>
            </div>

            <form action="/" method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}" />
                <div class="form-group">
                    <input type="text" name="name" placeholder="Enter your name" required>
                </div>
                <button type="submit">Get Started ✨</button>
            </form>
        </div>
    </body>
    </html>
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
