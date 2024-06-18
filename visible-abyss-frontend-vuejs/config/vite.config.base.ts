import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

import { resolve } from 'path'
import { defineConfig } from 'vite'

import svgLoader from 'vite-svg-loader'

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'

import {ArcoResolver} from 'unplugin-vue-components/resolvers'
import {vitePluginForArco} from '@arco-plugins/vite-vue'

export default defineConfig({
  base: './',
  plugins: [
    vue(),
    vueJsx(),
    svgLoader({
      svgoConfig: {}
    }),
    vitePluginForArco({
      style: 'css'
    }),
    AutoImport({
      resolvers: [
        ArcoResolver()
      ],
    }),
    Components({
      resolvers: [
        ArcoResolver({
          sideEffect: true,
        }),
      ]
    }),
  ],
  resolve: {
    alias: [
      {
        find: '@',
        replacement: resolve(__dirname, '../src'),
      },
      {
        find: 'assets',
        replacement: resolve(__dirname, '../src/assets'),
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
      less: {
        modifyVars: {

        },
        javascriptEnabled: true,
      },
    },
  },
})
