from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property
        fields = ['id', 'askingPrice', 'numberBeds', 'numberBaths', 'address', 'photo1']

class ImageUpdate(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['photo1', "photo2", "photo3", 'photo1_priority', 'photo2_priority', 'photo3_priority']
        extra_kwargs = {
            'photo1': {'read_only': True},
            'photo2': {'read_only': True},
            'photo3': {'read_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Create a list of photo items with their priorities
        photos = [
            {'photo': representation['photo1'], 'priority': representation['photo1_priority']},
            {'photo': representation['photo2'], 'priority': representation['photo2_priority']},
            {'photo': representation['photo3'], 'priority': representation['photo3_priority']},
        ]
        
        # Sort photos based on priority
        sorted_photos = sorted(photos, key=lambda x: x['priority'])
        
        # Return the sorted photos
        return {'photos': [photo['photo'] for photo in sorted_photos]}