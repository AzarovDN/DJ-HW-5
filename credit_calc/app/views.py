from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get_context_data(self, **kwargs):
        context = super(CalcView, self).get_context_data(**kwargs)

        form = CalcForm(self.request.GET or None)  # instance= None
        if form.is_valid():
            initial_fee = form.clean_initial_fee()
            rate = form.clean_rate()
            months_count = form.clean_months_count()
            context['common_result'] = (initial_fee + initial_fee * rate * .01)
            context['result'] = round(context['common_result'] / months_count, 2)

        context["form"] = form

        return context