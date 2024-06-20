// noinspection TypeScriptValidateTypes

import { mergeConfig, defineConfig, loadEnv } from "vite";
import baseConfig from "./vite.config.base"

export default defineConfig(({command, mode}) => {

    const env = loadEnv(mode, process.cwd(), '')

    const mergeBaseConfig = mergeConfig({
        mode: 'dev',
        plugins: [],
        server: {
            host: "0.0.0.0",
            port: Number(env.VITE_APP_PORT),
            open: false,
            fs: {
                strict: true,
            },
            proxy: {
                [env.VITE_APP_BASE_API]: {
                    target: env.VITE_APP_SERVICE_API,
                    changeOrigin: true,
                    // eslint-disable-next-line prettier/prettier
                    rewrite: (path) => path.replace(new RegExp("^" + env.VITE_APP_BASE_API), ""),
                },
            },
        },
    }, baseConfig)

    return mergeBaseConfig
})
