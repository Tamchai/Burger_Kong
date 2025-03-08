from fasthtml.common import *
app, rt = fast_app(live=True)
import register
import watch_and_seedetail

if __name__ == "__routing__":
    rt.run()