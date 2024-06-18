// ================== 导入

// ----- 组件
import {mergeConfig, loadEnv} from "vite";

// ----- 文件：基础配置文件
import baseConfig from "./vite.config.base"

// ----- 文件：其他配置文件

// ================== 配置
export default mergeConfig({
        // 需要在项目的根目录下包含相应的文件「.env.prod」
        mode: "prod",
        plugins: [
            // 插件
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
                },
            },
            minify: 'esbuild',
            target: 'es2015',
            sourcemap: false,
        },
    },
    baseConfig,
)