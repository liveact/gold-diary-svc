from rest_framework import status
from rest_framework.views import exception_handler as drf_exception_handler

from apps.utils.response import Results


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        return Results.error_info(
            msg=response.data.get("detail"), status=response.status_code
        )
    else:
        return Results.error_info(
            msg=str(exc), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
