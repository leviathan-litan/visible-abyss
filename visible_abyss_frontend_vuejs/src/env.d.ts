/// <reference types="vite/client" />

declare module "*.vue" {
    import {DefineComponent} from "vue"
    const component: DefineComponent<{}, {}, any>
    export default component
}

interface ImportMetaEnv {
    readonly NODE_ENV: string,
    readonly VITE_APP_TITLE: string,
    readonly VITE_APP_PORT: number,
    readonly VITE_APP_BASE_API: string,
    readonly VITE_APP_BASE_URL: string,
    readonly VITE_APP_SERVICE_API: string,
}

interface ImportMeta {
    readonly env: ImportMetaEnv
}