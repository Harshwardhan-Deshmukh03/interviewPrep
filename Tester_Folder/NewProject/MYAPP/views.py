from django.shortcuts import render

#aarya edit
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HomePage")
def contact(request):
    return render(request,'MYAPP/dashboard.html')
def contact2(request):
    return render(request,'MYAPP/resources.html')
def index(request):
    context = {
        'pageTitle': 'Data Science',
        'paragraph1': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
        'paragraph2': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
        'btnLink': 'http://127.0.0.1:8000/generate-pdf/',
        'btnText': 'Click Here'
    }
    return render(request, 'MYAPP/index.html', context)




#PDF FORM
# views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import render
from .admin import MyForm

# def generate_pdf(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             # Extract form data
#             name = form.cleaned_data['name']
#             age = form.cleaned_data['age']
            
#             # Generate PDF
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="output.pdf"'
#             p = canvas.Canvas(response, pagesize=letter)
#             p.drawString(100, 750, "Name: " + name)
#             p.drawString(100, 730, "Age: " + str(age))
#             p.save()
#             return response
#     else:
#         form = MyForm()
#     return render(request, 'MYAPP/resources.html', {'form': form})

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io

# def generate_pdf(request):
#     # Render the HTML template
#     template = get_template('MYAPP/index.html')
#     context = {}  # Add any context data here
#     html = template.render(context)

#     # Create a PDF response
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="output.pdf"'

#     # Generate PDF from HTML
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('PDF generation error!')

#     return response
def generate_pdf(request):
    # Render the HTML template
    template = get_template('MYAPP/index.html')
    context = {
        'pageTitle': 'Data Science',
        'paragraph1': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
        'paragraph2': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
        'btnLink': '#',
        'btnText': ''
    }
    html = template.render(context)

    # Create a PDF file
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

    # Return PDF as response
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="my_website.pdf"'
        return response
    return HttpResponse('Error rendering PDF', status=500)


