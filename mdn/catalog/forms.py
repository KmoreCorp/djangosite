import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(\
        help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_data(self):
        data = self.cleaned_data['renewal_date']

        #日期至少是当前，不能更早
        if data < datetime.date.today():
            raise ValidationError(_('日期无效  续借日期早于今天'))

        # 日期是否被允许，即不超过今天起四周
        if data > datetime.date.today()+datetime.timedelta(weeks=4):
            raise ValidationError(_('日期无效  续借时长超过四周'))

        return data