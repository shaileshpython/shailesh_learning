from django.contrib import admin
from django.urls import path
from . import views

# views.UsersListApiView.as_view(), name="users"
# /api/v1/expensesbyteam/{team_id} # .as_view(), name="users"
urlpatterns = [

    # path('admin/', admin.site.urls),
    # path('/api/v1/expensesbyteam/<int:pk>/',views.TeamExpenses.as_view(),name="team_expenses"),

]