from django.shortcuts import render
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items
from Base_App.models import BookTable

# Create your views here.

def HomeView(request):
    return render(request, 'index.html')

def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')

        if name != '' and phone_number != 0 and email != '' and total_person != 0 and booking_date != '':
            data = BookTable(Name=name, Phone_Number=phone_number, Email=email, Total_Person=total_person,
                             Booking_Date=booking_date)
            data.save()
    return render(request, 'book_table.html')

def MenuView(request):
    return render(request, 'menu.html')

def AboutView(request):
    return render(request, 'about.html')

def FeedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('your_name')
        description = request.POST.get('descriptions')
        rating = request.POST.get('give_us_rating')

        data = Feedback(User_Name=name, Description=description, Rating=rating)
        data.save()
    return render(request, 'feedback.html')

