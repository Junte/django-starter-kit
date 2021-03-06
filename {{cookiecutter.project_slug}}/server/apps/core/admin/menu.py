from admin_tools.menu import Menu, items, reverse


class AdminMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.children += [
            items.MenuItem('Home', reverse('admin:index')),
            items.AppList(title='Applications'),
            {%- if cookiecutter.use_celery == "y" %}
            items.MenuItem('Management', children=[
                items.MenuItem('Job queue', '/admin/flower/'),
            ])
            {%- endif %}
        ]
