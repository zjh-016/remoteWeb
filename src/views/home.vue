<template>
    <div>
        <a-space wrap>
            <a-button type="primary">Primary Button</a-button>
            <a-button>Default Button</a-button>
            <a-button type="dashed">Dashed Button</a-button>
            <a-button type="text">Text Button</a-button>
            <a-button type="link">Link Button</a-button>
        </a-space>
    </div>
</template>

<script>
export default {
    name: "index_page",
    mounted() {
        console.log("Home component mounted");
    }
};
</script>
<style></style>