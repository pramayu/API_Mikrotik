import graphene
from controller.queries.qruser import QrUser
from controller.services import Service

class Query(QrUser, graphene.ObjectType):
	pass

class Mutation(Service, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query, mutation=Mutation)