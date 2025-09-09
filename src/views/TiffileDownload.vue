<template>
    <div>
        <a-card>
            <a-page-header title="数据下载" @back="() => $router.go(-1)">
                <template #tags>
                    <a-tag color="blue">running</a-tag>
                </template>
                <template #extra>
                    <a-button key="1" type="primary" @click="showModel">查询公开数据集</a-button>
                </template>
                <a-row type="flex">
                    <a-statistic title="LandSat" :value="0" />
                    <a-statistic title="Sentinel" :value="0" :style="{
                        margin: '0 32px',
                    }" />
                    <a-statistic title="MODIS" :value="0" />
                </a-row>
            </a-page-header>
        </a-card>
        <br />
        <a-row>
            <a-col :span="24">
                <a-card>
                    <a-table :columns="columns"> </a-table>
                </a-card>
            </a-col>
        </a-row>

        <a-modal v-model:visible="visible" :width="640" title="查询公开数据集" :footer="null">
            <SearchDataForm @searchParams="searchRemData" />
        </a-modal>
    </div>
</template>

<script>
import SearchDataForm from '@/components/form/searchDataForm.vue';

export default {
    name: "remoteData",
    components: {
        SearchDataForm
    },
    data() {
        return {
            modalText: '111111',
            visible: false,
            confirmLoading: false,
            columns: [
                {
                    title: "开始日期",
                    dataIndex: "AcquisitionDateRangeStart",
                    key: "AcquisitionDateRangeStart",
                    width: 100
                },
                {
                    title: "结束日期",
                    dataIndex: "AcquisitionDateRangeEnd",
                    key: "AcquisitionDateRangeEnd",
                    width: 100
                },
                {
                    title: "Bands",
                    children: [
                        {
                            title: "BandNo",
                            dataIndex: "BandNo",
                            width: 100
                        },
                        {
                            title: "Resolution",
                            dataIndex: "Resolution",
                            width: 100
                        },
                        {
                            title: "Width",
                            dataIndex: "Width",
                            width: 100
                        },
                        {
                            title: "Height",
                            dataIndex: "Height",
                            width: 100
                        },
                    ]
                },
                {
                    title: "Bbox",
                    dataIndex: "Bbox",
                    width: 100
                },
                {
                    title: "CloudCoverage",
                    dataIndex: "CloudCoverage",
                    width: 100
                },
                {
                    title: "Name",
                    dataIndex: "Name",
                    width: 100
                },
                {
                    title: "SourceType",
                    dataIndex: "SourceType",
                    width: 100
                },
                {
                    title: "StacId",
                    dataIndex: "StacId",
                    width: 100
                },
            ]
        }
    },
    mounted() {
        console.log("Remote Data component mounted");
    },
    methods: {
        showModel() {
            this.visible = true
        },
        searchRemData(data) {
            console.log("父组件：")
            console.log(data)
        },
        handleOk() {
            this.modalText = 'The modal will be closed after two seconds';
            this.confirmLoading = true;
            setTimeout(() => {
                this.visible = false;
                this.confirmLoading = false;
            }, 2000)
        }

    }
}
</script>
<style></style>