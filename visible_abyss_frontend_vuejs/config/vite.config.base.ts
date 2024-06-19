// ================== 导入

// ----- 组件
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
import svgLoader from "vite-svg-loader";

import Autoimport from "unplugin-auto-import/vite"
import Components from 'unplugin-vue-components/vite'

// ----- 组件（拆包）
// import {resolve, path} from "path";
import {resolve} from "path";

import {defineConfig, loadEnv} from "vite";
import {fileURLToPath, URL} from "node:url";

import {ArcoResolver} from "unplugin-vue-components/dist/resolvers";
import { vitePluginForArco } from "@arco-plugins/vite-vue";
import { createSvgIconsPlugin } from "vite-plugin-svg-icons";
import { viteMockServe } from "vite-plugin-mock";

// ----- 文件

// https://vitejs.dev/config/
export default defineConfig({
    base: "./",
    plugins: [
        vue(),
        vueJsx(),
        svgLoader({
            svgoConfig:{}
        }),
        Autoimport({
            resolvers: [
                ArcoResolver()
            ]
        }),
        Components({
            resolvers: [
                ArcoResolver({
                    sideEffect: true
                })
            ]
        }),
        vitePluginForArco({
            style: 'css'
        }),
        // Mock.JS
        viteMockServe({
            mockPath: "./mock/",
        }),
        // SVG图标
        createSvgIconsPlugin({
            // iconDirs: [path.resolve(process.cwd(), "src/assets/icons")],
            iconDirs: [
                resolve(__dirname, '../src/assets/icons'),
            ],
            symbolId: 'icon-[dir]-[name]',
        }),
    ],
    resolve: {
        alias: [
            // {
            //     find:'@',
            //     replacement: fileURLToPath(new URL('./src', import.meta.url))
            // },
            // {
            //     find:'assets',
            //     replacement: fileURLToPath(new URL('./src/assets', import.meta.url))
            // },

            {
                find:'@',
                replacement: resolve(__dirname, '../src')
            },
            {
                find:'assets',
                replacement: resolve(__dirname, '../src/assets')
            },
            {
                find:'vue-i18n',
                replacement: 'vue-i18n/dist/vue-i18n.cjs.js',
            },
            {
                find:'vue',
                replacement: 'vue/dist/vue.esm-bundler.js',
            },
        ],
        extensions: ['.ts', '.js'],
    },
    define: {
        'process.env': {},
    },
    css: {
        preprocessorOptions: {
            less: {
                modifyVars: {

                },
                javascriptEnabled: true,
            },
            scss: {
                prependData: ``,
                additionalData: ``,
            },
        },
    },
    server:{
        port: Number(process.env.VITE_APP_PORT),
    }
})
