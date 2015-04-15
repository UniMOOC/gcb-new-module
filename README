# Adding a new module to GCB 1.8

Small example of how new modules are added on Google CourseBuilder 1.8 version

## Module folder

First thing you need is to create a new folder inside `modules/` to host all your module's files. Then you need a file to act as the module's entry point, its content should look something like this:

``` python
from models import custom_modules

def register_module():
    """Registers this module in the registry."""

    global_urls = []
    course_urls = []

    global custom_module
    custom_module = custom_modules.Module(
        'Module title',
        'Description',
        global_urls, course_urls)
    return custom_module
```

And now you have to add it to the list of modules in `app.yaml` under `env_variables.GCB_REGISTERED_MODULES` like so:

``` yaml
env_variables:
  GCB_PRODUCT_VERSION: '1.8.0'

  ...

  GCB_REGISTERED_MODULES:
    modules.activity_tag.activity_tag
    ...
    modules.oauth2.oauth2=disabled
    modules.new_module.new_module
```

And you're set. I've included a couple of URLs and hooks in the module configuration just in case an example is needed.
