import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: path.resolve(__dirname, 'static/js/dist'),
    emptyOutDir: true,
    rolldownOptions: {
      output: {
        dir: path.resolve(__dirname, 'static/js/dist'),
        entryFileNames: '[name].js',
      },
      input: {
        sidebar: path.resolve(__dirname, 'static/js/sidebar.js')
      }
    }
  }
})
