from rest_framework.response import Response


def success(data=None, message="ok", page=0, size=0, count=0):
    res = {"error": 0, "message": message, "data": data}
    if isinstance(data, list):
        res.update(page=page, size=size, count=count)
    return Response(res, status=200)


def error(data=None, message="error", status=400):
    if data:
        message = data
    res = {"data": data, "message": message, "error": status}
    return Response(res, status=status)


def paginated(data, request):
    page = int(request.GET.get("page", 1))
    size = int(request.GET.get("size", 10))
    start_idx = (page - 1) * size
    end_idx = start_idx + size
    count = len(data)
    paginated_data = data[start_idx:end_idx]
    return paginated_data, page, size, count
