from django.shortcuts import render, redirect
from django.views import View
from todo.models import Todo

# Create your views here.
# トップ画面
class IndexView(View):
    
    # Getリクエストの時の処理
    def get(self, request):
        '''GETリクエストを受け付けたとき'''
        todos = Todo.objects.all().order_by('-updated_at')
        return render(request, 'todo/index.html',{
            'todos': todos
        })
            # render(request, パス, 渡したいデータ(辞書形式))
    
    # Postリクエストの時の処理
    def post(self, request):
        '''POSTリクエストでTODO登録がsubmitされたとき'''

        # フォームから渡ってくるリクエストボディの内容をDBに記録する
        memo = request.POST['memo']
        todo = Todo(memo=memo)
        todo.save()
        return redirect('/')
            # リダイレクト → 別のページに転送する
        