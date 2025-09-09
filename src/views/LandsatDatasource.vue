<template>
    <div>
        <a-card>
            <a-page-header title="LandSat" sub-title="LandSat 系列卫星" @back="() => $router.go(-1)">
                <template #tags>
                    <a-tag color="green">启用</a-tag>
                </template>
                <template #extra>
                    <a-button key="1" type="primary">选择数据集</a-button>
                </template>
                <a-row type="flex">
                    <a-statistic title="卫星状态" value="正常" />
                    <a-statistic title="数量" :value="5" :style="{
                        margin: '0 32px',
                    }" />
                    <a-statistic title="已退役" :value="1" />
                </a-row>
            </a-page-header>
        </a-card>
        <br />
        <a-row>
            <a-col :span="8" v-for="item in remoteData" :key="item.satellite_code">
                <a-tooltip :title="item.satellite_info">
                    <a-card hoverable class="text-container">
                        <template #cover>
                            <img :alt="item.satellite_name" :src="item.src_url" />
                        </template>
                        <a-card-meta :title="item.satellite_name">
                            <template #description>{{ item.satellite_info }}</template>
                        </a-card-meta>
                    </a-card>
                </a-tooltip>
            </a-col>
        </a-row>
    </div>
</template>

<script>
import { getAction } from '../request/request.js'
export default {
    name: "index_page",
    data() {
        return {
            remoteData: []
        }
    },
    mounted() {
        console.log("Remote Data component mounted");
        this.getLandSatData()
    },
    created() {

    },
    methods: {
        getLandSatData() {
            getAction('/data/getLandsatData').then(response => {
                this.remoteData = response.data
                console.log(this.remoteData.length)
                console.log(this.remoteData)
            })
        }

    }
};
</script>
<style scoped>
.text-container {
    margin-bottom: 50px;
    max-width: 240px;
    /* 根据需要设置最大宽度 */
    max-height: 500px;
    /* 根据需要设置最大高度 */
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    /* 设置要显示的行数 */
    -webkit-box-orient: vertical;
}

.demo-page-header :deep(tr:last-child td) {
    padding-bottom: 0;
}
</style>