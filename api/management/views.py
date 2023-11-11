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
        if self.action in [
            "reset_password"
            "verify_otp",
            "regenerate_otp"
        ]:
            self.permission_classes = []
        return super(UserViewSet, self).get_permissions()

    @action(detail=True, methods=["PATCH"])
    def verify_otp(self, request, pk=None):
        try:
            instance = self.get_object()
            if instance.verify_otp(request.data.get("otp")):
                return Response({"success": "Successfully verified the user."}, status=status.HTTP_200_OK)

            return Response(
                {"message": "User active or Please enter the correct OTP."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["PATCH"])
    def regenerate_otp(self, request, pk=None):
        """ Regenerate OTP for the given user and send it to the user. """
        try:
            instance = self.get_object()
            if instance.regenerate_otp():
                return Response({"success": "Successfully generate new OTP."}, status=status.HTTP_200_OK)

            return Response({"message": "Max OTP try reached, try after an hour"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(url_path="reset-password", detail=False, methods=["PATCH"])
    def reset_password(self, request):
        try:
            instance = self.queryset.get(phone_number=request.data.get("phone_number"))
            if instance.reset_password():
                return Response({"success": "The password has been reset and sent to your phone number!"}, status=status.HTTP_200_OK)
            return Response({"message": "Error sending message"}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"message": "User with this phone number not found!"}, status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({"message": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class PanelViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
