from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"MyAppHTML/index.html")

def gradeTable(request):
    return render(request,"MyAppHTML/gradeTable.html")

def cgpa_calculation(request):
    cgpa_value = None
    sem1 = None

    if request.method == 'POST':
        try:
            sem1 = float(request.POST.get('sem1', 0))
            sem2 = float(request.POST.get('sem2', 0))
            sem3 = float(request.POST.get('sem3', 0))
            sem4 = float(request.POST.get('sem4', 0))
            sem5 = float(request.POST.get('sem5', 0))
            sem6 = float(request.POST.get('sem6', 0))
            sem7 = float(request.POST.get('sem7', 0))
            sem8 = float(request.POST.get('sem8', 0))

            # Calculate CGPA only if all fields are not empty
            total_sum = sem1 + sem2 + sem3 + sem4 + sem5 + sem6 + sem7 + sem8
            cgpa_value = "{:.1f}".format(total_sum / 8)  # You might want to add validation to ensure inputs are valid
            # if cgpa_value:
            #     return HttpResponse(f"""
            #                  <script>
            #                      alert(`Your CGPA is : {cgpa_value}`);
            #                      window.location.href = 'http://127.0.0.1:8000/cgpa_cal';
            #                  </script>
            #             """)
        except ValueError:
            cgpa_value = "Invalid input"  # Handle the case where conversion to float fails


    return render(request, "MyAppHTML/cgpa_eigthtSem.html",context={"cgpa_value":cgpa_value})

def cgpa_calculation_sixSem(request):
    cgpa_value = None
    sem1 = None

    if request.method == 'POST':
        try:
            sem1 = float(request.POST.get('sem1', 0))
            sem2 = float(request.POST.get('sem2', 0))
            sem3 = float(request.POST.get('sem3', 0))
            sem4 = float(request.POST.get('sem4', 0))
            sem5 = float(request.POST.get('sem5', 0))
            sem6 = float(request.POST.get('sem6', 0))


            # Calculate CGPA only if all fields are not empty
            total_sum = sem1 + sem2 + sem3 + sem4 + sem5 + sem6
            cgpa_value = "{:.1f}".format(total_sum / 6)  # You might want to add validation to ensure inputs are valid
            # if cgpa_value:
            #     return HttpResponse(f"""
            #                  <script>
            #                      alert(`Your CGPA is : {cgpa_value}`);
            #                      window.location.href = 'http://127.0.0.1:8000/cgpa_cal';
            #                  </script>
            #             """)
        except ValueError:
            cgpa_value = "Invalid input"  # Handle the case where conversion to float fails


    return render(request, "MyAppHTML/cgpa_sixSem.html",context={"cgpa_value":cgpa_value})






def cgpa_percentage(request):
    cgpa_percentage_value = None
    sem1 = None

    if request.method == 'POST':
        try:
            cgpa_value = float(request.POST.get('percentage', 0))

            # Calculate CGPA percentage
            percentage=cgpa_value * 9.5
            cgpa_percentage_value = "{:.1f}".format(percentage)

        except ValueError:
            cgpa_percentage_value = "Invalid input"  # Handle the case where conversion to float fails
    return render(request, "MyAppHTML/cgpa_percentage.html",context={"cgpa_percentage_value":cgpa_percentage_value})



