import {App} from 'vue'

// 导入：eCharts
import {use} from 'echarts/core'

import {CanvasRenderer} from 'echarts/renderers'

import {
    PieChart,
    LineChart,
    BarChart,
    MapChart,
    GaugeChart,
    PieSeriesOption,
    LineSeriesOption,
    BarSeriesOption,
    MapSeriesOption,
    GaugeSeriesOption
} from 'echarts/charts'

import {
    TitleComponent,
    TooltipComponent,
    GridComponent,
    LegendComponent,
    DataZoomComponent
} from 'echarts/components'

use([
    CanvasRenderer,
    PieChart,
    LineChart,
    BarChart,
    MapChart,
    GaugeChart,
    TitleComponent,
    TooltipComponent,
    GridComponent,
    LegendComponent,
    DataZoomComponent,
])

// import Chart from './chart/index.vue';
// import Breadcrumb from './breadcrumb/index.vue';

export default {
    install(Vue: App) {
        // Vue.component('Chart', Chart);
        // Vue.component('Breadcrumb', Breadcrumb);
    },
};