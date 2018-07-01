# import logging
#
# from django.conf import settings
# from django.contrib.sites.models import Site
# from django.utils.translation import get_language
# from django_countries.fields import Country
#
# from . import analytics
# from ..discount.models import Sale
# from .utils import get_client_ip, get_country_by_ip, get_currency_for_country
#
# logger = logging.getLogger(__name__)
#
#
# def google_analytics(get_response):
#     """Report a page view to Google Analytics."""
#     def middleware(request):
#         client_id = analytics.get_client_id(request)
#         path = request.path
#         language = get_language()
#         headers = request.META
#         try:
#             analytics.report_view(
#                 client_id, path=path, language=language, headers=headers)
#         except Exception:
#             logger.exception('Unable to update analytics')
#         return get_response(request)
#     return middleware
#
#
# def discounts(get_response):
#     """Assign active discounts to `request.discounts`."""
#     def middleware(request):
#         discounts = Sale.objects.all()
#         discounts = discounts.prefetch_related('products', 'categories')
#         request.discounts = discounts
#         return get_response(request)
#
#     return middleware
#
#
# def country(get_response):
#     """Detect the user's country and assign it to `request.country`."""
#     def middleware(request):
#         client_ip = get_client_ip(request)
#         if client_ip:
#             request.country = get_country_by_ip(client_ip)
#         if not request.country:
#             request.country = Country(settings.DEFAULT_COUNTRY)
#         return get_response(request)
#
#     return middleware
#
#
# def currency(get_response):
#     """Take a country and assign a matching currency to `request.currency`."""
#     def middleware(request):
#         if hasattr(request, 'country') and request.country is not None:
#             request.currency = get_currency_for_country(request.country)
#         else:
#             request.currency = settings.DEFAULT_CURRENCY
#         return get_response(request)
#
#     return middleware
#
#
# def site(get_response):
#     """Clear the Sites cache and assign the current site to `request.site`.
#
#     By default django.contrib.sites caches Site instances at the module
#     level. This leads to problems when updating Site instances, as it's
#     required to restart all application servers in order to invalidate
#     the cache. Using this middleware solves this problem.
#     """
#     def middleware(request):
#         Site.objects.clear_cache()
#         request.site = Site.objects.get_current()
#         return get_response(request)
#
#     return middleware



# coding=utf-8
import jwt
import traceback

from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser, User
from django.conf import LazySettings
from django.contrib.auth.middleware import get_user

settings = LazySettings()


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))

    @staticmethod
    def get_jwt_user(request):

        user_jwt = get_user(request)
        # user_jwt.username = user_jwt.nickname
        print(type(user_jwt))
        # user_jwt['fffff']='ff'
        if user_jwt.is_authenticated():
            return user_jwt
        token = request.META.get('HTTP_AUTHORIZATION', None)
        user_jwt = AnonymousUser()
        if token is not None:
            try:
                user_jwt = jwt.decode(
                    token,
                    settings.WP_JWT_TOKEN,
                )
                user_jwt = User.objects.get(
                    id=user_jwt['data']['user']['id']
                )
            except Exception as e: # NoQA
                traceback.print_exc()
        return user_jwt
