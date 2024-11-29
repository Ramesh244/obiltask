# import time
# from django.core.cache import caches
# from django.http import JsonResponse

# class RedisRateLimitMiddleware:
#     """
#     Middleware to enforce rate limiting using Redis as the backend.
#     """
#     RATE_LIMIT = 5  # Maximum requests allowed
#     TIME_WINDOW = 60  # Time window in seconds (e.g., 60 seconds)

#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.cache = caches['default']  # Use the default Redis cache

#     def __call__(self, request):
#         client_ip = self.get_client_ip(request)
#         cache_key = f"rate_limit:{client_ip}"

#         # Use Redis to track request counts
#         request_count = self.cache.get(cache_key, 0)

#         if request_count >= self.RATE_LIMIT:
#             return JsonResponse(
#                 {"error": "Rate limit exceeded. Try again later."},
#                 status=429,
#             )

#         # Increment the request count with an expiry time equal to TIME_WINDOW
#         pipe = self.cache.client.get_client().pipeline()
#         pipe.incr(cache_key)
#         pipe.expire(cache_key, self.TIME_WINDOW)
#         pipe.execute()

#         # Proceed to the view
#         response = self.get_response(request)
#         return response

#     @staticmethod
#     def get_client_ip(request):
#         """
#         Extract the client IP address from the request headers.
#         """
#         x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
#         if x_forwarded_for:
#             return x_forwarded_for.split(",")[0]
#         return request.META.get("REMOTE_ADDR")
