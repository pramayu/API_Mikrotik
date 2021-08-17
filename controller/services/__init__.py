import graphene
from controller.services.signin import SignUser

class Service(graphene.ObjectType):
	signuser 	= SignUser.Field()