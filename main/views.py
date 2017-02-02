from django.views.generic.base import TemplateView
from showcase.views import filter_by_author
from verification import send_validation


class HomePageView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

# region User Control Panel


class UserControlPanelHomeView(TemplateView):
    template_name = "user/control_panel_home.html"

    def get_context_data(self, **kwargs):
        context = super(UserControlPanelHomeView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        if logged_user.is_authenticated:
            context['storyboarder'] = logged_user.storyboarder
            context['storyboards'] = filter_by_author(logged_user.storyboarder)
        return context


class UserControlPanelManageStoryboardView(TemplateView):
    template_name = "user/manage_storyboard.html"

    # TODO: More DRY stuff pls
    def get_context_data(self, **kwargs):
        context = super(UserControlPanelManageStoryboardView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        if logged_user.is_authenticated:
            context['storyboarder'] = logged_user.storyboarder
            context['storyboards'] = filter_by_author(logged_user.storyboarder)
        return context

# endregion

def UserAccountSettings(request):
    # Later, add whether or not there is a user account verified, and if so, redirect to a proper edit settings
    return send_validation(request)