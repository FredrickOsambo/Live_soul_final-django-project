from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Doctorinfo, User, HealthFact
from django.contrib import messages
from django. shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, UserProfile, Doctorinfo
from .forms import ArticleForm
from .forms import SignUpForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    return render(request, 'core/profile.html', {'profile': profile})


def logout_view(request):
    logout(request)
    return redirect('home')

def doctor_list(request):
    doctors = Doctorinfo.objects.all()
    return render(request, 'core/doctor_list.html', {'doctors': doctors})


def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'core/login_signup.html', {'page': page})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {'page': page}
    return render(request, 'core/login_signup.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'core/login_signup.html', {'form': form})



def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'core/home.html',  {'articles': articles})

# Existing view functions...
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'core/create_article.html', {'form': form})

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'core/article_list.html', {'articles': articles})

def article_detail(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'core/article_list.html', {'article': article})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctorinfo, pk=pk)
    return render(request, 'core/doctor_detail.html', {'doctor': doctor})

                                           

def health_facts(request):
    health_facts = HealthFact.objects.all()
    context = {
        'health_facts': health_facts,
    }
    return render(request, 'core/health_facts.html', context)


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'core/submit_feedback.html', {'form': form})

@login_required
def view_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'core/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    user = request.user
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'core/edit_profile.html', {'form': form})