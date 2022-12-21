from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):       # Para realizar la paginacion de la API
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000