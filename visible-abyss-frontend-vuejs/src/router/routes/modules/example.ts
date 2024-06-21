import type {AppRouteRecordRaw} from "../types";

const EXAMPLE: AppRouteRecordRaw = {
    path: '/example',
    name: 'example',
    children: [
        {
            path: 'about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('@/views/example/about/index.vue')
        },
        {
            path: 'pinia',
            name: 'pinia',
            component: () => import('@/views/example/pinia/index.vue')
        },
        {
            path: 'lang',
            name: 'lang',
            component: () => import('@/views/example/lang/index.vue')
        },
    ]
}

export default EXAMPLE