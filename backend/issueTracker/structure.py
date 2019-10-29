# urls
    urlpatterns = [
        path(
            '<a_query.property from html template|argument for view_func>/', 
            views.func,
            name = 'url_name for html template')
    ]

# views
    def view_func(request, argument_from_url_path):
        # make query
        query = models.A_model.objects.query(arg)
        return render(request, "html template", {'query for html template': query})

# html template
    <div>
        {{query.property}} # query from views
        <a href="{% url 'app:url_name from urls' a_query.property as parameter for urls %}">a link</a>
    </div>
