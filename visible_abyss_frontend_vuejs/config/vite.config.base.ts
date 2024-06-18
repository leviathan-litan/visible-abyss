// ================== 导入

// ----- 组件
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
import svgLoader from "vite-svg-loader";

// ----- 组件（拆包）
import {resolve} from "path";
import {defineConfig} from "vite";
import {fileURLToPath, URL} from "node:url";

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
            }
        }
    }
})
