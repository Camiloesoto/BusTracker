from django.shortcuts import render
from django.http import JsonResponse
import openai
# Create your views here.

open_ai_key = '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'

openai.api_key = open_ai_key

def ask_openai(message):
    response = openai.Completion.create( 
        model = 'text-davinci-003',
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')



