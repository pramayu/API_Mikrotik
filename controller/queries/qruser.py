import graphene

class QrUser(graphene.ObjectType):
	user = graphene.String()

	def resolve_user(root, info):
		pass