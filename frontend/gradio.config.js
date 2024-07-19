import tailwindcss from "@tailwindcss/vite";
import wasm from "vite-plugin-wasm";

// `@rerun-io/web-viewer` uses `new URL("./re_viewer_bg.wasm", import.meta.url)` since 0.17,
// which does not play well with `vite dev`: https://github.com/rerun-io/rerun/issues/6815
// we need to patch the config, but `gradio` does not let us directly set the `optimize` option.
/** @type {() => import("vite").Plugin} */
const hack = () => ({
  config() {
    return {
      optimizeDeps: {
        exclude: process.env.NODE_ENV === "production" ? [] : ["@rerun-io/web-viewer"],
      },
    };
  },
});

export default {
  plugins: [wasm(), tailwindcss(), hack()],
  svelte: {
    preprocess: [],
  },
  build: {
    target: "esnext",
  },
};

