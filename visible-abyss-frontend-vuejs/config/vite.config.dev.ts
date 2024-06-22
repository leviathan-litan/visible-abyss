import {mergeConfig,defineConfig,loadEnv} from 'vite';
import baseConfig from './vite.config.base'

export default defineConfig(({mode, command}) => {

    const env = loadEnv(mode, process.cwd())

    return mergeConfig(
        {
            mode: 'dev',
            server: {
                open: false,
                host: '0.0.0.0',
                port: Number(env.VITE_PORT),
                fs: {
                    strict: true,
                },
            },
            plugins: [],
        },
        baseConfig,
    )
})
