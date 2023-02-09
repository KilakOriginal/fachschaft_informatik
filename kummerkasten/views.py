from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Fachschaft InfMath home page
def homePage(request):
    return redirect("https://www.fs-infmath.uni-kiel.de/wiki/Hauptseite")

# Success page (local app)
def messageSuccess(request):
    return render(request, "kummerkasten/message-success.html")

# Error page (local app)
def messageError(request):
    return render(request, "kummerkasten/message-error.html")

# Message form (Kummerkasten local app home)
def messageForm(request):
    import os.path, json
    lang = request.GET.get("lang")  # get-request for language
    text = {}  # Store text to be displayed on web page
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Locate this file
    file_path = ""  #  Language file location

    # If no language is specified use German as default
    if not lang:
        lang = "de"
        file_path = f"{dir_path}/languages/de.json"
    # Else use the language specified
    else:  
        file_path = f"{dir_path}/languages/{lang}.json"
        
        # Display a 404 page if an unknown language is specified
        if not os.path.isfile(file_path):
            from django.http import HttpResponseNotFound
            return HttpResponseNotFound("<h1>Error Code 405: Illegal query</h1><br><a href=\"./?lang=de\">Open form (german)</a><br><a href=\"./?lang=en\">Open form (english)</a>")
    
    # Load the language file contents into the text dict
    with open(file_path, encoding='utf-8') as f:
        text = json.loads(f.read())

    # On form submit
    if request.method == "POST":
        from . import send_mail
        form = send_mail.EmailForm(request.POST or None)  # Temporarily store form contents (subject and message)

        # If the user input was valid and the email was successfully sent display the success page
        if form.is_valid() and not send_mail.send_mail(text["recipient"], form.cleaned_data["subject"], form.cleaned_data["message"]):
            return render(request, f"kummerkasten/message-success.html", {"text":text})
        return render(request, f"kummerkasten/message-error.html", {"text":text})  # Otherwise display the error page
    
    # Initial state (no submission)
    return render(request, "kummerkasten/message-form.html", {"text":text, "lang":lang})
