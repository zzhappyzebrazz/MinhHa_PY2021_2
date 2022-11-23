from django.shortcuts import render
from stories.models import Category, Story
from django.utils import timezone

story_list = Story.objects.order_by("-public_day")
next_4_stories = story_list[1:5]
stories_4 = next_4_stories
now = timezone.now
# Create your views here.
def index(request):
    
    newest = (story_list[0])
    
    last_6_modified = story_list[:6]
    
    young_children = [story for story in story_list if story.category_id == 1]
    older_children = [story for story in story_list if story.category_id == 2]

    now = timezone.now
    
    return render(request, 'stories/index.html',
                  {
                      'now' : now,
                      'newest' : newest,
                      'next_4_stories' : next_4_stories,
                      'young_children' : young_children,
                      'older_children' : older_children,
                      'last_6_modified' : last_6_modified,
                      'stories_4' :stories_4,
                  }
                  )

def category(request, pk):
    name = Category.objects.get(pk=pk)
    stories = [story for story in story_list if story.category_id == pk]
    print(pk)
    print(stories)
    category_name = name.name
    newest_story = stories[:-4]

    return render(request, 'stories/category.html',
                  {
                      'now' : now,
                      'stories': stories,
                      'newest_story' : newest_story,
                      'stories_4' :stories_4,
                      'category_name' : category_name,
                  })

def story(request, id):
    content = Story.objects.get(id=id)
    print(content.name)
    return render(request, 'stories/story.html',
                  {
                    'now' : now,
                    'content' : content,
                    'stories_4' :stories_4,
                   })


def contact(request):
    return render(request, 'stories/contact.html',
                  {
                    'now' : now,
                    'stories_4' :stories_4,
                   })

