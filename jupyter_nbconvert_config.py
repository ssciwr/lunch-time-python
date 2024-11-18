c = get_config()  # noqa
c.ExecutePreprocessor.enabled = True
c.ExecutePreprocessor.kernel_name = "python"
c.NbConvertApp.export_format = "slides"
c.SlidesExporter.extra_template_paths = ["."]
c.SlidesExporter.file_extension = ".slides.html"
c.SlidesExporter.reveal_transition = "convex"
c.SlidesExporter.reveal_scroll = True
c.SlidesExporter.template_name = "jupyter_nbconvert_template"
