from django.shortcuts import render, redirect
from django.db import transaction
from .models import AITool

TOOLS_DATA = [
    {'name': "Gemini", 'description': "Google's multimodal large language model for generating content, code, and images. Excellent for complex reasoning and tasks.", 'website': "https://gemini.google.com/"},
    {'name': "Midjourney", 'description': "A powerful generative AI program for creating stunning, photorealistic images from simple text prompts.", 'website': "https://www.midjourney.com/"},
    {'name': "GitHub Copilot", 'description': "An AI pair programmer that provides real-time code suggestions, completion, and entire function bodies.", 'website': "https://github.com/features/copilot"},
    {'name': "Perplexity AI", 'description': "An answer engine that uses generative AI to provide direct answers with detailed sources and citations.", 'website': "https://www.perplexity.ai/"},
]

def index(request):
    # # Populate database once (get_or_create ensures no duplicates)
    # for tool_data in TOOLS_DATA:
    #     AITool.objects.get_or_create(**tool_data)

    # Handle search query
    query = request.GET.get('q')
    if query:
        tools = AITool.objects.filter(name__icontains=query)
    else:
        tools = AITool.objects.all()
    
    context = {'tools': tools}
    return render(request, 'index.html', context)

@transaction.atomic
def add_tool(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        website = request.POST.get('website')
        if name and description and website:
            AITool.objects.create(name=name, description=description, website=website)
    return redirect('index')  # Redirect back to index after add