from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def pagination(page, page_size, result_list):  
    try:
        page = int(page)
    except ValueError:
        page = 1
    try:
        page_size = int(page_size)
        if page_size not in [4 ,8, 16, 24, 32, 40]:
            page_size = 8
    except ValueError:
        page_size = 4
    paginator = Paginator(result_list, page_size)
    try:
        result_list_page = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        result_list_page = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        result_list_page = paginator.page(page)  
    # if page == 1:
    #     result_list_page = result_list(page_size)
    return page, page_size, paginator, result_list_page
