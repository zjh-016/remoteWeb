import json
import aie
from flask import Blueprint, jsonify, send_file, request
from config import getDbConnection
from Tea.exceptions import TeaException
from alibabacloud_tea_openapi import models
from alibabacloud_aiearth_engine20220609.models import *
from alibabacloud_aiearth_engine20220609.client import Client

data_bp = Blueprint('data', __name__)

config = models.Config(
    # 您的AccessKey ID,
    access_key_id='LTAI5tCWaMjpsorqhZXig7VX',
    # 您的AccessKey Secret,
    access_key_secret='8ot9G6JOpT13COAxZ4zHLrtsVxGB2Q',
    # 地域ID
    region_id='cn-hangzhou',
    # 访问的域名
    endpoint='aiearth-engine.cn-hangzhou.aliyuncs.com'
)

client = Client(config)

conn = getDbConnection()

@data_bp.route('/getLandsatData', methods=['GET', 'POST'])
def getLandsatData():
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM rem_satellite_data')
            result = cursor.fetchall()
    finally:
        print('success')
    return jsonify(result)


@data_bp.route('/getMap', methods=['GET', 'POST'])
def landsat5C2L2Map():
    try:
        aie.Authenticate(token='ea8ba5d60f89f3f0975418aaf161eea9')  # 确保已配置阿里云 AK/SK
        aie.Initialize()

        # 定义区域
        feature_collection = aie.FeatureCollection('China_Province') \
            .filter(aie.Filter.eq('province', '浙江省'))
        geometry = feature_collection.geometry()

        # 获取影像集合并转换为单张 Image
        dataset = aie.ImageCollection('LANDSAT_LC08_C02_T1_L2') \
            .filterBounds(geometry) \
            .filterDate('2018-10-01', '2018-10-31') \
            .filter(aie.Filter.lte('eo:cloud_cover', 10.0)) \
            .limit(10)

        # # 生成缩略图 URL
        # vis_params = {
        #     'bands': ['SR_B4', 'SR_B3', 'SR_B2'],
        #     'min': 8000,
        #     'max': 13000,
        # }
        # thumb_url = image.get_thumb_URL({
        #     'visParams': vis_params,
        #     'dimensions': 800,
        #     'region': geometry
        # })

        return send_file(dataset, mimetype='image/png')

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@data_bp.route('/getRegion', methods=['GET', 'POST'])
def getRegion():
    sql = "SELECT max(id) as id, max(province) as province,city,max(county) as county from rem_region WHERE county is null and city is not null GROUP BY city ORDER BY id"
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            province = ''
            options = []
            res = []
            for obj in result:
                resDict = {}
                if(obj['province'] == province):
                    options.append({'label': obj['city'], 'value': obj['id']})
                elif(obj['province'] != province):
                    resDict['label'] = province
                    province = obj['province']
                    resDict['options'] = options
                    options = []
                    options.append({'label': obj['city'], 'value': obj['id']})
                    if(resDict['label'] != ""):
                        res.append(resDict)
    finally:
        print(' getRegion success')


    return jsonify(res)

@data_bp.route('/searchDataSource', methods=['GET', 'POST'])
def searchDataSource():
    dateStart = request.form.get('dateStart')
    dateEnd = request.form.get('dateEnd')

    try:
        # 查询公开数据
        list_data_request = ListDatasRequest()
        list_data_request.date_start = "2022-01-01"
        list_data_request.date_end = "2022-06-01"
        list_data_request.region_wkt = ""
        list_data_request.page_size = 20
        list_data_request.page_number = 1
        list_data_request.cloudage_max = 100
        list_data_request.cloudage_min = 0
        list_data_request.source_type_list = ['SENTINEL_GRD', 'SENTINEL_MSIL2A']

        data_list: ListDatasResponse = client.list_datas(list_data_request)
        return jsonify(data_list.body)
    finally:
        print(data_list.body)