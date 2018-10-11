from datetime import datetime, timedelta

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


class UpdateTodayFilter(SimpleListFilter):
    title = _('Update date')
    parameter_name = 'updated'

    def lookups(self, request, model_admin):
        return (
            ('today', _('today')),
            ('today', _('today'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            return queryset.filter(date_updated=datetime.today().date())


class CreateDateFilter(SimpleListFilter):
    title = _('Creation date')
    parameter_name = 'created'

    def lookups(self, request, model_admin):
        return (
            ('today', _('today')),
            ('three', _('three days ago')),
            ('week', _('week ago'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            return queryset.filter(date_updated=datetime.today().date())

        if self.value() == 'three':
            date_ago = datetime.today() - timedelta(days=3)
            return queryset.filter(date_updated__gte=date_ago.date())

        if self.value() == 'week':
            date_ago = datetime.today() - timedelta(weeks=1)
            return queryset.filter(date_updated__gte=date_ago.date())


