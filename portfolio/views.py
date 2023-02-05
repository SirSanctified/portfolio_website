from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic

from . import models, forms


def home(request):
    user = models.UserProfile.objects.first()
    projects = models.Project.objects.all()
    technologies = models.Technology.objects.all()
    soft_skills = models.SoftSkill.objects.all()
    context = {
        'user_profile': user,
        'projects': projects,
        'technologies': technologies,
        'soft_skills': soft_skills,
    }
    return render(request, 'portfolio/index.html', context)


class ContactView(generic.FormView):
    template_name = "portfolio/contact.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent successfully, thank you for getting in touch. I '
                                       'will get back to you as soon as possible.')
        return super().form_valid(form)


def blog_posts(request):
    blogs = models.Blog.objects.all()
    return render(request, 'portfolio/blogs.html', context={'blogs': blogs})


def blog_details(request, pk):
    blog = models.Blog.objects.get(id=pk)
    comments = models.Comment.objects.filter(blog=blog)
    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.blog = blog
            form.save()
            messages.success(request, "Your comment has been posted successfully")
            return redirect('/blogs/{}'.format(pk))
    elif request.method == 'GET':
        form = forms.CommentForm()
    return render(request, 'portfolio/blog-details.html', context={'blog': blog, 'comments': comments, 'form': form})
