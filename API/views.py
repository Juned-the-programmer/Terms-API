from django.shortcuts import render
from django.http import JsonResponse
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ImageSerializer

import pytesseract

import pandas as pd
import re
import string

import pickle
import cv2
# Create your views here.
@api_view(['GET'])
def list_api(request):
    return JsonResponse("Terms and conditions API",safe=False)

@api_view(['POST'])
def text_extract(request):

    image_data = request.data
    
    print(image_data)
    
    serializer = ImageSerializer(data=image_data)

    if serializer.is_valid():  
        serializer.save()

    image = Image_to_Text.objects.all().last().image
    image_path = image.path

    image_gray = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image_gray , cv2.COLOR_BGR2GRAY)

    ret, th = cv2.threshold(gray_image ,
        127,  # threshold value
        255,  # maximum value assigned to pixel values exceeding the threshold
        cv2.THRESH_BINARY) 

    Extracted_Text = pytesseract.image_to_string(image_path)

    return JsonResponse(Extracted_Text , safe=False)
    # return Response(serializer.data)

@api_view(['POST'])
def text_process(request):

    news = str(request.data['news'])
    print(news)

    saved_db = pickle.load(open("model_db.sav" , 'rb'))
    saved_adb = pickle.load(open("model_adb.sav" , 'rb'))
    saved_GBC = pickle.load(open("model_GBC.sav" , 'rb'))
    saved_LR = pickle.load(open("model_LR.sav" , 'rb'))
    saved_RFC = pickle.load(open("model_RFC.sav" , 'rb'))
    saved_svm = pickle.load(open("model_svm.sav" , 'rb'))

    saved_vectors = pickle.load(open("model_vectorization.sav" ,'rb'))

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorization = TfidfVectorizer(analyzer='word',stop_words='english')

    def wordopt(text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub("\\W"," ",text) 
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
            
        return text

    def output_label(n):
        if n == 0:
            return "Fake News"
        elif n == 1:
            return "Not A Fake News"

    def manual_testing(news):
        testing_news = {"text":[news]}
        print(testing_news)
        new_def_test = pd.DataFrame(testing_news)
        print(new_def_test)
        new_def_test["text"] = new_def_test["text"].apply(wordopt)
        new_x_test = new_def_test["text"]
        new_xv_test = saved_vectors.transform(new_x_test)
        pred_DT = saved_db.predict(new_xv_test)
        pred_ADB = saved_adb.predict(new_xv_test)
        pred_GBC = saved_GBC.predict(new_xv_test)
        pred_LR = saved_LR.predict(new_xv_test)
        pred_RFC = saved_RFC.predict(new_xv_test)
        pred_SVM = saved_svm.predict(new_xv_test)

        return print("\n\n DT Prediction : {}\n ADB Prediction : {}\n GBC Prediction : {}\n LR Prediction : {}\n RFC Prediction : {}\n SVM Prediction : {} ".format(output_label(pred_DT[0]),
                                                                                                                                                                    output_label(pred_ADB[0]),
                                                                                                                                                                    output_label(pred_GBC[0]),
                                                                                                                                                                    output_label(pred_LR[0]),
                                                                                                                                                                    output_label(pred_RFC[0]),
                                                                                                                                                                    output_label(pred_SVM[0])))

    manual_testing(news)

    return JsonResponse("Terms and conditions text Process" , safe=False)