from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class UserControlPanelView(TemplateView):
    template_name = "user/control_panel.html"

    def get_context_data(self, **kwargs):
        context = super(UserControlPanelView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        if logged_user.is_authenticated:
            context['storyboarder'] = logged_user.storyboarder
        return context
