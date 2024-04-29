
import gradio as gr
from app import demo as app
import os

_docs = {'Rerun': {'description': 'Creates an image component that can be used to upload images (as an input) or display images (as an output).', 'members': {'__init__': {'value': {'type': 'list[str] | None', 'default': 'None', 'description': 'A path or URL for the default value that Rerun component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'show_download_button': {'type': 'bool', 'default': 'True', 'description': 'If True, will display button to download image.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'height': {'type': 'int | str', 'default': '640', 'description': 'height of component in pixels. If a string is provided, will be interpreted as a CSS value. If None, will be set to 640px.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will allow users to upload and edit an image; if False, can only be used to display images. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}}, 'postprocess': {'value': {'type': 'list[gradio.data_classes.FileData]\n    | gradio.data_classes.FileData\n    | str\n    | list[str]', 'description': 'Expects a `str` or `pathlib.Path` object containing the path to the image.'}}, 'preprocess': {'return': {'type': 'str | None', 'description': 'A `str` containing the path to the image.'}, 'value': None}}, 'events': {'clear': {'type': None, 'default': None, 'description': 'This listener is triggered when the user clears the Rerun using the X button for the component.'}, 'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the Rerun changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'upload': {'type': None, 'default': None, 'description': 'This listener is triggered when the user uploads a file into the Rerun.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'Rerun': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_rerun`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange"> <a href="https://github.com/radames/gradio-rerun-viewer/issues" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/Issues-white?logo=github&logoColor=black"></a> 
</div>

Rerun viewer with Gradio
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_rerun
```

## Usage

```python
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
        run_on_click=True,
    )

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `Rerun`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["Rerun"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["Rerun"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, a `str` containing the path to the image.
- **As output:** Should return, expects a `str` or `pathlib.Path` object containing the path to the image.

 ```python
def predict(
    value: str | None
) -> list[gradio.data_classes.FileData]
    | gradio.data_classes.FileData
    | str
    | list[str]:
    return value
```
""", elem_classes=["md-custom", "Rerun-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          Rerun: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
