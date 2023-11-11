from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "reset_password":
            self.permission_classes = []
        return super(UserViewSet, self).get_permissions()

    @action(url_path="reset-password", detail=False, methods=["PATCH"])
    def reset_password(self, request):
        try:
            instance = self.queryset.get(phone_number=request.data.get("phone_number"))
            if instance.reset_password():
                return Response({"success": "Пароль сброшен и отправлен на ваш номер телефона!"}, status=status.HTTP_200_OK)
            return Response({"message": "Ошибка отправки сообщения"}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"message": "Ползователь с данным номером телефона не найден!"}, status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({"message": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class PanelViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
