from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import glob
import os.path

# import lms_algorithm

def home(request):
    return None

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        # print(lms_algorithm.error_mse)
    return render(request, 'index.html')

def downloadfile(request):
    folder_path = r'C:\Users\krish\Desktop\gainedgeproject\testsite\algo_output'
    file_type = r'\*jpg'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    chunk_size = 8192
    path = open(max_file,'r')
    mime_type, _ = mimetypes.guess_type(max_file)
    response = StreamingHttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = 'attachment; filename=%s' % max_file
    return response

# output display error
# importing algorithm file and displaying loading icon till it completes
