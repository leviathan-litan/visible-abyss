// ================== 导入

// ----- 组件
import {mergeConfig, defineConfig, loadEnv} from "vite";

// ----- 文件
import baseConfig from "./vite.config.base"

// ================== 配置：融合（mergeConfig）
export default mergeConfig(
    {
        // 需要在项目的根目录下包含相应的文件「.env.dev」
        mode: "dev",
        server: {
            // 服务运行后自动打开首页
            open: true,
            // 服务器地址
            // host: '0.0.0.0',
            host: '0.0.0.0',
            // 服务器端口
            // port: Number(env.VITE_APP_PORT),
            // port: Number(process.env.VITE_APP_PORT),
            port: 3000,
            fs: {
                strict: true,
            },
            // 反向代理
            // proxy: {
            //     [env.VITE_APP_BASE_API]: {
            //         target: env.VITE_APP_SERVICE_API,
            //         changeOrigin: true,
            //         // eslint-disable-next-line prettier/prettier
            //         rewrite: (path) => path.replace(new RegExp("^" + env.VITE_APP_BASE_API), ""),
            //     },
            // }
        },
        plugins: [
            // 插件
        ],
    },
    baseConfig,
)