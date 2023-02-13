from .models import Product, ProductImage
from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.FileField(
            max_length=20, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )
    seller = serializers.ReadOnlyField(source="seller.name")

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "seller",
            "images",
            "uploaded_images",
        ]
        extra_kwargs = {"user": {"read_only": True}}

    def validate(self, attrs):
        attrs["seller"] = self.context.get("request").user
        return attrs

    def create(self, validated_data):
        uploaded_data = validated_data.pop("uploaded_images")
        new_product = Product.objects.create(**validated_data)
        for item in uploaded_data:
            ProductImage.objects.create(product=new_product, images=item)
        return new_product
