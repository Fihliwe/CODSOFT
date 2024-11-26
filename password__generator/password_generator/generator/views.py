import string
import random
from django.shortcuts import render

def home(request):
    return render(request, 'generator/home.html')

def generate_password(request):
    if request.method == "POST":
        characters_number = int(request.POST.get('length', 8))
        if characters_number < 8:
            return render(request, 'generator/home.html', {
                'error': "Password length must be at least 8 characters."
            })

        # Character sets
        s1 = list(string.ascii_lowercase)
        s2 = list(string.ascii_uppercase)
        s3 = list(string.digits)
        s4 = list(string.punctuation)

        random.shuffle(s1)
        random.shuffle(s2)
        random.shuffle(s3)
        random.shuffle(s4)

        # Determine number of characters from each set
        part1 = round(characters_number * (30 / 100))
        part2 = round(characters_number * (20 / 100))

        result = []
        for x in range(part1):
            result.append(s1[x])
            result.append(s2[x])

        for x in range(part2):
            result.append(s3[x])
            result.append(s4[x])

        random.shuffle(result)
        password = "".join(result)

        return render(request, 'generator/home.html', {
            'password': password
        })

    return render(request, 'generator/home.html')
