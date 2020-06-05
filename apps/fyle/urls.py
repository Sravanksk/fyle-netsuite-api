from django.urls import path

from .views import ExpenseGroupView, ExpenseGroupByIdView, ExpenseGroupScheduleView, ExpenseView, EmployeeView, \
    CategoryView, CostCenterView, ProjectView, UserProfileView, ClusterDomainView

urlpatterns = [
    path('user/', UserProfileView.as_view()),
    path('expense_groups/', ExpenseGroupView.as_view()),
    path('expense_groups/trigger/', ExpenseGroupScheduleView.as_view()),
    path('expense_groups/<int:expense_group_id>/', ExpenseGroupByIdView.as_view()),
    path('expense_groups/<int:expense_group_id>/expenses/', ExpenseView.as_view()),
    path('employees/', EmployeeView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('cost_centers/', CostCenterView.as_view()),
    path('projects/', ProjectView.as_view()),
    path('domain/', ClusterDomainView.as_view())
]
