from django.views.generic import TemplateView

# === Main application entry point ===

class DashboardView(TemplateView):
    """
    The only purpose of this view is to provide a subview
    that gives a baseline for the JavaScript SPA
    """
    template_name = "dashboard.html"
