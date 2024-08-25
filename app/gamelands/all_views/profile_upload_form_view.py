from django.shortcuts import render
from gamelands.forms import ProfileForm

def profile_upload_form(request):
    context = {
        'form': ProfileForm()
    }
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            context = {'profile_pic': form}
        else:
            context = {
                'form':form
            }
            return render(request, 'html/cabinet.html', context )
    return render(request, 'html/cabinet.html', context )
    