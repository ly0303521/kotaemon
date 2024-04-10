from pathlib import Path

import gradio as gr


class HelpPage:
    def __init__(self, app):
        self._app = app
        self.dir_md = Path(__file__).parent.parent / "assets" / "md"
        self.doc_dir = Path(__file__).parents[4] / "docs"

        with gr.Accordion("User Guide"):
            with (self.doc_dir / "usage.md").open(encoding="utf-8") as fi:
                gr.Markdown(fi.read())

        with gr.Accordion("Changelogs"):
            gr.Markdown(self.get_changelogs())

    def get_changelogs(self):
        with (self.dir_md / "changelogs.md").open(encoding="utf-8") as fi:
            return fi.read()
