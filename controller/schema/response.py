import graphene

class ObjRespond(graphene.ObjectType):
	status 	= graphene.Boolean()
	messag 	= graphene.String()
	topath 	= graphene.String()