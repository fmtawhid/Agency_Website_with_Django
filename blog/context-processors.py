from .models import blog_item_category
def menu_links(request):
    links = blog_item_category.objects.all()
    return dict(links = links)