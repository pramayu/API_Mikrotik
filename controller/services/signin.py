import graphene
from controller.schema.response import ObjRespond

class SignUser(graphene.Mutation):

	class Arguments:
		username 	= graphene.String()
		password 	= graphene.String()
		ipaddres 	= graphene.String()

	Output = ObjRespond

	def mutate(self, info, **kwargs):
		return ObjRespond(status=True, messag='ok', topath='user')