import  graphene
import blogs.schema

class Query(blogs.schema.Query, graphene.ObjectType):
    pass

class Mutation(blogs.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

