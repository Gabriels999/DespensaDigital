from despensa.products.models import User
from ..models import Profile


def user_jon():
    ze = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
    )
    return ze


def profile_jon():
    ze = user_jon()
    profile_ze = Profile(
        user=ze,
        bio='Staff dev',
        avatar='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7b_kyJLpVSVTw48E8LjRICv73BfaKJ9RAtQoYzmD4jwjnWEJ-dMzHInpgP9t10ZQdb6A&usqp=CAU'
    ).save()
    return profile_ze
