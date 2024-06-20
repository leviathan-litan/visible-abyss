<template>
  <div>
    <h3>「Pinia」计数器的实例</h3>
    <a-space>
      <a-button type="outline" status="success" shape="round" @click="increment">{{count}}</a-button>
      <span>「doubleCount」：{{doubleCount}}</span>
    </a-space>
  </div>
</template>

<script setup lang="ts">
import {toRefs} from "vue";

import {useCounterStore} from "@/stores";

const counter = useCounterStore()

const {count,doubleCount} = toRefs(counter)
const {increment} = counter
</script>

<style scoped>

</style>