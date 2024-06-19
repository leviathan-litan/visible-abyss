/**
 * 是否生成打爆报告
 */
import * as process from "process";

export default {}

export function isReportMode(): boolean {
    return process.env.REPORT === 'true'
}
