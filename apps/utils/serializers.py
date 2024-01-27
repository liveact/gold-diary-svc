class SetUserSerializerMixin:
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user_id"] = request.user.id
        return super().create(validated_data)
