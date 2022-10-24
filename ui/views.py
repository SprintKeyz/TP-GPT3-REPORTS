from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'title': 'Report Card Commenter'})


'''
<h2>REPORT CREATOR</h2>
        <div class="category" id="cat1">
            <p>Student file</p>
            <div id="uploadbox1" class="uploadbox">
                <img src="{% static 'img/file.svg' %}" draggable="false">
                <p>Click or drag files here to upload</p>
            </div>
        </div>

        <hr>

        <div class="buttons">
            <button id="reset">Reset</button>
            <button id="submit">Generate</button>
        </div>
'''
