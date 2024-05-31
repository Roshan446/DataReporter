from django.shortcuts import render, redirect
from django.views import View
from report.models import ExcelFile, Report
from datetime import datetime
from django.db.models import Sum, Count
import pandas as pd
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class ImportFileView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"index.html")
    def post(self, request, *args, **kwargs):
        file = request.FILES["file"]
        excel_obj = ExcelFile.objects.create(file=file)
        path = str(excel_obj.file.path)
        d =pd.read_excel(path)
        for colums, rows  in d.iterrows():
            date = rows["Date"]
            date_obj = datetime.strptime(date, "%d-%m-%Y")
            formated_date = date_obj.strftime("%Y-%m-%d")
            
            Report.objects.create(
                   date = formated_date,
                    accno = rows["ACCNO"],
                    cust_state =rows["Cust State"],
                    cust_pin =rows["Cust Pin"] ,
                    dpd = rows["DPD"],
 
            )
        messages.success(request, "your reportfile has been saved")
            
            
        return render(request, 'success.html')
    


class ExportTxt(View):
    def get(self, request, *args, **kwargs):
        report_obj = Report.objects.all()


        data_count = report_obj.values("cust_state", "dpd").annotate(count = Count("id"))

        data =[]
        for d in data_count:
      
           data.append(
           {
                "cust_state": d.get("cust_state"),
                "DPD": d.get("dpd"),
                "count": d.get("count")})
        df =pd.DataFrame(data).to_csv("report.csv", index=False)
        report_obj.delete()
        return redirect('import')
    