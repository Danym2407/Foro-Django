from django.shortcuts import render

posts = [

    {
        'author': 'Daniela Mendez',
        'title': 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted': 'October 30, 2024',

    },
        {
        'author': 'Iris Jasso',
        'title': 'Blog Post 2',
        'content' : 'First Post content',
        'date_posted': 'October 31, 2024',

    }
]

def home (request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html', {'title': 'About'})




