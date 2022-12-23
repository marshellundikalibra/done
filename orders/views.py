from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.models import Order, OrderItems
from orders.serializers import OrderSerializer,OrderItemSerializer



class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

class OrderItemViewSet():
    queryset=OrderItems.objects.all()
    serializer_class=OrderItemSerializer
    permission_classes=[IsAuthenticated, ]