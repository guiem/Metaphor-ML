from functools import wraps

from django.conf import settings
from django.contrib import messages

import requests

def check_recaptcha(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:
                request.recaptcha_is_valid = True
                messages.success(request, 'Success. Thanks for voting. You can vote as many times as you want my dear '
                                          'troll! 🙈', extra_tags='alert alert-success')
            else:
                request.recaptcha_is_valid = False
                messages.error(request, 'Invalid reCAPTCHA. Please check the reCAPTCHA at the end of this site and '
                                        'verify you are human! 🤖', extra_tags='alert alert-danger')
        return view_func(request, *args, **kwargs)
    return _wrapped_view