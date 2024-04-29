---
tags: [gradio-custom-component, SimpleImage, multimodal data, visualization, machine learning, robotics]
title: gradio_rerun
short_description: Rerun viewer with Gradio
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_rerun`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange"> <a href="https://github.com/radames/gradio-rerun-viewer/issues" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/Issues-white?logo=github&logoColor=black"></a> 

Rerun viewer with Gradio

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

## `Rerun`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">A path or URL for the default value that Rerun component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>show_download_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will display button to download image.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | str
```

</td>
<td align="left"><code>640</code></td>
<td align="left">height of component in pixels. If a string is provided, will be interpreted as a CSS value. If None, will be set to 640px.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will allow users to upload and edit an image; if False, can only be used to display images. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `clear` | This listener is triggered when the user clears the Rerun using the X button for the component. |
| `change` | Triggered when the value of the Rerun changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `upload` | This listener is triggered when the user uploads a file into the Rerun. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, a `str` containing the path to the image.
- **As input:** Should return, expects a `str` or `pathlib.Path` object containing the path to the image.

 ```python
 def predict(
     value: str | None
 ) -> list[gradio.data_classes.FileData]
    | gradio.data_classes.FileData
    | str
    | list[str]:
     return value
 ```
 
