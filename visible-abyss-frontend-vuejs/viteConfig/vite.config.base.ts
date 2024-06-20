import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

import {resolve} from 'path'
import svgLoader from 'vite-svg-loader'

// https://vitejs.dev/config/
export default defineConfig({
    base: "./",
    plugins: [
        vue(),
        vueJsx(),
        svgLoader({
            svgoConfig: {}
        }),
    ],
    resolve: {
        // Version 1
        // alias: {
        //     '@': fileURLToPath(new URL('./src', import.meta.url)),
        //     'assets': fileURLToPath(new URL('./src/assets', import.meta.url)),
        //     'vue-i18n': "vue-i18n/dist/vue-i18n.cjs.js",
        //     'vue': "vue/dist/vue.esm-bundler.js",
        // }

        // Version 2
        alias: [
            {
                find: '@',
                replacement: resolve(__dirname, '../src'),
            },
            {
                find: 'assets',
                replacement: resolve(__dirname, '../src/assets'),
            },
            {
                find: 'vue-i18n',
                replacement: "vue-i18n/dist/vue-i18n.cjs.js",
            },
            {
                find: 'vue',
                replacement: "vue/dist/vue.esm-bundler.js",
            },
        ],
        extensions: [
            '.ts',
            '.js',
        ]
    },
    define: {
        'process.env': {},
    },
    css: {
        preprocessorOptions: {
            scss: {
                prependData: ``,
                additionalData: ``,
            },
            less: {
                modifyVars: {},
                javascriptEnabled: true,
            },
        },
    },
})
