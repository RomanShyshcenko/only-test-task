from rest_framework.generics import ListAPIView, CreateAPIView
from only_fans_stat.models import Links, AccountDetail
from only_fans_stat.serializers import LinksSerializer, AccountDetailSerializer


class ListAccountDetailView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class ListLinksView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class CreateLinksView(CreateAPIView):
    serializer_class = AccountDetailSerializer
