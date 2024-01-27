from rest_framework import status
from rest_framework.response import Response


class Results(object):
    def __init__(self, page=1, nums=1, count=1):
        self.page = page
        self.nums = nums
        self.count = count

    @classmethod
    def error_info(cls, msg, status):
        _info = {"msg": msg, "code": status}
        return Response(data=_info, status=status)

    def succss_result(self, data=None):
        if data is None:
            data = []
        elif not isinstance(data, list):
            data = [data]
        _info = {
            "msg": "success",
            "code": status.HTTP_200_OK,
            "data": {
                "page": self.page,
                "numpages": self.nums,
                "count": self.count,
                "results": data,
            },
        }
        return Response(data=_info)


class CreateResponseMixin(Results):
    def post(self, request, *args, **kwargs):
        res = super().post(request, *args, **kwargs)
        if str(res.status_code).startswith("2"):
            return self.succss_result(res.data)
        else:
            return self.error_info(res.data, res.status_code)


class RetrieveResponseMixin(Results):
    def retrieve(self, request, *args, **kwargs):
        res = super().retrieve(request, *args, **kwargs)
        if str(res.status_code).startswith("2"):
            return self.succss_result(res.data)
        else:
            return self.error_info(res.data, res.status_code)


class DeleteResponseMixin(Results):
    def delete(self, request, *args, **kwargs):
        res = super().delete(request, *args, **kwargs)
        if str(res.status_code).startswith("2"):
            return self.succss_result(res.data)
        else:
            return self.error_info(res.data, res.status_code)


class UpdateResponseMixin(Results):
    def update(self, request, *args, **kwargs):
        res = super().update(request, *args, **kwargs)
        if str(res.status_code).startswith("2"):
            return self.succss_result(res.data)
        else:
            return self.error_info(res.data, res.status_code)


class RetrieveUpdateDeleteResponseMixin(
    RetrieveResponseMixin,
    UpdateResponseMixin,
    DeleteResponseMixin,
):
    pass
