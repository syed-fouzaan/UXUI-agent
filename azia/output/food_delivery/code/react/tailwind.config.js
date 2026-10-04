/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: '#EA580C',
        'primary-hover': '#C2410C',
        secondary: '#4F46E5',
        accent: '#F59E0B',
        background: '#FAFAF9',
        surface: '#FFFFFF',
        border: '#E7E5E4',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
