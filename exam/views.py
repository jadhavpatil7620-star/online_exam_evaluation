from django.shortcuts import render
from exam.models import Question, Stud_Info, Result
from django.contrib.auth import logout

# Create your views here.

# Question Page All Views Are Here
def AddQuestionPage(request):
    return render(request, 'questions/addquestion.html')

def AddQuestion(request):
    try:
        qid = request.POST['qid']
        sub = request.POST['subject']
        que = request.POST['question']
        opt1 = request.POST['opt1']
        opt2 = request.POST['opt2']
        opt3 = request.POST['opt3']
        opt4 = request.POST['opt4']
        cor_ans = request.POST['rightans']
        
        quedb = Question.objects.create(
            que_id = qid,
            sub_name = sub,
            que_name = que,
            option_1 = opt1,
            option_2 = opt2,
            option_3 = opt3,
            option_4 = opt4,
            correct_ans = cor_ans
        )
        
        return render(request, 'questions/addquestion.html', {'quedb': quedb, 'msg': 'Question Added Successfully !!!'})
    except:
        return render(request, 'questions/addquestion.html', {'msg': 'Question ID is already present !!!'})


def UpdateQuestionPage(request):
    return render(request, 'questions/updatequestion.html')

def UpdateQuestion(request):
    qid = request.GET['qid']
    sub = request.GET['subject']
    que = request.GET['question']
    opt1 = request.GET['opt1']
    opt2 = request.GET['opt2']
    opt3 = request.GET['opt3']
    opt4 = request.GET['opt4']
    cor_ans = request.GET['rightans']
    
    Question.objects.filter(que_id=qid, sub_name=sub)
    
    # if Question.que_id == qid and Question.sub_name == sub:
    quedb = Question.objects.update(
        que_name = que,
        option_1 = opt1,
        option_2 = opt2,
        option_3 = opt3,
        option_4 = opt4,
        correct_ans = cor_ans
    )
    
    return render(request, 'questions/updatequestion.html', {'quedb': quedb, 'msg': 'Question Updated Successfully !!!'})
    
    # else:
    #     return render(request, 'questions/updatequestion.html', {'msg': 'Subject Name Or Subject ID Invalid !!!'})
    
def ViewQuestionPage(request):
    return render(request, 'questions/viewquestion.html')

def ViewQuestion(request):
    qid = request.GET['qid']
    sub = request.GET['subject']
    
    quedb = Question.objects.get(que_id=qid, sub_name=sub)

    return render(request, 'questions/viewquestion.html', {'quedb': quedb})

def DeleteQuestionPage(request):
    return render(request, 'questions/deletequestion.html')

def DeleteQuestion(request):
    qid = request.GET['qid']
    sub = request.GET['subject']
    
    Question.objects.get(que_id=qid, sub_name=sub).delete()
    
    return render(request, 'questions/deletequestion.html', {'msg':'Question Deleted Successfully !!!'})

def QuestionCurdPage(request):
    if request.session.get('role') != 'admin':
        return render(request, 'student/login.html', {'msg': 'Access Denied !!!'})
    return render(request, 'questions/questioncurd.html')

def ShowAllQuestion(request):
    
    quedb = Question.objects.all()
    return render(request, 'questions/showallquestions.html', {'quedb': quedb})

# Student Views Start Here

def StudentRegisterPage(request):
    return render(request, 'students/addstudent.html')

def StudentRegister(request):
    if request.method == 'POST':
        
        uname = request.POST.get('username')
        psw = request.POST.get('password')
        cfpsw = request.POST.get('cfpassword')
        email = request.POST.get('email')
        mobno = request.POST.get('mobile_no')
        
        if psw != cfpsw:
            return render(request, 'students/addstudent.html', {'msg': 'Confirm Password Should Be Same !!!'})
        
        Stud_Info.objects.create(
            username = uname,
            password = psw,
            email = email,
            mobile_no = mobno
        )
        
        return render(request, 'students/login.html', {'msg':'Student Logged IN Successfully !!!'})
    
def StudentLoginPage(request):
    return render(request, 'students/login.html')
    
def StudentLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        psw = request.POST.get('password')
        userdb = Stud_Info.objects.filter(username=uname).first()
        if userdb is None:
            return render(request, 'students/login.html', {'msg': 'Username Does Not Exist !!!'})

        if userdb.password != psw:
            return render(request, 'students/login.html', {'msg': 'Invalid Password !!!'})

        request.session['username'] = uname
        request.session['role'] = userdb.role
        request.session['answer'] = {}
        request.session['score'] = 0
        request.session['qno'] = 0

        if userdb.role == 'admin':
            return render(request, 'admin/admindashboard.html')
        subject = Question.objects.values('sub_name').distinct()
        return render(request, 'students/subject.html', {'subject': subject})
    return render(request, 'students/login.html')
    
def DeleteStudentPage(request):
    return render(request, 'students/deletestudent.html')
    
