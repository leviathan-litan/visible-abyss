/** @type {import('tailwindcss').Config} */
export default {
  content: [
      "./src/**/*.{html,js,ts,jsx,tsx,vue}"
  ],
  theme: {
    extend: {
      colors: {
        // 'primary': '#0F172A',
        'primary': {
          DEFAULT: '#1E3A8A',
          '50': '#E2E8F0',
          '100': '#CBD5E0',
          '200': '#94A3B8',
          '300': '#64748B',
          '400': '#475569',
          '500': '#334155',
          '600': '#1E293B',
          '700': '#0F172A',
          '800': '#0E7490',
          '900': '#0E7490',
        },
        // 'secondary': '#1E293B',
        'secondary': {
          DEFAULT: '#1E293B',
          '50': '#E2E8F0',
          '100': '#CBD5E0',
          '200': '#94A3B8',
          '300': '#64748B',
          '400': '#475569',
          '500': '#334155',
          '600': '#1E293B',
          '700': '#0F172A',
          '800': '#0E7490',
          '900': '#0E7490',
        },
        'tertiary': '#1E3A8A',
        'quaternary': '#1E3A8A',
        'quinary': '#1E3A8A',
        'senary': '#1E3A8A',
        'septenary': '#1E3A8A',
        'octonary': '#1E3A8A',
        'nonary': '#1E3A8A',
      }
    },
  },
  plugins: [],
}

