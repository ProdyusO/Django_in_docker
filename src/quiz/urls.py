from django.urls import path

from .views import ExamListView, ExamDetailView, ExamResultCreateView, ExamQuestionView, ExamResultDetailView, \
    ExamResultUpdateView, ExamResultDeleteView, ExamResultListView

app_name = 'quizzes'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
    path('result_list/', ExamResultListView.as_view(), name='result_list'),
    path('<uuid:uuid>/results/create/', ExamResultCreateView.as_view(), name='result_create'),
    path('<uuid:uuid>/results/<uuid:result_uuid>/details/', ExamResultDetailView.as_view(), name='result_details'),
    path('<uuid:uuid>/results/<uuid:result_uuid>/update/', ExamResultUpdateView.as_view(), name='result_update'),
    path('<uuid:uuid>/results/<uuid:result_uuid>/delete/', ExamResultDeleteView.as_view(), name='result_delete'),
    path('<uuid:uuid>/results/<uuid:result_uuid>/question/next/', ExamQuestionView.as_view(), name='question'),
]