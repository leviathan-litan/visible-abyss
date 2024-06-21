<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
const { locale } = useI18n({
  useScope: "global"
})

function exchangeToZH() {
  locale.value = "zh-CN"
  console.log(t("menu.dashboard"))
}

function exchangeToEN() {
  locale.value = "en-US"
}
</script>
<template>

<!--  <el-input type="text" :placeholder="$t('title')" />-->
  <br/>
  <div>{{ t('menu.dashboard') }}</div>
  <a-button @click="exchangeToEN">英文模式</a-button>
  <a-button @click="exchangeToZH">中文模式</a-button>
</template>
<style scoped>
</style>
