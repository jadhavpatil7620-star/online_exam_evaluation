from django.urls import path
from exam import views

urlpatterns = [
    path('addquestion/', views.AddQuestionPage),
    path('addquestionpage/', views.AddQuestion),
    path('updatequestionpage/', views.UpdateQuestionPage),
    path('updatequestion/', views.UpdateQuestion),
    path('viewquestionpage/', views.ViewQuestionPage),
    path('viewquestion/', views.ViewQuestion),
    path('deletequestionpage/', views.DeleteQuestionPage),
    path('deletequestion/', views.DeleteQuestion),
    path('questioncurdpage/', views.QuestionCurdPage),
    path('showallquestion/', views.ShowAllQuestion),
    
    # Student Page Urls
    path('studentregisterpage/', views.StudentRegisterPage),
    path('studentregister/', views.StudentRegister),
    path('deletestudentpage/', views.DeleteStudentPage),
    path('deletestudent/', views.DeleteStudent),
    path('updatestudentpage/', views.UpdateStudentPage),
    path('updatestudent/', views.UpdateStudent),
    path('viewstudentpage/', views.ViewStudentPage),
    path('viewstudent/', views.ViewStudent),
    path('showallstudentpage/', views.ShowAllStudentPage),
    path('studentcurdpage/', views.StudentCurdPage),
    path('home/', views.HomePage),
    # path('startexam/', views.StartTest),
    path('studentlogin/', views.StudentLogin),
    path('', views.StudentLoginPage),
    # path('subjectpage/', views.SubjectPage),
    path('startexam/', views.StartExam),
    path('nextquestion/', views.NextQuestion),
    path('previousquestion/', views.PreviousQuestion),
    path('endtest/', views.EndTest),
    path('logout/', views.Logout),
    path('showallresult/', views.ShowAllResult),
    path('module/', views.ModulePage),
    
    # API URLS
    path('viewapi/', views.ViewRest),
    path('getapi/<str:uname>', views.GetData),
]
