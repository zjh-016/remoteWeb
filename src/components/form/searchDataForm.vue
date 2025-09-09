<template>
    <a-form :model="formState" name="basic" :label-col="{ span: 4 }" :wrapper-col="{ span: 16 }" @finish="onFinish"
        @finishFailed="onFinishFailed">
        <a-form-item label="区域" name="region" :rules="[{ required: true, message: '请输入你要查询的地区!' }]">
            <a-select v-model:value="formState.region" :options="options" style="width: 200px"
                @change="handleRegionChange"></a-select>
        </a-form-item>

        <a-form-item label="日期" name="dateRange" :rules="[{ required: true, message: '请选择你要查询的日期!' }]">
            <a-range-picker v-model:value="formState.dateRange" :format="dateFormat">
                <template #dateRender="{ current }">
                    <div class="ant-picker-cell-inner" :style="getCurrentStyle(current)">
                        {{ current.date() }}
                    </div>
                </template>
            </a-range-picker>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 4, span: 16 }">
            <a-button type="primary" html-type="submit">Submit</a-button>
        </a-form-item>
    </a-form>
</template>

<script>
import { getAction } from '@/request/request';
export default {
    emits: ['onFinish'],
    data() {
        return {
            dateFormat: 'YYYY-MM-DD',
            formState: {
                region: '',      // 区域选择值
                dateRange: [],   // 日期范围值
            },
            options: [
                {
                    label: 'Manager',
                    options: [
                        { value: 'jack', label: 'Jack' },
                        { value: 'lucy', label: 'Lucy' }
                    ]
                },
                {
                    label: 'Engineer',
                    options: [
                        { value: 'yiminghe', label: 'Yiminghe' }
                    ]
                }
            ],

        }
    },
    created() {
        this.getRegion()
    },
    methods: {
        onFinish() {
            console.log('选中的区域:', this.formState.region);
            console.log('日期范围:', this.formState.dateRange);
            var i = 0;
            var dateRange = []
            for (i = 0; i < this.formState.dateRange.length; i++) {
                dateRange.push(this.formState.dateRange[i].format(this.dateFormat))
            }
            console.log("格式化后的日期： ", dateRange)
            var resObj = {
                region: this.formState.region,
                dateRange: dateRange
            }
            this.$emit('searchParams', resObj)
            console.log("emit")
        },

        onFinishFailed(errorInfo) {
            console.log(errorInfo)
            return false
        },
        getCurrentStyle(current) {
            const style = {};
            if (current.date() === 1) {
                style.border = '1px solid #1890ff';
                style.borderRadius = '50%';
            }
            return style;
        },
        handleRegionChange(value) {
            console.log(value)
        },
        getRegion() {
            getAction('/data/getRegion').then(response => {
                console.log(response.data)
                this.options = response.data
            })
        },

    }
};
</script>

<style></style>