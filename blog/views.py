from django.shortcuts import render

posts= [
    {
      "author": "Joy Cheruto",
      "title": "Starting My Tech Journey",
      "content": "Today I officially began my journey into software engineering and AI.",
      "date_posted": "2025-01-12"
    },
    {
      "author": "Alex Kip",
      "title": "Understanding React Hooks",
      "content": "Hooks simplify state management in functional components.",
      "date_posted": "2025-02-03"
    },
    {
      "author": "Sarah Kim",
      "title": "The Power of Data Science",
      "content": "Data science is transforming industries across the world.",
      "date_posted": "2025-02-20"
    },
    {
      "author": "Michael Doe",
      "title": "Why Cybersecurity Matters",
      "content": "Security is a core part of any modern digital system.",
      "date_posted": "2025-03-01"
    },
    {
      "author": "Linda Faith",
      "title": "Exploring Backend Development",
      "content": "C# and SQL are powerful tools for creating scalable systems.",
      "date_posted": "2025-04-10"
    }
  ]



def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})