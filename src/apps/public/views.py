from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    """
    Landing page view for DaTARA platform.
    Displays hero section, features, and call-to-action elements.
    """
    template_name = 'public/landing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'DaTARA - DataCamp Application Tracker',
            'meta_description': 'Streamline scholarship applications for DataCamp Donates program with comprehensive admin tools and analytics.',
        })
        return context


class ApplicationPageView(TemplateView):
    """
    Scholarship application page view.
    """
    template_name = 'public/application.html'


class PartnerOrganizationPageView(TemplateView):
    """
    Partner organization information page view.
    """
    template_name = 'public/partner_organization.html'


class FAQPageView(TemplateView):
    """
    Frequently Asked Questions page view.
    """
    template_name = 'public/faq.html'


# Function-based views for simpler pages
def landing_page(request):
    """
    Landing page view with statistics and features.
    """
    context = {
        'scholarship_count': '40,000+',
        'value_donated': '$15M+',
        'partner_orgs': '200+',
    }
    return render(request, 'public/landing.html', context)

