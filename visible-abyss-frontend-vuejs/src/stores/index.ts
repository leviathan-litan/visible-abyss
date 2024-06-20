import { createPinia } from "pinia";

import {useCounterStore} from "@/stores/modules/counter";

const pinia = createPinia()

export {
    useCounterStore,
}

export default pinia
