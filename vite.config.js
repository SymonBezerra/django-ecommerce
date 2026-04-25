import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: path.resolve(__dirname, 'static/dist'),
    emptyOutDir: true,
    rolldownOptions: {
      output: {
        dir: path.resolve(__dirname, 'static/dist'),
        entryFileNames: '[name].js',
        assetFileNames: '[name].[ext]',
        chunkFileNames: '[name].js',
      },
      input: {
        sidebar: path.resolve(__dirname, 'static/js/sidebar.js'),
        login: path.resolve(__dirname, 'home/static/home/js/login.js'),
      }
    }
  }
})