def DeleteStudent(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        
        if Stud_Info.username != uname:
            return render(request, 'students/deletestudent.html', {'msg': 'Username Does Not Exitst !!!'})
        
        Stud_Info.objects.get(username=uname).delete()
        return render(request, 'students/deletestudent.html', {'msg': 'Student Deleted Successfully !!!'})
    
def UpdateStudentPage(request):
    return render(request, 'students/updatestudent.html')

def UpdateStudent(request):
    if request.method == 'POST':
        
        uname = request.POST.get('username')
        psw = request.POST.get('password')
        email = request.POST.get('email')
        mobno = request.POST.get('mobile_no')
        
        userdb = Stud_Info.objects.filter(username=uname)
        
        if not userdb.exists():
            return render(request, 'student/updatestudent.html', {'msg': 'Username does not exists !!!'})
        
        userdb.update(
            password = psw,
            email = email,
            mobile_no = mobno
        )
        
        return render(request, 'students/updatestudent.html', {'userdb': userdb, 'msg': 'Student Updated Successfully !!!'})
    
def ViewStudentPage(request):
    return render(request, 'students/viewstudent.html')

def ViewStudent(request):
    if request.method == 'POST':
        
        uname = request.POST.get('username')
        
        userdb = Stud_Info.objects.get(username=uname)
        
        return render(request, 'students/viewstudent.html', {'userdb': userdb})

def ShowAllStudentPage(request):
    
    userdb = Stud_Info.objects.all()
    
    return render(request, 'students/showallstudents.html', {'userdb': userdb})

def StudentCurdPage(request):
    return render(request, 'students/studentcurd.html')

def HomePage(request):
    return render(request, 'home.html')

# def StartExam(request):
#     if request.session.get('role') != 'student':
#         return render(request, 'student/login.html', {'msg': 'Access Denied !!!'})
#     if request.method == 'POST':
#         subject = request.POST.get('subject')
#         request.session['subject'] = subject
        
#         question = Question.objects.filter(sub_name=subject).values()
        
#         allquestion = list(question)
#         request.session['allquestion'] = allquestion
        
#         return render(request, 'starttest.html', {'question': allquestion[0]})

def StartExam(request):

    if request.method == 'POST':

        subject = request.POST.get('subject')

        request.session['subject'] = subject

        allquestion = list(
            Question.objects.filter(
                sub_name=subject
            ).values()
        )

        request.session['allquestion'] = allquestion
        request.session['qno'] = 0
        request.session['answer'] = {}

        return render(
            request,
            'starttest.html',
            {
                'question': allquestion[0],
                'qno': 0,
                'totalquestion': len(allquestion)
            }
        )
    
def NextQuestion(request):

    allquestion = request.session['allquestion']
    questionindex = request.session['qno']

    if 'op' in request.POST:

        answer = request.session['answer']

        answer[str(questionindex)] = [
            request.POST.get('qno'),
            request.POST.get('que_name'),
            request.POST.get('op'),
            request.POST.get('answer')
        ]

        request.session['answer'] = answer

    if questionindex < len(allquestion) - 1:

        request.session['qno'] += 1

        questionindex = request.session['qno']

        question = allquestion[questionindex]

        return render(
            request,
            'starttest.html',
            {
                'question': question,
                'qno': request.session['qno'],
                'totalquestion': len(allquestion)
            }
        )

    question = allquestion[-1]

    return render(
        request,
        'starttest.html',
        {
            'question': question,
            'qno': request.session['qno'],
            'totalquestion': len(allquestion)
        }
    )
    
def PreviousQuestion(request):

    allquestion = request.session['allquestion']
    questionindex = request.session['qno']

    if 'op' in request.POST:

        answer = request.session['answer']

        answer[str(questionindex)] = [
            request.POST.get('qno'),
            request.POST.get('que_name'),
            request.POST.get('op'),
            request.POST.get('answer')
        ]

        request.session['answer'] = answer

    if questionindex > 0:

        request.session['qno'] -= 1

        questionindex = request.session['qno']

        question = allquestion[questionindex]

        return render(
            request,
            'starttest.html',
            {
                'question': question,
                'qno': request.session['qno'],
                'totalquestion': len(allquestion)
            }
        )

    question = allquestion[0]

    return render(
        request,
        'starttest.html',
        {
            'question': question,
            'qno': 0,
            'totalquestion': len(allquestion)
        }
    )
        
def EndTest(request):

    if 'op' in request.POST:

        answer = request.session['answer']

        answer[str(request.session['qno'])] = [
            request.POST.get('qno'),
            request.POST.get('que_name'),
            request.POST.get('op'),
            request.POST.get('answer')
        ]

        request.session['answer'] = answer

    response = list(request.session['answer'].values())

    score = 0

    for res in response:

        if res[2] == res[3]:

            score += 1

    finalscore = score

    uname = request.session['username']

    userdb = Stud_Info.objects.get(
        username=uname
    )

    subject = request.session['subject']

    Result.objects.create(
        username=userdb,
        subject=subject,
        score=finalscore
    )

    return render(
        request,
        'result/scorecard.html',
        {
            'response': response,
            'finalscore': finalscore
        }
    )

def Logout(request):
    logout(request)
    return render(request, 'students/login.html')

def ShowAllResult(request):
    resultdb = Result.objects.all()
    return render(request, 'result/showallresult.html', {'resultdb': resultdb})

def ModulePage(request):
    return render(request, 'module.html')

########################################################################################################################################

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer

@api_view(['GET'])
def ViewRest(request):
    return Response({'EMP ID': 'GSD1578', 'EMP NAME': 'Gopal', 'Degination': 'SD'})

@api_view(['GET'])
def GetData(request, uname):
    userdb = Stud_Info.objects.get(username=uname)
    return Response({'Username': userdb.username, 'Password': userdb.password, 'Email': userdb.email, 'Mobile No.': userdb.mobile_no})