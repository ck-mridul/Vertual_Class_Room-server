from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('name', 'email', 'image', 'is_verifyed', 'password')
        
    def create(self, validated_data):
        user = User.objects.create(
            name = validated_data['name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        instance.save()
        return instance