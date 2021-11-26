from rest_framework import serializers
from .models import Group, Event, UserProfile, Member
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password= serializers.CharField(required=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id","image", "is_premium", "bio")

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "profile")
        extra_kwargs = {"password":{"write_only":True, "required":False}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        Token.objects.create(user=user)
        return user


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "team1", "team2", "time", "score1", "score2", "group")

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Member
        fields = ("user", "group", "admin")



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields= ("id", "name", "location", "description")

class GroupFullSerializer(serializers.ModelSerializer):
        events = EventSerializer(many=True)
      ##  members = MemberSerializer(many=True)
        members = serializers.SerializerMethodField()

        class Meta:
            model = Group
            fields = ("id", "name", "location", "description", "events", "members")

        def get_members(self, obj):
            people_points = []
            members = obj.members.all()
            for member in members:
                    points = 0
                    member_serialized = MemberSerializer(member, many=False)
                    member_data = member_serialized.data
                    member_data['points'] = points

                    people_points.append(member_data)

            return people_points