import json

from django.shortcuts import render

# Create your views here.

def webpage(request):
    context['object_list'] = article.objects.filter(title__icontains=request.GET.get('search'))
    return render(request,"index.html",context)

import pyodbc
import pandas as pd
import pandas.io.formats.style

from django.http import HttpResponse
from django.utils.translation import gettext


# Synapse dev
from matplotlib import widgets, interactive

server = 'synappoc-db.database.windows.net'
database = 'synapPOC'
username = 'Appadmin'
password = 'App1234#'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(driver=driver,
                        server=server,
                        database=database,
                        uid=username, pwd=password)
crsr = conn.cursor()


def home(request):
    print("COMMIMNF TO DATA")
    df = pd.read_sql(
        "select * from INFORMATION_SCHEMA.columns as meta, IRM.DataCatalogue as cat where lower(meta.table_name+meta.column_name) = lower(cat.tablename+cat.fieldname)",conn)


    df = df[['TABLE_CATALOG', 'TABLE_SCHEMA', 'TABLE_NAME', 'COLUMN_NAME', 'ORDINAL_POSITION', 'COLUMN_DEFAULT', 'IS_NULLABLE', 'DATA_TYPE', 'CHARACTER_MAXIMUM_LENGTH', 'CHARACTER_OCTET_LENGTH', 'NUMERIC_PRECISION', 'NUMERIC_PRECISION_RADIX', 'NUMERIC_SCALE', 'DATETIME_PRECISION', 'CHARACTER_SET_CATALOG', 'CHARACTER_SET_SCHEMA',
             'CHARACTER_SET_NAME', 'COLLATION_CATALOG', 'COLLATION_SCHEMA', 'COLLATION_NAME', 'DOMAIN_CATALOG', 'DOMAIN_SCHEMA', 'DOMAIN_NAME', 'TableType', 'TableName', 'FieldName', 'DataType', 'FieldNameDescription',
             'SampleData', 'ActualSource', 'LastUpdatedDate', 'ReviewedBy', 'ApprovedBy', 'ReviewedDate', 'ApprovedDate', 'Tagstosearchthedata', 'sourceobjectname',
             'sourcefieldname', 'targettransformation']]


    json_records = df.reset_index().to_json(orient ='records')
    arr = []
    arr = json.loads(json_records)

    contextt = {'d': arr}
    return render(request,'test2.html',contextt)


def extend1(request):
    #do something

    context =  {'d': "arr"}
    return render(request,'frame_1.html',context)

def extend2(request):
    #do something
    template = 'frame_2.html'
    context =  {'d': "arr"}
    return render(request,'frame_2.html',context)

def extend3(request):
    df = pd.read_sql(
        "select * from INFORMATION_SCHEMA.columns as meta, IRM.DataCatalogue as cat where lower(meta.table_name+meta.column_name) = lower(cat.tablename+cat.fieldname)",
        conn)

    df = df[['TABLE_CATALOG', 'TABLE_SCHEMA', 'TABLE_NAME', 'COLUMN_NAME', 'ORDINAL_POSITION', 'COLUMN_DEFAULT',
             'IS_NULLABLE', 'DATA_TYPE', 'CHARACTER_MAXIMUM_LENGTH', 'CHARACTER_OCTET_LENGTH', 'NUMERIC_PRECISION',
             'NUMERIC_PRECISION_RADIX', 'NUMERIC_SCALE', 'DATETIME_PRECISION', 'CHARACTER_SET_CATALOG',
             'CHARACTER_SET_SCHEMA',
             'CHARACTER_SET_NAME', 'COLLATION_CATALOG', 'COLLATION_SCHEMA', 'COLLATION_NAME', 'DOMAIN_CATALOG',
             'DOMAIN_SCHEMA', 'DOMAIN_NAME', 'TableType', 'TableName', 'FieldName', 'DataType', 'FieldNameDescription',
             'SampleData', 'ActualSource', 'LastUpdatedDate', 'ReviewedBy', 'ApprovedBy', 'ReviewedDate',
             'ApprovedDate', 'Tagstosearchthedata', 'sourceobjectname',
             'sourcefieldname', 'targettransformation']]

    json_records = df.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_records)

    contextt = {'d': arr}
    return render(request,'frame_3.html',contextt)


def extend4(request):
    df = pd.read_sql(
        "select * from INFORMATION_SCHEMA.columns as meta, IRM.DataCatalogue as cat where lower(meta.table_name+meta.column_name) = lower(cat.tablename+cat.fieldname)",
        conn)

    df = df[['TABLE_CATALOG', 'TABLE_SCHEMA', 'TABLE_NAME', 'COLUMN_NAME', 'ORDINAL_POSITION', 'COLUMN_DEFAULT',
             'IS_NULLABLE', 'DATA_TYPE', 'CHARACTER_MAXIMUM_LENGTH', 'CHARACTER_OCTET_LENGTH', 'NUMERIC_PRECISION',
             'NUMERIC_PRECISION_RADIX', 'NUMERIC_SCALE', 'DATETIME_PRECISION', 'CHARACTER_SET_CATALOG',
             'CHARACTER_SET_SCHEMA',
             'CHARACTER_SET_NAME', 'COLLATION_CATALOG', 'COLLATION_SCHEMA', 'COLLATION_NAME', 'DOMAIN_CATALOG',
             'DOMAIN_SCHEMA', 'DOMAIN_NAME', 'TableType', 'TableName', 'FieldName', 'DataType', 'FieldNameDescription',
             'SampleData', 'ActualSource', 'LastUpdatedDate', 'ReviewedBy', 'ApprovedBy', 'ReviewedDate',
             'ApprovedDate', 'Tagstosearchthedata', 'sourceobjectname',
             'sourcefieldname', 'targettransformation']]

    json_records = df.reset_index().to_json(orient='records')
    arr = []
    arr = json.loads(json_records)

    contextt = {'d': arr}
    return render(request,'frame_4.html',contextt)



