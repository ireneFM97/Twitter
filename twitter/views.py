from django.views import View
from django.template.response import TemplateResponse


class IndexView(View):
    def get(self, request):
        return TemplateResponse(request, 'twitter/index.html')
