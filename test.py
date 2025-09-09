import time

from Tea.exceptions import TeaException
from alibabacloud_tea_openapi import models
from alibabacloud_aiearth_engine20220609.models import *
from alibabacloud_aiearth_engine20220609.client import Client

if __name__ == '__main__':
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

    try:
        # 查询公开数据
        list_data_request = ListDatasRequest()
        list_data_request.date_start = "2022-01-01"
        list_data_request.date_end = "2022-06-01"
        list_data_request.region_wkt = "POLYGON((115.5 39.5, 117.5 39.5, 117.5 40.5, 115.5 40.5, 115.5 39.5))"
        list_data_request.page_size = 20
        list_data_request.page_number = 1
        list_data_request.cloudage_max = 100
        list_data_request.cloudage_min = 0
        list_data_request.source_type_list = ['SENTINEL_GRD', 'SENTINEL_MSIL2A']

        data_list: ListDatasResponse = client.list_datas(list_data_request)
        print(data_list.body)

        # 查询用户发布的栅格数据
        # list_user_raster_datas_request = ListUserRasterDatasRequest()
        # list_user_raster_datas_request.page_size = 20
        # list_user_raster_datas_request.page_number = 1
        # list_user_raster_datas_request.name = '*'
        # list_user_raster_datas_request.from_type = 'personal'
        #
        # user_raster_list: ListUserRasterDatasResponse = client.list_user_raster_datas(list_user_raster_datas_request)
        # print(user_raster_list.body)
        #
        # # 查询用户发布的矢量数据
        # list_user_vector_datas_request = ListUserVectorDatasRequest()
        # list_user_vector_datas_request.page_size = 20
        # list_user_vector_datas_request.page_number = 1
        # list_user_vector_datas_request.from_type = 'personal'
        #
        # user_vector_list: ListUserRasterDatasResponse = client.list_user_vector_datas(list_user_vector_datas_request)
        # print(user_vector_list)
        #
        # # 查询用户发布的地图服务
        # list_user_map_service_datas_request = ListUserMapServiceDatasRequest();
        # list_user_map_service_datas_request.page_number = 1
        # list_user_map_service_datas_request.page_size = 20
        # list_user_map_service_datas_request.name = "test"
        # list_user_map_service_datas_response = client.list_user_map_service_datas(list_user_map_service_datas_request)
        # print(list_user_map_service_datas_response)
        #
        # # 下载数据
        # download_data_reqeust = DownloadDataRequest()
        # download_data_reqeust.data_id = "LT05_L2SP_113026_19840420_20200918_02_T1"
        # download_data_reqeust.band_no = ""
        # while not client.download_data(download_data_reqeust).body.finished:
        #     time.sleep(10)
        # else:
        #     download_url = client.download_data(download_data_reqeust).body.download_url
        #     print(download_url)
    except TeaException as e:
        # 打印整体的错误输出
        print(e)
        # 打印错误码
        print(e.code)
        # 打印错误信息，错误信息中包含
        print(e.message)
        # 打印服务端返回的具体错误内容
        print(e.data)