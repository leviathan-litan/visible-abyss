import {App} from 'vue'
import permissions from './permission'

export default {
    install(Vue: App) {
        Vue.directive('permission', permissions);
    },
};