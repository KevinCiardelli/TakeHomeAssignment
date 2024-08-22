from rest_framework import serializers
from .models import Property

#Serializer for the browsing function, want to display all relevant information with one picture
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'askingPrice', 'numberBeds', 'numberBaths', 'address', 'photo1']


#Serializer for both showing the order of photos, and modification of the order
class ImageUpdate(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['photo1', "photo2", "photo3", 'photo1_priority', 'photo2_priority', 'photo3_priority']

        #Do not want to edit the photo names / urls / strings
        extra_kwargs = {
            'photo1': {'read_only': True},
            'photo2': {'read_only': True},
            'photo3': {'read_only': True}
        }

    #This is how we are going to sort our photos based on a priority systems
    #Each photo has a set priority and will be displayed based on the lowest priority in order
    #Implemenetation with ios can be associated with setting priority variabgle equal to placement wihtin and array (index) upon modification/saving
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        photos = [
            {'photo': representation['photo1'], 'priority': representation['photo1_priority']},
            {'photo': representation['photo2'], 'priority': representation['photo2_priority']},
            {'photo': representation['photo3'], 'priority': representation['photo3_priority']},
        ] 

        sorted_photos = sorted(photos, key=lambda x: x['priority'])
        
        return {'photos': [photo['photo'] for photo in sorted_photos]}