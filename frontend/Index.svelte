<svelte:options accessors={true} />

<script context="module" lang="ts">
  export { default as BaseExample } from "./Example.svelte";
</script>

<script lang="ts">
  import "./app.css";
  import type { Gradio } from "@gradio/utils";

  import { WebViewer } from "@rerun-io/web-viewer";
  import { onMount } from "svelte";

  import { Block } from "@gradio/atoms";
  import { StatusTracker } from "@gradio/statustracker";
  import type { FileData } from "@gradio/client";
  import type { LoadingStatus } from "@gradio/statustracker";

  export let elem_id = "";
  export let elem_classes: string[] = [];
  export let visible = true;
  export let height: number | string = 640;
  export let value: null | FileData[] | string[] = null;
  export let container = true;
  export let scale: number | null = null;
  export let min_width: number | undefined = undefined;
  export let loading_status: LoadingStatus;
  export let interactive: boolean;

  export let gradio: Gradio<{
    change: never;
    upload: never;
    clear: never;
    clear_status: LoadingStatus;
  }>;

  $: height = typeof height === "number" ? `${height}px` : height;

  $: value, gradio.dispatch("change");
  let dragging: boolean;
  let rr: WebViewer;
  let ref: HTMLDivElement;

  onMount(() => {
    rr = new WebViewer();
    rr.start(undefined, ref);
    return () => rr.stop();
  });

  $: if (value !== null && Array.isArray(value)) {
    for (const file of value) {
      if (typeof file !== "string") {
        if (file.url) {
          rr.open(file.url);
        }
      } else {
        rr.open(file);
      }
    }
  }
</script>

{#if !interactive}
  <Block
    {visible}
    variant={"solid"}
    border_mode={dragging ? "focus" : "base"}
    padding={false}
    {elem_id}
    {elem_classes}
    allow_overflow={false}
    {container}
    {scale}
    {min_width}
  >
    <StatusTracker
      autoscroll={gradio.autoscroll}
      i18n={gradio.i18n}
      {...loading_status}
      on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
    />
    <div class="viewer" bind:this={ref} style:height />
  </Block>
{/if}

<style>
  .viewer {
    width: 100%;
  }

  :global(div.viewer > canvas) {
    position: initial !important;
    top: unset !important;
  }
</style>
