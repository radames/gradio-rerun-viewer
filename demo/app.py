import gradio as gr
from gradio_rerun import Rerun


example = Rerun().example_value()


def predict(url: str, file_path: str | list[str] | None):
    if url:
        return url
    return file_path


with gr.Blocks(css=".gradio-container { max-width: unset!important; }") as demo:
    with gr.Row():
        with gr.Column():
            with gr.Group():
                file_path = gr.File(file_count="multiple", type="filepath")
                url = gr.Text(
                    info="Or use a URL",
                    label="URL",
                )
        with gr.Column():
            pass
    btn = gr.Button("Run", scale=0)
    with gr.Row():
        rerun_viewer = Rerun(height=900)

    inputs = [file_path, url]
    outputs = [rerun_viewer]

    gr.on([btn.click, file_path.upload], fn=predict, inputs=inputs, outputs=outputs)

    gr.Examples(
        examples=[
            [
                None,
                "https://app.rerun.io/version/0.15.1/examples/detect_and_track_objects.rrd",
            ],
            [
                ["./examples/rgbd.rrd"],
                None,
            ],
            [
                ["./examples/rrt-star.rrd"],
                None,
            ],
            [
                ["./examples/structure_from_motion.rrd"],
                None,
            ],
            [
                ["./examples/structure_from_motion.rrd", "./examples/rrt-star.rrd"],
                None,
            ],
        ],
        fn=predict,
        inputs=inputs,
        outputs=outputs,
    )

if __name__ == "__main__":
    demo.launch()
