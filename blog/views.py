from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog, Author, Category
from .forms import PostForm, SignUpForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
	num_blog = blog.objects.all().count()
	num_authors=Author.objects.count()
	blogs = blog.objects.all()
	authors = Author.objects.all()
	
	return render(
		request,
		'index.html',
		context={'num_blog':num_blog, 'num_authors':num_authors, 'blogs':blogs, 'authors':authors,},

		)

def detail(request, blog_id):
	thisblog = get_object_or_404(blog, pk=blog_id)
	return render(request, 'details.html', {'blog':thisblog})

@login_required
def newblog(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.published = timezone.now()
			author = Author.objects.get(pk=request.user.pk)
			post.author = author

			post.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request, 'newblog.html',{'form':form})

def SignUp(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			date_of_birth = form.cleaned_data.get('date_of_birth')
			user = authenticate(username=username, password=password)
			author = Author.objects.create(user=user, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)

			login(request, user)
			return redirect('index')

	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})


@login_required
def LogOut(request):
	logout(request)
	return redirect('index')