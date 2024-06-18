/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#31343d',
          200: '#9e9e9e',
          300: '#212329',
          700: '#101114',
        },
        secondary: {
          100: '#e2e2d5',
          200: '#888883',
        },
      },
    },
  },
  plugins: [],
}

