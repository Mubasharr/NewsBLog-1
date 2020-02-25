import  graphene
from graphene_django.types import  DjangoObjectType
from blogs.models import Categories, NewsBlog


class CategoryType(DjangoObjectType):
    class Meta:
        model = Categories


class News(DjangoObjectType):
    class Meta:
        model = NewsBlog


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_news = graphene.List(News)

    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Categories.objects.get(pk=id)

        if name is not None:
            return Categories.objects.get(name=name)

        return None

    def resolve_all_categories(self, info, **kwargs):
        return  Categories.objects.all()

    def resolve_all_news(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return NewsBlog.objects.select_related('category').all()


# Add New Category Mutation
class AddCategory(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        categoryName = graphene.String(required=True)

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    def mutate(self, info, categoryName):

        _category = Categories.objects.create(name=categoryName)

        # Notice we return an instance of this mutation
        return AddCategory(category=_category)


### Update Category
class CategoryUpdate(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        categoryTitle = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    def mutate(self, info, categoryTitle, id):
        category = Categories.objects.get(pk=id)
        category.name = categoryTitle
        category.save()
        # Notice we return an instance of this mutation
        return CategoryUpdate(category=category)

# Delete Category
class DeleteCategory(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Categories.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)

class Mutation(object):
    update_category = CategoryUpdate.Field()
    add_category = AddCategory.Field()
    delete_category = DeleteCategory.Field()