from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class AlterModelViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    """
    A viewset that provides default `create()`, `update()`,
    `partial_update()`, and `destroy()` actions.
    """
    pass


