from collections import OrderedDict

from rest_framework import status
from rest_framework.pagination import PageNumberPagination as drf_PageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(drf_PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("msg", "success"),
                    ("code", status.HTTP_200_OK),
                    (
                        "data",
                        OrderedDict(
                            [
                                ("count", self.page.paginator.count),
                                ("page", self.page.number),
                                ("numpages", self.page.paginator.num_pages),
                                ("results", data),
                            ]
                        ),
                    ),
                ]
            )
        )
