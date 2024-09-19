from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import MenuItem


def get_menu_tree(src):
    class Tree:

        def __init__(self, elem):
            self.body = elem
            self.heirs = []

        def __str__(self):
            if isinstance(self.body, MenuItem):
                return self.body.name
            elif isinstance(self.body, str):
                return self.body
            else:
                return self.body.__class__.__name__

        body = None
        heirs = list()

        def append(self, elem):
            self.heirs.append(Tree(elem))

        def recapp(self, elem):
            if isinstance(elem, QuerySet):
                for i in elem.all():
                    self.recapp(Tree(i))
            elif isinstance(elem, Tree):
                self.append(elem.body)
                for i in elem.body.children.all():
                    self.heirs[-1].recapp(Tree(i))
            else:
                raise TypeError("Must be Tree or QuerySet")

    new_tree = Tree("")
    queryset = src
    new_tree.recapp(queryset)
    return new_tree


class MenuView(View):

    def get(self, request: HttpRequest, tag="pass") -> HttpResponse:
        tree = get_menu_tree(MenuItem.objects.filter(parent=None))
        return render(request, 'menuapp/menu.html', context={'tree': tree, "parent_url": ''})
