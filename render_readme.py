import os
import glob

from jinja2 import Template

from cdt_config import (
    CDT_PATH,
    CUSTOM_CDT_PATH,
    folder_to_package,
)


def render_readme():
    recipes = set(
        glob.glob(CDT_PATH + "/*")
        + glob.glob(CUSTOM_CDT_PATH + "/*")
    )
    recipes = set(
        os.path.basename(r) for r in recipes if not r.endswith("README.md")
    )
    pkgs = sorted(list({folder_to_package(x) for x in recipes}))

    with open("README.md.tmpl", "r") as fp:
        tmpl = Template(fp.read())

    with open("README.md", "w") as fp:
        fp.write(tmpl.render(cdts=pkgs))


if __name__ == '__main__':
    render_readme()
