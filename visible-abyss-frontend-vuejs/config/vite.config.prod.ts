import {mergeConfig} from "vite";
import baseConfig from './vite.config.base'

import configCompressPlugin from './plugin/compress';
import configVisualizerPlugin from './plugin/visualizer';
import configArcoResolverPlugin from './plugin/arcoResolver';

export default mergeConfig(
    {
        mode: 'production',
        plugins: [
            configCompressPlugin('gzip', true),
            configVisualizerPlugin(),
            configArcoResolverPlugin(),
        ],
        build: {
            rollupOptions: {
                input: {
                    main: './src/index.html',
                    about: './src/about.html',
                    contact: './src/contact.html'
                },
                output: {
                    manualChunks: {
                        arco: ['@arco-design/web-vue'],
                        chart: ['echarts', 'vue-echarts'],
                        vue: [
                            'vue',
                            'vue-router',
                            'vuex',
                            'vue-i18n',
                            'pinia',
                            '@vueuse/core',
                        ]
                    },
                },
            },
            chunkSizeWarningLimit: 2000,
        },
    },
    baseConfig
)