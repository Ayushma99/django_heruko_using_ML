from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from . form import approvalform
from . models import approval
from . serializers import api
from sklearn.externals import joblib
import pandas as pd
from keras.models import load_model
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Create your views here.
class viewapprove(viewsets.ModelViewSet):
    queryset=approval.objects.all()
    serializer_class=api

def ohevalue(df):
    ohe_col=joblib.load(os.path.join(BASE_DIR, "ohe.pkl"))
    cat_col=["Gender","Married","Education","Self_Employed","Property_Area"]
    df_new=pd.get_dummies(df,columns=cat_col)
    new_dict={}
    for i in ohe_col:
        if i in df_new.columns:
            new_dict[i]=df_new[i].values
        else:
            new_dict[i]=0
    newdf=pd.DataFrame(new_dict)
    return newdf

# @api_view(['POST'])
def approvereject(unit):
    try:
        model=load_model(os.path.join(BASE_DIR, "loan_model.h5"))
        scale=joblib.load(os.path.join(BASE_DIR,"scale.pkl"))
        # mydata=request.data
        # unit=np.array(list(mydata.values()))
        # unit=unit.reshape(1,-1)
        X=scale.transform(unit)
        y_pred=model.predict(X)
        y_pred=y_pred>0.5
        dfs=pd.DataFrame(y_pred,columns=["Status"])
        dfs=dfs.replace({True:"Approved",False:"Rejected"})
        return ('Your status is {}'.format(dfs["Status"].values[0]))
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def cform(request):
    if request.method=="POST":
        form=approvalform(request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data["Firstname"]
            Lastname=form.cleaned_data["Lastname"]
            Dependents=form.cleaned_data["Dependents"]
            ApplicantIncome=form.cleaned_data["ApplicantIncome"]
            CoapplicantIncome=form.cleaned_data["CoapplicantIncome"]
            LoanAmount=form.cleaned_data["LoanAmount"]
            Loan_Amount_Term=form.cleaned_data["Loan_Amount_Term"]
            Credit_History=form.cleaned_data["Credit_History"]
            Gender=form.cleaned_data["Gender"]
            Married=form.cleaned_data["Married"]
            Education=form.cleaned_data["Education"]
            Self_Employed=form.cleaned_data["Self_Employed"]
            Property_Area=form.cleaned_data["Property_Area"]
            myDict=(request.POST).dict()
            df=pd.DataFrame(myDict,index=[0])
            status=approvereject(ohevalue(df))
            if int(df["LoanAmount"])<200000:
                messages.success(request,"Application Status : {}".format(status))
            else:
                messages.success(request,"Your Loan Request exceeds Rs. 2,00,000. Make small loan request.")
    form=approvalform()
    return render(request,"Myapi/form.html",{"form":form})
