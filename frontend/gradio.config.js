import tailwindcss from "@tailwindcss/vite";
import wasm from "vite-plugin-wasm";

export default {
  plugins: [wasm(), tailwindcss()],
  svelte: {
    preprocess: [],
  },
};
