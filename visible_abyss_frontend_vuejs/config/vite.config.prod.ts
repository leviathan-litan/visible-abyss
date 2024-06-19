// ================== 导入

// ----- 组件
import {mergeConfig, loadEnv} from "vite";

// ----- 文件：基础配置文件
import baseConfig from "./vite.config.base"

// ----- 文件：其他配置文件
import configArcoResolverPlugin from "./plugin/arcoResolver";
import configCompressPlugin from "./plugin/compress";
import configVisualizerPlugin from "./plugin/visualizer";

// ================== 配置
export default mergeConfig({
        // 需要在项目的根目录下包含相应的文件「.env.prod」
        mode: "prod",
        plugins: [
            // 插件
            configCompressPlugin('gzip'),
            configVisualizerPlugin(),
            configArcoResolverPlugin(),
        ],
        build: {
            chunkSizeWarningLimit: 20480,
            reportCompressedSize: false,
            rollupOptions: {
                onwarn: () => {},
                output: {
                    chunkFileNames: "static/js/[name]-[hash].js",
                    entryFileNames: "static/js/[name]-[hash].js",
                    assetFileNames: "static/[ext]/[name]-[hash].[ext]",

                    // 分包
                    manualChunks(id) {
                        if (id.includes('node_modules')) {
                            return id.toString().split('node_modules/')[1].split('/')[0].toString()
                        }
                    }
                },
            },
            minify: 'esbuild',
            target: 'es2015',
            sourcemap: false,
        },
    },
    baseConfig,
)
