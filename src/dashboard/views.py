from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import pandas as pd
from RegexGenerator import RegexGenerator
import csv
import re
from datetime import datetime

from dashboard.forms import DocumentForm
from dashboard.models import Attribute, Document


def basicView(request):

    if request.method == "POST":
        repetitions = 1
        for i in range(repetitions):
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                createAttributes()

                if i == repetitions - 1:
                    return redirect("/data/")

    context = {}

    return render(request, "dashboard/main.html", context)


def dataView(request):

    allDocs = Document.objects.all().order_by("-uploaded_at")

    context = {
        "allDocs": allDocs,
    }

    return render(request, "dashboard/data.html", context)


def createAttributes():
    first_time = datetime.now()
    document = Document.objects.all().latest("uploaded_at")

    df = pd.read_csv(document.file.path)

    for column in df:
        regexList = set()
        regexCombination = ""

        for entry in range(int(len(df))):
            regexList.add(RegexGenerator(str(df[column].iloc[entry])).get_regex())

        print(len(regexList))

        regexList = sorted(regexList)

        max = 50
        for i, regex in enumerate(regexList):
            if i != 0 and i != len(regexList) and i != max:
                regexCombination += "|"
            regexCombination += regex

            if i == max - 1:
                break

        regexCombination = f"({regexCombination})"

        attribute = Attribute(
            document=document,
            name=column,
            type=df.dtypes[column],
            regex=regexCombination,
            security=69,
        )

        attribute.save()

    attributes = Attribute.objects.all()
    docAttributes = Attribute.objects.filter(document=document)
    for attribute in attributes:
        for docAttribute in docAttributes:
            if attribute is not docAttribute:
                if attribute.regex == docAttribute.regex:
                    pass

    later_time = datetime.now()
    difference = later_time - first_time

    document.executionTime = difference.total_seconds()
    document.save()


def downloadView(request):
    output = []
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    query_set = Document.objects.all()
    # Header
    writer.writerow(["id", "time"])
    for document in query_set:
        output.append(
            [
                document.id,
                document.executionTime,
            ]
        )
    # CSV Data
    writer.writerows(output)
    return response
