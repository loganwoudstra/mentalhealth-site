from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry, CheckIn
from django.utils import timezone
from statistics import mean
import datetime
import tensorflow as tf
import re

# stopword_model = tf.keras.models.load_model('mentalhealth/stopword_model.h5')
# cbow_model = tf.keras.models.load_model('mentalhealth/cbow_model.h5')


def clean_data(text_data):
    text_data = re.sub('http\S+', ' ', text_data)  # remove http websites
    text_data = re.sub('www\S+', ' ', text_data)  # remove www websites
    text_data = re.sub('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', ' ', text_data)  # remove html markup
    text_data = re.sub('nbsp;', ' ', text_data)  # remove nbsp
    text_data = re.sub('@[A-Za-z0-9]+', ' ', text_data)  # remove mentions
    text_data = re.sub('[^A-Za-z\s]+', '', text_data)  # remove numbers, punctuation, emojis, anything not letters
    text_data = re.sub('\s\s+', ' ', text_data)  # remove extra whitespaces
    text_data = text_data.lower()  # makes everything lowercase
    return text_data


# Create your views here.
def home(response):
    if response.user.is_authenticated:
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        labels = []
        data = []
        day = timezone.localtime(timezone.now()).date()
        delta = datetime.timedelta(1)

        for i in range(7):
            labels.append(weekdays[day.weekday()])
            score = CheckIn.objects.filter(user=response.user).filter(date=day)
            if score:
                data.append(score[0].score)
            else:
                data.append(0)
            day -= delta

        if data[0] == 0:
            text = "Looks like you haven't completed you daily check-in today. Click the button below to start it"
        elif data[1] == 0:
            text = "Remember to complete your check-in every day to track your well-being throughout the week"
        elif data[0] > data[1]:
            text = "Looks like you're doing better today than you were yesterday. Keep it up!"
        else:
            text = "Looks like you're doing a little worse today than yesterday. No worries, there is always tomorrow!"

        labels.reverse()
        data.reverse()

    else:
        labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        data = [1.0, 3.4, 4.4, 2.6, 3.6, 4.2, 1.6]
        text = "Sign in  to complete daily check-ins to track your mental health over time"

    return render(response, 'mentalhealth/home.html', {
        'labels': labels,
        'data': data,
        'text': text,
    })


def newentry(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = EntryForm(response.POST)
            if form.is_valid():
                entry = form.save(commit=False)
                if len(entry.text) > 200:
                    entry.preview = entry.text[:197] + "..."
                else:
                    entry.preview = entry.text
                entry.user = response.user
                entry.last_edit_date = timezone.localtime(timezone.now())

                detected_depression = False
                if stopword_model.predict([clean_data(entry.text)])[0] >= 0.6 and cbow_model.predict([clean_data(entry.text)])[0] >= 0.6:

                    entry.depression = True
                    detected_depression = True
                entry.save()

                # a boolean value is used to determine whether to redirect because if a rediredct within the above if
                # statement, the entry won't be saved
                if detected_depression:
                    return redirect("/depression_detected")

            return redirect("/allentries")
        else:
            form = EntryForm()

        return render(response, "mentalhealth/newentry.html", {"form": form})
    else:
        return redirect("/login")


def allentries(response):
    if response.user.is_authenticated:
        entries = Entry.objects.filter(user=response.user)
        return render(response, 'mentalhealth/allentries.html', {'entries': entries})
    else:
        return redirect("/login")


def oldentry(response, id):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = EntryForm(response.POST)
            if form.is_valid():
                entry = Entry.objects.get(id=id)
                entry.title = form.cleaned_data['title']
                entry.text = form.cleaned_data['text']
                entry.last_edit_date = timezone.localtime(timezone.now())
                if len(entry.text) > 200:
                    entry.preview = entry.text[:197] + "..."
                else:
                    entry.preview = entry.text

                detected_depression = False
                if stopword_model.predict([clean_data(entry.text)])[0] >= 0.6 and cbow_model.predict([clean_data(entry.text)])[0] >= 0.6:
                    entry.depression = True
                    detected_depression = True
                else:  # only needed for edits because old depressive entries could be edited to not be depressive
                    entry.depression = False
                entry.save()

                if detected_depression:
                    return redirect("/depression_detected")

            return redirect("/allentries")

        else:
            entry = Entry.objects.get(id=id)
            initial = {'title': entry.title, 'text': entry.text}
            form = EntryForm(initial=initial)

            return render(response, "mentalhealth/oldentry.html", {"form": form, 'entry': entry})
    else:
        return redirect("/login")


def del_entry(response, id):
    if response.user.is_authenticated:
        entry = Entry.objects.get(id=id)

        if response.method == 'POST':
            entry.delete()
            return redirect('/allentries')

        return render(response, 'mentalhealth/oldentry.html', {'entry': entry})
    else:
        return redirect("/login")


def checkin(response):
    if response.user.is_authenticated:
        if not CheckIn.objects.filter(user=response.user).filter(date=timezone.localtime(timezone.now()).date()):
            if response.method == "POST":
                questions = response.POST.getlist('questions')
                int_questions = [int(q) for q in questions]
                score = mean(int_questions)

                ci = CheckIn(user=response.user, score=score, date=timezone.localtime(timezone.now()).date())
                ci.save()
                return redirect("/")

            return render(response, "mentalhealth/checkin.html", {'not_done': True})
        else:
            return render(response, "mentalhealth/checkin.html")
    else:
        return redirect("/login")

def depression_detected(response):
    return render(response, "mentalhealth/depression_detected.html")

def about_model(response):
    return render(response, "mentalhealth/about_model.html")
