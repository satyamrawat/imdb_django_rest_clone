from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatforms, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many = True, read_only = True)
    platform = serializers.CharField(source = 'platform.name')
    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ['active']

    # def get_len_name(slef,object):
    #     return len(object.name)

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title adn description cannot be same as description")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Name too short")
    #     else:
    #         return value


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many = True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name= 'movie-detail'
    # )
    # url = serializers.HyperlinkedIdentityField(view_name="streamplatform")
    class Meta:
        model = StreamPlatforms
        fields = "__all__"


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.active = validated_data.get('active')
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title adn description cannot be same as description")
#         else:
#             return data


#     def validate_name(self, value):
#         if len(value < 5):
#             raise serializers.ValidationError("Name too short")
#         else:
#             return value
