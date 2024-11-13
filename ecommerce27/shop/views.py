from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import ProductForm
from .models import Product, Category


# Create your views here.
# def shop(request):
#     return HttpResponse("Welcome to my Django Project")

# def base(request):
#     return render(request, 'base.html')

# For view Home page
def home(request):
    # Using below query fetch all products from DB and stored in a variable
    products = Product.objects.all()
    # print(products)
    category = Category.objects.all()
    # print(category)
    return render(request, 'home.html', {'products': products, 'category': category})

# For view Registration page
def signup(request):
    # Checking whether user input data into html file or not
    if request.method == "POST":
        # Getting user credentials from Registration page
        signup_fname = request.POST.get('fname')
        signup_lname = request.POST.get('lname')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        # Create Registration user with username, password and email
        # [Note: User model is default, it should pass 3 arguments in correct order]
        signup_user = User.objects.create_user(username, email, password1)

        # Fetching data from database for later pass to necessary fields
        signup_user.first_name = signup_fname
        signup_user.last_name = signup_lname

        # Save User Registration
        signup_user.save()

        # Set redirection page using URL path - name
        return redirect('signin')

    # Display Registration page if access its URL
    return render(request, 'signup.html')

# For view Login page
def signin(request):
    if request.method == "POST":
        # Getting user credentials from Login page
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        # Debug: Print username and password to console for checking
        print(f"Username: {username}, Password: {password1}")

        # Verifying user's credentials
        login_user = authenticate(username=username, password=password1)
        print(type(login_user))

        # Checking login user existence
        if login_user is not None:
            # Request for Login
            login(request, login_user)
            # Redirect to Dashboard page to get URL dashboard
            return redirect('dashboard')
        else:
            # Error message if credentials are invalid then redirect to Login page
            messages.error(request, "Invalid Credentials")
            return redirect('signin')

    # Display Login page if access its URL
    return render(request, 'signin.html')

# Dashboard view only after login using decorator
@login_required(login_url='dasboard')
# For View Dashboard page
def dashboard(request):
    # Call Login - first name, last name which saved in Registration table
    login_fname = request.user.first_name
    login_lname = request.user.last_name
    return render(request, 'dashboard.html', {'board_fname': login_fname, 'board_lname': login_lname})

# For Logout page
def signout(request):
    logout(request)
    messages.success(request, "You are successfully logout..")
    return redirect('signin')

# For Add Products
def add_product(request):
    # Checking form is submitted
    if request.method == 'POST':
        # Assign all form data into a variable
        # [POST - used to save data, FILES - used to save images]
        add_product_form = ProductForm(request.POST, request.FILES)
        # Checking form validation
        if add_product_form.is_valid():
            # Save Form and display success message
            add_product_form.save()
            messages.success(request, "Product has been added successfully")
    # Else assign all form data into a variable
    add_product_form = ProductForm()
    # Render form data into HTML file
    return render(request, 'add_products.html', {'form': add_product_form})

# For Edit Products
def edit_product(request, product_id):
    # Retrieve the selected product or return a 404 if it doesn't exist
    selected_product = get_object_or_404(Product, id=product_id)
    # Checking form is submitted
    if request.method == "POST":
        # Assign all form data into a variable
        # [POST - used to save data, FILES - used to save images, instance - used to pass selected product]
        update_product_form = ProductForm(request.POST, request.FILES, instance=selected_product)
        # Checking form validation
        if update_product_form.is_valid():
            update_product_form.save()
            messages.success(request, "Product has been updated successfully")
            return redirect('edit_product', product_id=selected_product.id)
    # Else assign existing form data into a variable
    update_product_form = ProductForm(instance=selected_product)
    # Render form data into HTML file
    return render(request, 'edit_products.html', {'form': update_product_form})

# For Delete Products
def delete_product(request, product_id):
    selected_product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
            selected_product.delete()
            messages.success(request, "Product has been deleted successfully")
            return redirect('home')
    return render(request, 'delete_products.html', {'product':selected_product})

# For Products - Add to Cart
def add_to_cart(request, product_id):
    selected_product = get_object_or_404(Product, id=product_id)
    if request.method=="POST":
        pass
    return render(request, 'add_to_cart.html')


