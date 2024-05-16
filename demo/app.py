import rerun as rr
import rerun.blueprint as rrb
import gradio as gr
from gradio_rerun import Rerun
import time
import cv2


@rr.thread_local_stream("rerun_example_streaming_blur")
def repeated_blur(img):
    stream = rr.binary_stream()

    blueprint = rrb.Blueprint(
        rrb.Horizontal(
            rrb.Spatial2DView(origin="image/original"),
            rrb.Spatial2DView(origin="image/blurred"),
        ),
        collapse_panels=True,
    )

    rr.send_blueprint(blueprint)

    rr.set_time_sequence("iteration", 0)

    rr.log("image/original", rr.Image(img))
    yield stream.read()

    blur = img

    for i in range(100):
        rr.set_time_sequence("iteration", i)

        # Pretend blurring takes a while
        time.sleep(0.1)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)

        rr.log("image/blurred", rr.Image(blur))

        yield stream.read()


with gr.Blocks() as demo:
    with gr.Row():
        img = gr.Image(interactive=True, label="Image")
        with gr.Column():
            blur = gr.Button("Repeated Blur")
    with gr.Row():
        viewer = Rerun(streaming=True)

    blur.click(repeated_blur, inputs=[img], outputs=[viewer])


if __name__ == "__main__":
    demo.launch()
