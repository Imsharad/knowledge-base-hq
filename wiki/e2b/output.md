CLI Commands
============

Build your sandbox with our CLI.

You can use `--help` flag for more information about commands.

* * *

Auth
====

  

[`auth login`](#auth-login)

----------------------------

Log in to the CLI. It will save your access token in `~/.e2b` file.

    e2b auth login
    

CopyCopied!

[`auth logout`](#auth-logout)

------------------------------

Log out of the CLI. It will remove your access token from `~/.e2b` file.

    e2b auth logout
    

CopyCopied!

[`auth info`](#auth-info)

--------------------------

Get info about your current user.

    e2b auth info
    

CopyCopied!

* * *

Templates
=========

  

[`template init`](#template-init)

----------------------------------

Creates a basic Dockerfile (`./e2b.Dockerfile`) in current directory. You can then run `e2b template build` to build sandbox template from this Dockerfile.

    e2b template init
    

CopyCopied!

#### **Options**

*   Name
    
    Flags
    
    \-p, --path
    
    `path`
    
    Description
    
    Change the root directory where the command is executed to `path` directory.
    

[`template build`](#template-build)

------------------------------------

Builds a sandbox template defined by `./e2b.Dockerfile` or `./Dockerfile` from the root directory. By default, the root directory is the current working directory. This command also creates the `e2b.toml` config.

    e2b template build
    

CopyCopied!

Running `e2b template build` without specifying a template with the `[template]` argument will rebuild template defined by the `e2b.toml` config.

If there is no `e2b.toml` config a new template will be created.

#### **Arguments**

*   Name
    
    Flags
    
    \[template\]
    
    Description
    
    Specify the template you want to rebuild. You can use the template name or ID.
    

#### **Options**

*   Name
    
    Flags
    
    \-c, --cmd
    
    `start-command`
    
    Description
    
    Specify the command that should be running when a sandbox starts.
    
*   Name
    
    Flags
    
    \--config
    
    `e2b-toml`
    
    Description
    
    Specify the path to the config file. By default, E2B tries to find `e2b.toml` in the root directory.
    
*   Name
    
    Flags
    
    \-n, --name
    
    `template-name`
    
    Description
    
    Specify the name of the sandbox template. You can use the template name to start the sandbox in the SDK. The name must be lowercase and contain only letters, numbers, dashes, and underscores.
    
*   Name
    
    Flags
    
    \-p, --path
    
    `path`
    
    Description
    
    Change the root directory where the command is executed to the `path` directory.
    
*   Name
    
    Flags
    
    \-d, --dockerfile
    
    `dockerfile`
    
    Description
    
    Specify the path to Dockerfile. By default E2B tries to find `e2b.Dockerfile` or `Dockerfile` in the root directory.
    
*   Name
    
    Flags
    
    \--cpu-count
    
    `cpu-count`
    
    Description
    
    Specify the number of CPUs that will be used to run the sandbox. The default value is 2.
    
*   Name
    
    Flags
    
    \--memory-mb
    
    `memory-mb`
    
    Description
    
    Specify the amount of memory in megabytes that will be used to run the sandbox. Must be an even number. The default value is 512.
    

[`template delete`](#template-delete)

--------------------------------------

Delete the sandbox template specified by the `[template]` argument, `e2b.toml` config in the working directory, or by an interactive selection. By default, the root directory is the current working directory.

This command also deletes the `e2b.toml` config.

    e2b template delete
    

CopyCopied!

Running `e2b template delete` without specifying a template with the `[template]` argument will delete the template defined by the `e2b.toml` config.

#### **Arguments**

*   Name
    
    Flags
    
    \[template\]
    
    Description
    
    Specify the template you want to delete. You can use the template name or ID.
    

#### **Options**

*   Name
    
    Flags
    
    \-p, --path
    
    `path`
    
    Description
    
    Change the root directory where the command is executed to the `path` directory.
    
*   Name
    
    Flags
    
    \--config
    
    `e2b-toml`
    
    Description
    
    Specify the path to the config file. By default, E2B tries to find `e2b.toml` in the root directory.
    
*   Name
    
    Flags
    
    \-s, --select
    
    Description
    
    Interactively select sandbox templates you want to delete.
    
*   Name
    
    Flags
    
    \-y, --yes
    
    Description
    
    Don't ask for confirmation before deleting the sandbox template.
    

[`template list`](#template-list)

----------------------------------

List your sandbox templates.

    e2b template list
    

CopyCopied!

* * *

Sandboxes
=========

  

[`sandbox list`](#sandbox-list)

--------------------------------

List your spawned sandboxes that are running right now.

    e2b sandbox list
    

CopyCopied!

[`sandbox connect`](#sandbox-connect)

--------------------------------------

Connects your terminal to a running sandbox that you spawned via the E2B SDK. This command is useful if you need to debug a running sandbox.

This command works similar to the `docker exec -it <container> bash` command in Docker.

    e2b sandbox connect <sandboxID>
    

CopyCopied!

You can use `e2b sandbox list` to get a list of running sandboxes and their IDs that can be used with `e2b sandbox connect <sandboxID>` command.

#### **Arguments**

*   Name
    
    Flags
    
    <sandboxID>
    
    Description
    
    Specify the ID of a running sandbox you want to connect to.
    

[`sandbox spawn`](#sandbox-spawn)

----------------------------------

Spawns a sandbox and connects your terminal to the sandbox. This command can be used to debug your sandbox template.

This command works similar to the `docker run -it <image> bash` command in Docker.

    e2b sandbox spawn
    

CopyCopied!

Running `e2b sandbox spawn` without specifying a template with the `[template]` argument will spawn sandbox defined by the `e2b.toml` config.

#### **Arguments**

*   Name
    
    Flags
    
    \[template\]
    
    Description
    
    Specify the template you want to spawn sandbox from. You can use the template name or ID.
    

#### **Options**

*   Name
    
    Flags
    
    \-p, --path
    
    `path`
    
    Description
    
    Change the root directory where the command is executed to `path` directory.
    
*   Name
    
    Flags
    
    \--config
    
    `e2b-toml`
    
    Description
    
    Specify the path to the config file. By default, E2B tries to find `e2b.toml` in the root directory.
    

[`sandbox kill`](#sandbox-kill)

--------------------------------

Immediately kill a running sandbox.

    e2b sandbox kill <sandboxID>
    

CopyCopied!

[`sandbox logs`](#sandbox-logs)

--------------------------------

Starts printing logs from the specified sandbox. If the sandbox is running new logs will be streamed to the terminal.

The timestamps are in the UTC format.

This command is useful if you need to debug a running sandbox or check logs from a sandbox that was already closed.

    e2b sandbox logs <sandboxID>
    

CopyCopied!

You can use `e2b sandbox list` to get a list of running sandboxes and their IDs that can be used with `e2b sandbox logs <sandboxID>` command.

#### **Arguments**

*   Name
    
    Flags
    
    <sandboxID>
    
    Description
    
    Specify the ID of the sandbox you want to get logs from.
    

#### **Options**

*   Name
    
    Flags
    
    \--level
    
    `level`
    
    Description
    
    Filter logs by level — allowed values are `DEBUG`, `INFO`, `WARN`, `ERROR`. The logs with the higher levels will be also shown.
    
    Default value is `DEBUG`.
    
*   Name
    
    Flags
    
    \-f, --follow
    
    Description
    
    Enable streaming logs until the sandbox is closed.
    
*   Name
    
    Flags
    
    \--format
    
    `format`
    
    Description
    
    Specify format for printing logs — allowed values are `pretty`, `json`.
    
    Default value is `pretty`.
    
*   Name
    
    Flags
    
    \--loggers
    
    `loggers`
    
    Description
    
    Specify enabled loggers — allowed values are `process`, `filesystem`, `terminal`, `network`. You can specify multiple loggers by separating them with a comma.
    
    Default value is `process,filesystem`.Installation
============

You build and manage sandbox templates with our CLI.

The CLI is distributed as an [NPM package](https://www.npmjs.com/package/e2b)
.

[Download CLI](#download-cli)

------------------------------

You can install the CLI with following command:

    npm install -g @e2b/cli@latest
    

CopyCopied!

[Login](#login)

----------------

You'll need to login to your account to start using the CLI. You'll be redirected to the browser after running the following command to finish the login.

    e2b login
    

CopyCopied!Examples
========

Here are some examples of how to use the E2B Code Interpreter package. If you are missing something, please let us know.

[Minimal example with the sharing context](#minimal-example-with-the-sharing-context)

--------------------------------------------------------------------------------------

The following example demonstrates how to create a shared context between multiple code executions. This is useful when you want to share variables between different code cells.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { CodeInterpreter } from '@e2b/code-interpreter'
    
    const sandbox = await CodeInterpreter.create()
    await sandbox.notebook.execCell('x = 1')
    
    const execution = await sandbox.notebook.execCell('x+=1; x')
    console.log(execution.text)  // outputs 2
    
    await sandbox.close()
    

CopyCopied!

[Get charts and any display-able data](#get-charts-and-any-display-able-data)

------------------------------------------------------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { CodeInterpreter } from '@e2b/code-interpreter'
    
    const sandbox = await CodeInterpreter.create()
    
    const code = `
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.linspace(0, 20, 100)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.show()
    `;
    
    // you can install dependencies in "jupyter notebook style"
    await sandbox.notebook.execCell("!pip install matplotlib")
    
    const execution = await sandbox.notebook.execCell(code)
    
    // this contains the image data, you can e.g. save it to file or send to frontend
    execution.results[0].png
    
    await sandbox.close()
    

CopyCopied!

[Streaming code output](#streaming-code-output)

------------------------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { CodeInterpreter } from "@e2b/code-interpreter";
    
    code = `
    import time
    import pandas as pd
    
    print("hello")
    time.sleep(3)
    data = pd.DataFrame(data=[[1, 2], [3, 4]], columns=["A", "B"])
    display(data.head(10))
    time.sleep(3)
    print("world")
    `
    
    const sandbox = await CodeInterpreter.create()
    
    await sandbox.notebook.execCell(code, {
      onStdout: (out) => console.log(out),
      onStderr: (outErr) => console.error(outErr),
      onResult: (result) => console.log(result.text)
    })
    

CopyCopied!Code Execution
==============

You can execute code using the notebook module, using the `execCell` method. The method takes a string of code as an argument and returns an object with the results of the execution.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { CodeInterpreter } from '@e2b/code-interpreter'
    
    const code = 'print("Hello, World!")'
    
    const sandbox = CodeInterpreter.create()
    const execution = await sandbox.notebook.execCell(code)
    

CopyCopied!

The `execCell` method also accepts following optional arguments:

*   `kernel id`: The ID of the kernel to execute the code on. If not provided, the default kernel is used. See [here](/docs/code-interpreter/kernels)
     for more info on kernels.
*   `on stdout`: A callback function to handle standard output messages from the code execution.
*   `on_stderr`: A callback function to handle standard error messages from the code execution.
*   `on_result`: A callback function to handle the result and display calls of the code execution.

[Streaming response](#streaming-response)

------------------------------------------

You can use the `on_*` callbacks to handle the output of the code execution as it happens. This is useful for long-running code. You can stream the output to the user as it is generated.

[Execution object](#execution-object)

--------------------------------------

The object returned by the `exec cell` method is little bit more complex, it's based on Jupyter. Here's an detailed explanation in the [Jupyter documentation](https://jupyter-client.readthedocs.io/en/stable/messaging.html)
.

It contains the following fields:

*   `results`: A list containing result of the cell (interactively interpreted last line) and display calls (e.g. matplotlib plots).
*   `logs`: Logs printed to stdout and stderr during execution.
*   `error`: An error message, if there was an error during execution of the cell. It works only for Python code, not for system (`!` e.g `!pip install e2b`) commands.

### Result object

This object can be created in two different ways:

*   Evaluation of the last line: If the last line of the code is an expression, the result is the value of that expression. As you would expect in REPL environments.
*   Display calls: Calls to display functions, which can be used to display rich output in the notebook. E.g. [`img.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)
    , [`display(img)`](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html)
    , etc.

Represents the data to be displayed as a result of executing a cell in a Jupyter notebook. The result is similar to the structure returned by [ipython kernel](https://ipython.readthedocs.io/en/stable/development/execution.html#execution-semantics)

The result can contain multiple types of data, such as text, images, plots, etc. Each type of data is represented as a string, and the result can contain multiple types of data. The display calls don't have to have text representation, it's always present for the actual result, the other representations are optional.

The result has those basic data types:

#### Text types:

*   `text`: text representation of the result
*   `html`: html representation of the result
*   `markdown`: markdown representation of the result
*   `latex`: latex representation of the result

#### Image types:

*   `png`: "base64 encoded png image",
*   `jpeg`: "base64 encoded jpeg image",
*   `svg`": "svg image",

#### Other types:

*   `json`: "json representation",
*   `javascript`: "javascript representation",
*   `pdf`: "base64 encoded pdf"

If you want to integrate your own display formats or how to implement them for your classes, you can read more in [here](https://github.com/ipython/ipython/blob/main/examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)

### Logs object

Logs printed to stdout and stderr during execution. Examples of logs are print statements, warnings, subprocess output, etc.

It contains two fields:

*   `stdout`: List of strings, each string is a line printed to stdout.
*   `stderr`: List of strings, each string is a line printed to stderr.

### Error object

An error message, if there was an error during execution of the cell.

It works only for Python code, not for system (e.g. `!pip install non_existent_package`) commands. The system commands are executed in a separate process and the output is in stdout/stderr.

It contains three fields:

*   `name`: Name of the error, e.g. `NameError`, `ValueError`, etc.
*   `value`: Value of the error, e.g. `name 'non_existent_variable' is not defined`, etc.
*   `traceback`: Traceback of the error.

[Example how to interpret the results to LLM](#example-how-to-interpret-the-results-to-llm)

--------------------------------------------------------------------------------------------

Here's an example how to return the results to LLM:

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    const code = '<CODE GENERATED BY LLM>'
    const execution = await sandbox.notebook.execCell(code)
    
    // There was an error during execution, return the error and its traceback
    if (execution.error) {
      return `There was an error during execution: ${execution.error.name}: ${execution.error.value}.\n
      ${execution.error.traceback}`
    }
    
    // The execution has some result, summarize to LLM, what are the results
    if (execution.results.length > 0) {
      let message = 'These are results of the execution:\n'
      let counter = 1
      for (const result of execution.results) {
        message += `Result ${counter++}:\n`
        if (result.isMainResult) {
          message += `[Main result]: ${result.text}\n`
        } else {
          message += `[Display data]: ${result.text}\n`
        }
        if (result.formats().length > 0) {
          message += `It has following formats: ${result.formats()}\n`
        }
      }
    
      return message
    }
    
    // There were no results, check if there was something is stdout/err
    if (
      execution.logs.stdout.length > 0 ||
      execution.logs.stderr.length > 0
    ) {
      let message = 'There was no result of the execution, but here are the logs:\n'
      if (execution.logs.stdout.length > 0) {
        message += `Stdout: ${execution.logs.stdout.join('\n')}\n`
      }
      if (execution.logs.stderr.length > 0) {
        message += `Stderr: ${execution.logs.stderr.join('\n')}\n`
      }
    
      return message
    }
    
    return 'There was no output of the execution.'
    

CopyCopied!Code Interpreter SDK
====================

E2B's [Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter)
 allows you to add code interpreting capabilities to your AI apps.

The code interpreter runs inside the [E2B Sandbox](https://github.com/e2b-dev/e2b)
 - an open-source secure sandbox made for running untrusted AI-generated code and AI agents.

*   ✅ Works with any LLM and AI framework
*   ✅ Supports streaming content like charts and stdout, stderr
*   ✅ Python & JS SDK
*   ✅ Runs on serverless and edge functions
*   ✅ Runs AI-generated code in secure sandboxed environments
*   ✅ 100% open source (including [infrastructure](https://github.com/e2b-dev/infra)
    )

[Quickstart](#quickstart)

--------------------------

### 1\. Install SDK

JavaScript/TypeScript

    npm i @e2b/code-interpreter
    

CopyCopied!

Python

    pip install e2b_code_interpreter
    

CopyCopied!

### 2\. Execute code with code interpreter inside sandbox

**JavaScript**

    import { CodeInterpreter } from '@e2b/code-interpreter'
    
    const sandbox = await CodeInterpreter.create()
    await sandbox.notebook.execCell('x = 1')
    
    const execution = await sandbox.notebook.execCell('x+=1; x')
    console.log(execution.text)  // outputs 2
    
    await sandbox.close()
    

CopyCopied!

**Python**

    from e2b_code_interpreter import CodeInterpreter
    
    with CodeInterpreter() as sandbox:
        sandbox.notebook.exec_cell("x = 1")
    
        execution = sandbox.notebook.exec_cell("x+=1; x")
        print(execution.text)  # outputs 2
    

CopyCopied!

### 3\. Hello World guide

Dive depeer and check out the [JavaScript](/docs/hello-world/js)
 and [Python](/docs/hello-world/py)
 the Hello World guides to learn how o connect code interpreter LLMs.Kernels
=======

In this section you can find information about kernels and how to use them in Code Interpreter SDK

By default the template starts with one default kernel. This kernel is used to execute code, if you don't specify `kernelID`. You can imagine kernel as a separate environment where code is executed. You can have multiple kernels running at the same time. Each kernel has its own state, so you can have multiple kernels running different code at the same time.

Kernel will be kept kept alive with the sandbox even if you disconnect.

[Creating a new kernel](#creating-a-new-kernel)

------------------------------------------------

To create a new kernel there's a `create kernel` method in `CodeInterpreter` class. This method takes two optional arguments:

*   `cwd` - working directory for the kernel, all system commands and file operations will be executed in this directory
*   `kernel name` - kernel spec name (defaults to default kernel spec for server). In our case it's `python3`. If you want to use another kernel, you have to install in the template first. In that case you probably want to use [Custom Template](/docs/code-interpreter/template)
    .

[Restarting a kernel](#restarting-a-kernel)

--------------------------------------------

To restart a kernel you can use `restart` method. This method takes one argument - `kernelID`, if not specifed it will restart the default kernel. This method will restart the kernel and clear its state.

[Listing kernels](#listing-kernels)

------------------------------------

To list all kernels you can use `list` method. This method returns an array of all running kernels with their IDs and kernel spec names.

[Shutting down a kernel](#shutting-down-a-kernel)

--------------------------------------------------

To shutdown a kernel you can use `shutdown` method. This method takes one argument - `kernelID`, if not specifed it will delete the default kernel. This method will delete the kernel and all its state.Using custom sandbox template & custom compute with Code Interpreter SDK
========================================================================

If you want to customize the Code Interprerter sandbox (e.g.: add a preinstalled package) you can do that by using a [custom sandbox template](https://e2b.dev/docs/sandbox/templates/overview)
.

[Step-by-step guide](#step-by-step-guide)

------------------------------------------

1.  Create custom sandbox by following [this guide](https://e2b.dev/docs/guide/custom-sandbox)
    
2.  Use prebuilt [E2B Code Interpreter image](https://hub.docker.com/r/e2bdev/code-interpreter)
     by replacing the `FROM` command in your `e2b.Dockerfile` with following
    
        FROM e2bdev/code-interpreter:latest
        
    
    CopyCopied!
    
3.  Copy [`start-up.sh`](./start-up.sh)
     to the same directory where's your `e2b.toml`
    
4.  Run the following in the same directory where's your `e2b.toml`
    
        e2b template build -c "/home/user/.jupyter/start-up.sh"
        
    
    CopyCopied!
    
5.  Use your custom sandbox with Code Interpreter SDK
    
    **Python**
    
        from e2b_code_interpreter import CodeInterpreter
        sandbox = CodeInterpreter(template="your-custom-sandbox-name")
        execution = sandbox.notebook.exec_cell("print('hello')")
        sandbox.close()
        
        # Or you can use `with` which handles closing the sandbox for you
        with CodeInterpreter(template="your-custom-sandbox-name") as sandbox:
            execution = sandbox.notebook.exec_cell("print('hello')")
        
    
    CopyCopied!
    
    **JavaScript/TypeScript**
    
        import { CodeInterpreter } from '@e2b/code-interpreter'
        const sandbox = await CodeInterpreter.create({ template: 'your-custom-sandbox-name' })
        const execution = await sandbox.notebook.execCell('print("hello")')
        await sandbox.close()
        
    
    CopyCopied!
    

[Customize CPU & RAM of your sandbox](#customize-cpu-and-ram-of-your-sandbox)

------------------------------------------------------------------------------

You can customize number of CPUs and MiB of RAM for your sandbox. To achieve that, specify the `--cpu-count` and `--memory-mb` options during the build step:

    e2b template build -c "/home/user/.jupyter/start-up.sh" --cpu-count 4 --memory-mb 4096
    

CopyCopied!

The above will create a custom sandbox with 4 CPUs a 4 GiB of RAM.

[How to install another Python kernels](#how-to-install-another-python-kernels)

--------------------------------------------------------------------------------

Jupyter has ability to work with different than Python kernel. It even supports multiple kernels in one notebook. If you want to install another kernels.

You can find list of available kernels [here](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
. Each has a little bit different installation process, but in general you need to install kernel package and register it in jupyter.Getting help
============

If you have any questions, issues, or feature requests, please reach out on of the following channels:

*   Send us an email at [hello@e2b.dev](mailto:hello@e2b.dev)
    
*   Talk to us on our [Discord server](https://discord.gg/U7KEcGErtQ)
    
*   Open an issue on [our GitHub](https://github.com/e2b-dev/e2b)
    
*   Reach out on [Twitter / X](https://twitter.com/e2b_dev)Your API Key
============

You can get your API key by signing up.[Sign up to get your API key](/docs/sign-in?view=sign-up)

[Use API key](#use-api-key)

----------------------------

To use the API key, you either:

*   **Set the API key as the `E2B_API_KEY` environment variable**
*   Or pass it directly to the `CodeInterpreter` constructor like this:

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { CodeInterpreter } from '@e2b/code-interpreter'
    
    const sandbox = await CodeInterpreter.create({ apiKey: 'YOUR_API_KEY' })
    await sandbox.notebook.execCell('x = 1')
    
    const execution = await sandbox.notebook.execCell('x+=1; x')
    console.log(execution.text)  // outputs 2
    
    await sandbox.close()
    

CopyCopied!Installation
============

You create and control sandboxes with our SDKs. We offer SDKs for [JavaScript / TypeScript](https://www.npmjs.com/package/e2b)
, and [Python](https://pypi.org/project/e2b/)
.

### JavaScript & Typescript

Usable both in Node.js and in the browser. Requires at least Node.js 18.0.

[](https://www.npmjs.com/package/e2b)

[Inspect on NPM](https://www.npmjs.com/package/e2b)

![](/docs/_next/static/media/node.ffbff9e8.svg)

### Python

Requires at least Python 3.8.

[](https://pypi.org/project/e2b)

[Inspect on PyPi](https://pypi.org/project/e2b)

![](/docs/_next/static/media/python.c624d255.svg)

You can install them using the following commands:

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    npm install e2b
    

CopyCopied!

[Next steps](#next-steps)

--------------------------

1.  [Get your API key](/docs/getting-started/api-key)
    
2.  [Explore the Sandbox API](/docs/sandbox/api/envs)Connecting bucket to the sandbox
================================

To enable persistence of the data in the sandbox we can use a bucket to store the data. We are leveraging the fuse file system to mount the bucket to the sandbox.

You will need to build a custom sandbox template with the fuse file system installed. The guide how to build a custom sandbox template can be found [here](/docs/guide/custom-sandbox)
.

[Google Cloud Storage](#google-cloud-storage)

----------------------------------------------

### Prerequisites

To use the Google Cloud Storage we'll need to have a bucket and a service account. The service account can be created [here](https://console.cloud.google.com/iam-admin/serviceaccounts)
, the bucket can be created [here](https://console.cloud.google.com/storage)
.

If you want to write to the bucket the service account must have the `Storage Object Admin` role for this bucket.

The guide how to create a service account key can be found [here](https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console)
.

### Mounting the bucket

To use the Google Cloud Storage we need to install the `gcsfuse` package. There's simple `Dockerfile` that can be used to create a container with the `gcsfuse` installed.

    FROM ubuntu:latest
    
    RUN apt-get update && apt-get install -y gnupg lsb-release wget
    
    RUN lsb_release -c -s > /tmp/lsb_release
    RUN GCSFUSE_REPO=$(cat /tmp/lsb_release); echo "deb https://packages.cloud.google.com/apt gcsfuse-$GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list
    RUN wget -O - https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    
    RUN apt-get update && apt-get install -y gcsfuse
    
    

CopyCopied!

The actual mounting of the bucket is done in runtime during the start of the sandbox. The `gcsfuse` command is used to mount the bucket to the sandbox.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: '<your template id>' })
    await sandbox.filesystem.makeDir("/home/user/bucket")
    await sandbox.uploadFile("key.json")
    
    const process = await sandbox.process.start("sudo gcsfuse <flags> --key-file /home/user/key.json <bucket-name> /home/user/bucket")
    const output = await process.wait()
    if (output.exitCode) {
        throw Error(output.stderr)
    }
    

CopyCopied!

### Flags

The list of all flags can be found [here](https://cloud.google.com/storage/docs/gcsfuse-cli#options)
.

### Allow the default user to access the files

To allow the default user to access the files we can use the following flags:

    -o allow_other -file-mode=777 -dir-mode=777
    

CopyCopied!

[Amazon S3](#amazon-s3)

------------------------

For Amazon S3 we can use the `s3fs` package. The `Dockerfile` is similar to the one for the Google Cloud Storage.

    FROM ubuntu:latest
    
    RUN apt-get update && apt-get install s3fs
    

CopyCopied!

Similarly to the Google Cloud Storage, the actual mounting of the bucket is done in runtime during the start of the sandbox. The `s3fs` command is used to mount the bucket to the sandbox.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: '<your template id>' })
    await sandbox.filesystem.makeDir('/home/user/bucket')
    
    
    // Create a file with the credentials
    // If you use another path for the credentials you need to add the path in the command s3fs command
    await sandbox.filesystem.write('/root/.passwd-s3fs', '<AWS_ACCESS_KEY_ID>:<AWS_SECRET_ACCESS_KEY>')
    await sandbox.process.startAndWait('sudo chmod 600 /root/.passwd-s3fs')
    
    const process = await sandbox.process.start('sudo s3fs <flags> <bucket-name> /home/user/bucket')
    const output = await process.wait()
    if (output.exitCode) {
        throw Error(output.stderr)
    }
    

CopyCopied!

### Flags

The list of all flags can be found [here](https://manpages.ubuntu.com/manpages/xenial/man1/s3fs.1.html)
.

### Allow the default user to access the files

To allow the default user to access the files add the following flag:

    -o allow_other
    

CopyCopied!

[Cloudflare R2](#cloudflare-r2)

--------------------------------

For Cloudflare R2 we can use very similar setup as for S3. The `Dockerfile` is the same as for S3. The mounting is slightly different, we need to specify the endpoint for R2.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    
    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: '<your template id>' })
    await sandbox.filesystem.makeDir('/home/user/bucket')
    
    // Create a file with the R2 credentials
    // If you use another path for the credentials you need to add the path in the command s3fs command
    await sandbox.filesystem.write('/root/.passwd-s3fs', '<R2_ACCESS_KEY_ID>:<R2_SECRET_ACCESS_KEY>')
    await sandbox.process.startAndWait('sudo chmod 600 /root/.passwd-s3fs')
    
    const output = await sandbox.process.startAndWait('sudo s3fs -o url=https://<ACCOUNT ID>.r2.cloudflarestorage.com <flags> <bucket-name> /home/user/bucket')
    if (output.exitCode) {
        throw Error(output.stderr)
    }
    

CopyCopied!

### Flags

It's the same as for S3.Creating Custom Sandbox
=======================

In this guide, we'll create a custom E2B sandbox with preinstalled dependencies and files. Once the sandbox is built, we'll show how to spawn and control it with our SDK.

[Prerequisites](#prerequisites)

--------------------------------

1.  [Node.js](https://nodejs.org/)
     18.0.0 or later
2.  [E2B CLI](/docs/cli/installation)
    
3.  Running Docker instance

[1\. Install E2B CLI](#1-install-e2-b-cli)

-------------------------------------------

### Install CLI

    npm install -g @e2b/cli@latest
    

CopyCopied!

You need Node.js 18.0.0 or later to install the CLI.

[2\. Login to CLI](#2-login-to-cli)

------------------------------------

Before you create your first custom sandbox, you will need to authenticate in the CLI with your E2B account. Run the following command in your terminal.

### Login to CLI

    e2b auth login
    

CopyCopied!

You need to have an existing E2B account to login. Sign up [here](/docs/getting-started/api-key)
.

[3\. Create `e2b.Dockerfile`](#3-create-e2b-dockerfile)

--------------------------------------------------------

To describe how your custom sandbox will look like, create a new Dockerfile and name it `e2b.Dockerfile`. We use this Dockerfile as the [template file](/docs/sandbox/templates/template-file)
.

Run `e2b template init` to create `e2b.Dockerfile` in the current directory.

We want our custom sandbox to have the [ffmpeg](https://www.ffmpeg.org/)
 isntalled - ffmpeg is a tool for editing video and audio files.

### e2b.Dockerfile

    # You can use most of the Debian-based base images
    FROM ubuntu:22.04
    
    # Install the ffmpeg tool/
    RUN apt update \
        && apt install -y ffmpeg
    

CopyCopied!

[4\. Build custom sandbox](#4-build-custom-sandbox)

----------------------------------------------------

Now it's time to create your custom sandbox based on the sandbox template file (the `e2b.Dockefile` file) you just created in the previous step.

Run the following command inside the template file directory in your terminal.

[Pro users](/docs/pricing)
 can use the `--cpu-count=` ([docs](/docs/cli/commands#template-build)
) and `--memory-mb=` ([docs](/docs/cli/commands#template-build)
) flags to customize the sandbox compute. Read more about the compute [here](/docs/sandbox/compute)
.

### Build sandbox template

    e2b template build --name "my-agent-sandbox"
    

CopyCopied!

Use the `.dockerignore` file to exclude files from the sandbox template.

The final output should look similar to this.

### Build output

    Preparing sandbox template building (1 files in Docker build context).
    Found ./e2b.Dockerfile that will be used to build the sandbox template.
    Started building the sandbox template my-agent-sandbox
    
    # Truncated for visibility
    # ...
    # ...
    
    Running postprocessing. It can take up to few minutes.
    
    Postprocessing finished.
    
    ✅ Building sandbox template my-agent-sandbox finished.
    
    ┌ Usage examples ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    │                                                                                                                                                      │
    │  You can use E2B Python or JS SDK to spawn sandboxes now.                                                                                            │
    │  Find more here - https://e2b.dev/docs/guide/custom-sandbox in Spawn and control your sandbox section.                                               │
    │                                                                                                                                                      │
    │───────────────────────────────────────────────────────────────────── Python SDK ─────────────────────────────────────────────────────────────────────│
    │                                                                                                                                                      │
    │  from e2b import Sandbox                                                                                                                             │
    │                                                                                                                                                      │
    │  # Start sandbox                                                                                                                                     │
    │  sandbox = Sandbox("my-agent-sandbox")                                                                                                               │
    │                                                                                                                                                      │
    │  # Interact with sandbox. Learn more here:                                                                                                           │
    │  # https://e2b.dev/docs/sandbox/overview                                                                                                             │
    │                                                                                                                                                      │
    │  # Close sandbox once done                                                                                                                           │
    │  sandbox.close()                                                                                                                                     │
    │                                                                                                                                                      │
    │─────────────────────────────────────────────────────────────────────── JS SDK ───────────────────────────────────────────────────────────────────────│
    │                                                                                                                                                      │
    │  import { Sandbox } from 'e2b'                                                                                                                  │
    │                                                                                                                                                      │
    │  // Start sandbox                                                                                                                                    │
    │  const sandbox = await Sandbox.create('my-agent-sandbox')                                                                                            │
    │                                                                                                                                                      │
    │  // Interact with sandbox. Learn more here:                                                                                                          │
    │  // https://e2b.dev/docs/sandbox/overview                                                                                                            │
    │                                                                                                                                                      │
    │  // Close sandbox once done                                                                                                                          │
    │  await sandbox.close()                                                                                                                               │
    │                                                                                                                                                      │
    └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    
    Execution time: 42.55s
    

CopyCopied!

This will create the `e2b.toml` file storing the sandbox config.

### e2b.toml

    # This is a config for E2B sandbox template
    template_id = "1wdqsf9le9gk21ztb4mo"
    dockerfile = "e2b.Dockerfile"
    template_name = "my-agent-sandbox"
    

CopyCopied!

| Sandbox template name | Sandbox template ID |
| --- | --- |
| `my-agent-sandbox` | `1wdqsf9le9gk21ztb4mo` |

### Updating your sandbox template

If you want to update your sandbox template, you run the same command you did to build it. This will rebuild the template.

### Update sandbox template

    e2b template build
    

CopyCopied!

[5\. Spawn and control your sandbox](#5-spawn-and-control-your-sandbox)

------------------------------------------------------------------------

Now you can use the [E2B SDK](/docs/getting-started/installation)
 to spawn & control your new custom sandbox.

The sandbox template name is `my-agent-sandbox`. We'll use it as an unique identifier and pass it to the SDK as the `template` parameter. This way, we'll be able to spawn our custom sandbox and control it with the SDK.

### Spawn & control your custom sandbox

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    // Spawn your custom sandbox
    const sandbox = await Sandbox.create({ template: 'my-agent-sandbox' }) 
    
    // Interact with sandbox. Learn more here:
    // https://e2b.dev/docs/sandbox/overview
    
    // Close sandbox once done
    await sandbox.close()
    

CopyCopied!Hello World.ts
==============

This JavaScript guide will show you the basics of E2B:

*   Connect the code interpreter to an LLM
*   Prompt the LLM to generate the Python code
*   Execute the AI-generated Python code in a secure E2B sandbox

### Get full code

Check out the [full code in our cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/hello-world-js)
.

### Overview

1.  [Install Code Interpreter SDK](#1-install-code-interpreter-sdk)
    
2.  [Prepare prompt and tools for LLM](#2-prepare-prompt-and-tools-for-llm)
    
3.  [Prepare code interpreting](#3-prepare-code-interpreting)
    
4.  [Call LLM and parse response with tools](#4-call-llm-and-parse-response-with-tools)
    
5.  [Create code interpreter and run everything](##5-create-code-interpreter-and-run-everything)
    
6.  [Save generated chart](#6-save-generated-chart)
    

[1\. Install Code Interpreter SDK](#1-install-code-interpreter-sdk)

--------------------------------------------------------------------

The Code Interpreter SDK allows you to run AI-generated code in a secure small VM - **E2B sandbox** - made for AI code execution. Inside the sandbox is a Jupyter server running that you can control from our SDK through the `notebook.execCell()` method.

Check out the [SDK's repository on GitHub](https://github.com/e2b-dev/code-interpreter)
.

    npm init -y \
    && npm i --save-dev typescript tsx @types/node \
    && npm i @e2b/code-interpreter
    

CopyCopied!

Get your E2B API key [here](/docs/getting-started/api-key)
 and save it to `.env` in your root directory.

### .env

    E2B_API_KEY="e2b-api-key"
    

CopyCopied!

[2\. Prepare prompt and tools for LLM](#2-prepare-prompt-and-tools-for-llm)

----------------------------------------------------------------------------

We'll be using Anthropic's [Claude 3 Opus](https://www.anthropic.com/news/claude-3-family)
 model but E2B works with any LLM so feel free to pick any you want!

Usually, all you need from the model is just support for tool use. If the LLM doesn't support tool use, you can ask the LLM to respond with Markdown or XML and parse the LLM's output on your own. Then just pass the parsed code from code blocks to the code interpreter.

Create the `model.ts` file and paste the following code.

### model.ts

    import { Tool } from '@anthropic-ai/sdk/src/resources/beta/tools'
    
    export const MODEL_NAME = 'claude-3-opus-20240229'
    
    export const SYSTEM_PROMPT = `
    ## your job & context
    you are a python data scientist. you are given tasks to complete and you run python code to solve them.
    - the python code runs in jupyter notebook.
    - every time you call \`execute_python\` tool, the python code is executed in a separate cell. it's okay to multiple calls to \`execute_python\`.
    - display visualizations using matplotlib or any other visualization library directly in the notebook. don't worry about saving the visualizations to a file.
    - you have access to the internet and can make api requests.
    - you also have access to the filesystem and can read/write files.
    - you can install any pip package (if it exists) if you need to but the usual packages for data analysis are already preinstalled.
    - you can run any python code you want, everything is running in a secure sandbox environment.
    `
    
    export const tools: Tool[] = [\
      {\
        name: 'execute_python',\
        description: 'Execute python code in a Jupyter notebook cell and returns any result, stdout, stderr, display_data, and error.',\
        input_schema: {\
          type: 'object',\
          properties: {\
            code: {\
              type: 'string',\
              description: 'The python code to execute in a single cell.'\
            }\
          },\
          required: ['code']\
        }\
      }\
    ]
    
    

CopyCopied!

This defines our system prompt and the `tools` dictionary with available tools for the LLM - namely the `"execute_python"` tool. A little bit later, we'll connect `"execute_python"` to the E2B's code interpretrer.

[3\. Prepare code interpreting](#3-prepare-code-interpreting)

--------------------------------------------------------------

We'll create a new function called `codeInterpret()` in a separate file `codeInterpreter.ts`.

### codeInterpreter.ts

    import { CodeInterpreter } from '@e2b/code-interpreter'
    
    export async function codeInterpret(codeInterpreter: CodeInterpreter, code: string) {
      console.log(`\n${'='.repeat(50)}\n> Running following AI-generated code:\n${code}\n${'='.repeat(50)}`);
    
      const exec = await codeInterpreter.notebook.execCell(
        code,
        {
          // You can stream logs from the code interpreter
          // onStderr: (stderr: string) => console.log("\n[Code Interpreter stdout]", stderr),
          // onStdout: (stdout: string) => console.log("\n[Code Interpreter stderr]", stdout),
          //
          // You can also stream additional results like charts, images, etc.
          // onResult: ...
        }
      )
    
      if (exec.error) {
        console.log('[Code Interpreter error]', exec.error) // Runtime error
        return undefined
      }
    
      return exec
    }
    

CopyCopied!

This function takes the `CodeInterpreter` object from our SDK, and `code` as paramaters. The `code` parameter is the code generated by the LLM.

Inside the function, we call the `codeInterpreter.notebook.execCell()` method. The `execCell()` takes `code` argument, and executes this `code` inside E2B sandbox.

[4\. Call LLM and parse response with tools](#4-call-llm-and-parse-response-with-tools)

----------------------------------------------------------------------------------------

We're using Claude 3 Opus. Get your [Anthropic API key](https://console.anthropic.com/)
, save it to `.env` file, and install the [Anthropic SDK](https://docs.anthropic.com/claude/reference/client-sdks)
.

### .env

    ANTHROPIC_API_KEY="anthropic-api-key"
    

CopyCopied!

    npm i @anthropic-ai/sdk
    

CopyCopied!

Now we'll put everything together. Create the `index.ts` file, import dependencies, and create the `chat()` function that will do the LLM calling and tool parsing.

### index.ts

    import * as fs from 'fs'
    
    import 'dotenv/config'
    import { CodeInterpreter, Execution } from '@e2b/code-interpreter'
    import Anthropic from '@anthropic-ai/sdk'
    
    import {
      MODEL_NAME,
      SYSTEM_PROMPT,
      tools,
    } from './model'
    import { codeInterpret } from './codeInterpreter'
    
    const anthropic = new Anthropic()
    
    async function chat(codeInterpreter: CodeInterpreter, userMessage: string): Promise<Execution | undefined> {
      console.log('Waiting for Claude...')
    
      const msg = await anthropic.beta.tools.messages.create({
        model: MODEL_NAME,
        system: SYSTEM_PROMPT,
        max_tokens: 4096,
        messages: [{role: 'user', content: userMessage}],
        tools,
      })
    
      console.log(`\n${'='.repeat(50)}\nModel response: ${msg.content}\n${'='.repeat(50)}`)
      console.log(msg)
    
      if (msg.stop_reason === 'tool_use') {
        const toolBlock = msg.content.find((block) => block.type === 'tool_use');
        const toolName = toolBlock.name
        const toolInput = toolBlock.input
    
        console.log(`\n${'='.repeat(50)}\nUsing tool: ${toolName}\n${'='.repeat(50)}`);
    
        if (toolName === 'execute_python') {
          const code = toolInput.code
          return codeInterpret(codeInterpreter, code)
        }
        return undefined
      }
    }
    

CopyCopied!

[5\. Create code interpreter and run everything](#5-create-code-interpreter-and-run-everything)

------------------------------------------------------------------------------------------------

Now we put all together, and run our program. In the end of `index.ts` add following code prompting the LLM to visualize a distribution of height of men and print the median.

### index.ts

    async function run() {
      const userMessage = 'Visualize a distribution of height of men based on the latest data you know. Also print the median value.'
    
      const codeInterpreter = await CodeInterpreter.create()
    
      const codeOutput = await chat(codeInterpreter, userMessage)
      if (!codeOutput) {
        console.log('No code output')
        return
      }
    
      const logs = codeOutput.logs
      console.log(logs)
    
      if (codeOutput.results.length == 0) {
        console.log('No results')
        return
      }
    
      const firstResult = codeOutput.results[0]
      // Print description of the first rich result
      console.log(firstResult.text)
    
      await codeInterpreter.close()
    }
    
    run()
    

CopyCopied!

After running your code with the following command

    $ tsx index.ts
    

CopyCopied!

you should see similar results to this:

    stdout=['The median male height is 175.5 cm\n'] stderr=[]
    <Figure size 800x400 with 1 Axes>
    

CopyCopied!

We got our median in the logs (`stdout`, and `stderr`) but we also something intering in `firstResult`.

    <Figure size 800x400 with 1 Axes>
    

CopyCopied!

[6\. Save generated chart](#6-save-generated-chart)

----------------------------------------------------

This looks like a plot. Let's save it to a file. Update the `run()` function like this, and run the code again with `tsx index.ts` in your terminal.

### index.ts

    async function run() {
      const userMessage = 'Visualize a distribution of height of men based on the latest data you know. Also print the median value.'
    
      const codeInterpreter = await CodeInterpreter.create()
    
      const codeOutput = await chat(codeInterpreter, userMessage)
      if (!codeOutput) {
        console.log('No code output')
        return
      }
    
      const logs = codeOutput.logs
      console.log(logs)
    
      if (codeOutput.results.length == 0) {
        console.log('No results')
        return
      }
    
      const firstResult = codeOutput.results[0]
      // Print description of the first rich result
      console.log(firstResult.text)
    
      // If we received a chart in PNG form, we can visualize it
      if (firstResult.png) {
          // Decode the base64 encoded PNG data
          const pngData = Buffer.from(firstResult.png, 'base64');
    
          // Generate a unique filename for the PNG
          const filename = 'chart.png';
    
          // Save the decoded PNG data to a file
          fs.writeFileSync(filename, pngData);
    
          console.log(`Saved chart to ${filename}`);
      }
    
      await codeInterpreter.close()
    }
    
    run()
    

CopyCopied!

The chart got saved in the `chart.png` file and it should look similar to this:

![Chart visualizing distribution height of men](/docs/_next/static/media/hello-world-chart.fd72ff25.png)Hello World.py
==============

This Python guide will show you the basics of E2B:

*   Connect the code interpreter to an LLM
*   Prompt the LLM to generate the Python code
*   Execute the AI-generated Python code in a secure E2B sandbox

### Get full code

Check out the [full code in our cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/hello-world-python)
.

### Overview

1.  [Install Code Interpreter SDK](#1-install-code-interpreter-sdk)
    
2.  [Prepare prompt and tools for LLM](#2-prepare-prompt-and-tools-for-llm)
    
3.  [Prepare code interpreting](#3-prepare-code-interpreting)
    
4.  [Call LLM and parse response with tools](#4-call-llm-and-parse-response-with-tools)
    
5.  [Create code interpreter and run everything](##5-create-code-interpreter-and-run-everything)
    
6.  [Save generated chart](#6-save-generated-chart)
    

[1\. Install Code Interpreter SDK](#1-install-code-interpreter-sdk)

--------------------------------------------------------------------

The Code Interpreter SDK allows you to run AI-generated code in a secure small VM - **E2B sandbox** - made for AI code execution. Inside the sandbox is a Jupyter server running that you can control from our SDK through the `notebook.execCell()` method.

Check out the [SDK's repository on GitHub](https://github.com/e2b-dev/code-interpreter)
.

    pip install e2b_code_interpreter python-dotenv
    

CopyCopied!

Get your E2B API key [here](/docs/getting-started/api-key)
 and save it to `.env` in your root directory.

### .env

    E2B_API_KEY="e2b-api-key"
    

CopyCopied!

[2\. Prepare prompt and tools for LLM](#2-prepare-prompt-and-tools-for-llm)

----------------------------------------------------------------------------

We'll be using Anthropic's [Claude 3 Opus](https://www.anthropic.com/news/claude-3-family)
 model but E2B works with any LLM so feel free to pick any you want!

Usually, all you need from the model is just support for tool use. If the LLM doesn't support tool use, you can ask the LLM to respond with Markdown or XML and parse the LLM's output on your own. Then just pass the parsed code from code blocks to the code interpreter.

Create the `model.py` file and paste the following code.

### model.py

    MODEL_NAME = "claude-3-opus-20240229"
    
    SYSTEM_PROMPT = """
    ## your job & context
    you are a python data scientist. you are given tasks to complete and you run python code to solve them.
    - the python code runs in jupyter notebook.
    - every time you call `execute_python` tool, the python code is executed in a separate cell. it's okay to multiple calls to `execute_python`.
    - display visualizations using matplotlib or any other visualization library directly in the notebook. don't worry about saving the visualizations to a file.
    - you have access to the internet and can make api requests.
    - you also have access to the filesystem and can read/write files.
    - you can install any pip package (if it exists) if you need to but the usual packages for data analysis are already preinstalled.
    - you can run any python code you want, everything is running in a secure sandbox environment.
    """
    
    tools = [\
        {\
            "name": "execute_python",\
            "description": "Execute python code in a Jupyter notebook cell and returns any result, stdout, stderr, display_data, and error.",\
            "input_schema": {\
                "type": "object",\
                "properties": {\
                    "code": {\
                        "type": "string",\
                        "description": "The python code to execute in a single cell."\
                    }\
                },\
                "required": ["code"]\
            }\
        }\
    ]
    

CopyCopied!

This defines our system prompt and the `tools` dictionary with available tools for the LLM - namely the `"execute_python"` tool. A little bit later, we'll connect `"execute_python"` to the E2B's code interpreter.

[3\. Prepare code interpreting](#3-prepare-code-interpreting)

--------------------------------------------------------------

We'll create a new function called `code_interpret()` in a separate file `code_interpreter.py`.

### code\_interpreter.py

    from e2b_code_interpreter import CodeInterpreter
    
    def code_interpret(code_interpreter: CodeInterpreter, code: str):
      print(f"\n{'='*50}\n> Running following AI-generated code:\n{code}\n{'='*50}")
      exec = code_interpreter.notebook.exec_cell(
        code,
        # You can stream logs from the code interpreter
        # on_stderr=lambda stderr: print("\n[Code Interpreter stdout]", stderr),
        # on_stdout=lambda stdout: print("\n[Code Interpreter stderr]", stdout),
        #
        # You can also stream additional results like charts, images, etc.
        # on_result=...
      )
    
      if exec.error:
        print("[Code Interpreter error]", exec.error) # Runtime error
      else:
        return exec.results, exec.logs
    

CopyCopied!

This function takes the `CodeInterpreter` object from our SDK and `code` as paramaters. The `code` parameter is the code generated by the LLM.

Inside the function, we call the `code_interpreter.notebook.exec_cell()` method. The `exec_cell()` takes the `code` argument and executes this `code` inside E2B sandbox.

[4\. Call LLM and parse response with tools](#4-call-llm-and-parse-response-with-tools)

----------------------------------------------------------------------------------------

We're using Claude 3 Opus. Get your [Anthropic API key](https://console.anthropic.com/)
, save it to `.env` file, and install the [Anthropic SDK](https://docs.anthropic.com/claude/reference/client-sdks)
.

### .env

    ANTHROPIC_API_KEY="anthropic-api-key"
    

CopyCopied!

    pip install anthropic
    

CopyCopied!

Now we'll put everything together. Create the `main.py` file, import dependencies, and create the `chat()` function that will do the LLM calling and tool parsing.

### main.py

    import base64
    from dotenv import load_dotenv
    from anthropic import Anthropic
    from typing import List, Tuple
    from e2b_code_interpreter import CodeInterpreter, Result
    from e2b_code_interpreter.models import Logs
    
    from e2b_hello_world.model import MODEL_NAME, SYSTEM_PROMPT, tools
    from e2b_hello_world.code_interpreter import code_interpret
    
    # Load the .env file
    load_dotenv()
    
    client = Anthropic()
    
    def chat(code_interpreter: CodeInterpreter, user_message: str) -> Tuple[List[Result], Logs]:
        print(f"\n{'='*50}\nUser Message: {user_message}\n{'='*50}")
    
        message = client.beta.tools.messages.create(
            model=MODEL_NAME,
            system=SYSTEM_PROMPT,
            max_tokens=4096,
            messages=[{"role": "user", "content": user_message}],
            tools=tools,
        )
    
        print(f"\n{'='*50}\nModel response: {message.content}\n{'='*50}")
    
        if message.stop_reason == "tool_use":
            tool_use = next(block for block in message.content if block.type == "tool_use")
            tool_name = tool_use.name
            tool_input = tool_use.input
    
            print(f"\n{'='*50}\nUsing tool: {tool_name}\n{'='*50}")
    
            if tool_name == "execute_python":
                return code_interpret(code_interpreter, tool_input["code"])
            return []
    

CopyCopied!

[5\. Create code interpreter and run everything](#5-create-code-interpreter-and-run-everything)

------------------------------------------------------------------------------------------------

Now we are ready to run our program. At the end of `main.py` add the following code prompting the LLM to visualize a distribution of the height of men and print the median.

### main.py

    def main():
      user_message = "Visualize a distribution of height of men based on the latest data you know. Also, print the median value."
    
      # Create the CodeInterpreter object and save it as code_interpreter
      with CodeInterpreter() as code_interpreter:
        code_interpreter_results, code_interpreter_logs = chat(
          code_interpreter,
          user_message,
        )
    
        print(code_interpreter_logs)
    
        first_result= code_interpreter_results[0]
        print(first_result)
    

CopyCopied!

After running your code with the following command

    $ python main.py
    

CopyCopied!

you should see results similar to this:

    stdout=['The median male height is 175.5 cm\n'] stderr=[]
    <Figure size 800x400 with 1 Axes>
    

CopyCopied!

We got our median in the logs (`stdout`, and `stderr`) but we also something intering in `first_result`.

    <Figure size 800x400 with 1 Axes>
    

CopyCopied!

[6\. Save generated chart](#6-save-generated-chart)

----------------------------------------------------

This looks like a plot. Let's save it to a file. Add the following to the end of `main.py` and run the code again with `python main.py` in your terminal.

### main.py

        # If we received a chart in PNG form, we can visualize it
        if first_result.png:
          # Decode the base64 encoded PNG data
          png_data = base64.b64decode(first_result.png)
    
          # Generate a unique filename for the PNG
          filename = f"chart.png"
    
          # Save the decoded PNG data to a file
          with open(filename, "wb") as f:
              f.write(png_data)
    
          print(f"Saved chart to {filename}")
    

CopyCopied!

The chart was saved in the `chart.png` file and it should look similar to this:

![Chart visualizing distribution height of men](/docs/_next/static/media/hello-world-chart.fd72ff25.png)Open source
===========

E2B is fully open source including the infrastructure layer.

*   [E2B monorepo containing the SDKs, CLI, and docs](https://github.com/e2b-dev/e2b)
    
*   [E2B infrastructure](https://github.com/e2b-dev/infra)
    
*   [Example code interpreter ChatGPT plugin](https://github.com/e2b-dev/llm-code-interpreter)
    
*   [List of awesome SDKs for AI agents](https://github.com/e2b-dev/awesome-sdks-for-ai-agents)
    
*   [List of awesome AI agents](https://github.com/e2b-dev/awesome-ai-agents)Pricing
=======

We charge you based on your real sandbox usage. All new users get one-time free $100 worth of usage in credits.

* * *

Plans pricing
=============

Additionally to the usage costs, you can also select a tier that includes dedicated support, prioritized features, and higher sandbox limits.

[Hobby tier](#hobby-tier)

--------------------------

**$0/month + usage costs**

[Sign Up](/docs/sign-in?view=sign-up)

*   One-time $100 of usage in credits
*   Community support
*   Up to 1 hour sandbox session length
*   Up to 20 concurrently running sandboxes

[Pro tier](#pro-tier)

----------------------

**$150/month + usage costs**

[Sign Up](/docs/sign-in?view=sign-up)

*   One-time $100 of usage in credits
*   Dedicated Slack channel with live Pro support from our team
*   Prioritized features
*   Customize your [sandbox compute](/docs/sandbox/compute)
    
*   Up to 24 hours sandbox session length
*   Up to 100 concurrently running sandboxes

If you need any additional features or resources, please [reach out to us](/docs/getting-help)
 with your use case.

* * *

Compute pricing
===============

We charge per second of a running sandbox.

*   vCPU: $0.000014 per second (~$0.05 per hour)
*   GiB RAM: $0.0000045 per second (~$0.018 per hour)
*   GiB storage: Free

1 GiB is equal to 1,024 MiB

[Sandbox compute](#sandbox-compute)

------------------------------------

Pro customers can customize the sandbox with **any combination** of the CPU and RAM based on the following tables.

**By default your sandbox has 2 vCPU and 512 MiB RAM.**

To customize your sandbox compute, you need to build your custom sandbox template using the [E2B CLI](/docs/cli/installation)
. Run [`e2b template build`](/docs/cli/commands#template-build)
 and specify the `--cpu-count` and `--memory-mb` options.

For example this custom build gives your sandbox 8 vCPU and 4GiB of RAM

    e2b template build --cput-count 8 --memory-mb 4096
    

CopyCopied!

### CPU

vCPUsPlan

Costs

1

Pro

$0.000014/s

2\[default\]

Hobby / Pro

$0.000028/s

3

Pro

$0.000042/s

4

Pro

$0.000056/s

5

Pro

$0.000070/s

6

Pro

$0.000084/s

7

Pro

$0.000098/s

8

Pro

$0.000112/s

### RAM

RAMPlan

Costs

512 MiB\[default\]

Hobby / Pro

**even** value **between 128 MiB** and **8,192 MiB**Pro

$0.0000045/GiB/s

### Storage

StoragePlan

Costs

1 GiBHobby

Free

5 GiBPro

Free

  

[Let us know](/docs/getting-help)
 if you need more powerful compute.Current Working Directory
=========================

You can set a working directory either for the whole sandbox, a filesystem operation, or a new process.

[Sandbox](#sandbox)

--------------------

If the current working directory for the sandbox is not set, it will default to the home directory - `/home/user`.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      cwd: '/code', 
    })
    
    // You can also change the cwd of an existing sandbox
    sandbox.cwd = '/home' 
    
    await sandbox.close()
    

CopyCopied!

[Filesystem](#filesystem)

--------------------------

All filesystem operations with relative paths are relative to the current working directory.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      cwd: '/home/user/code', 
    })
    
    await sandbox.filesystem.write('hello.txt', 'Welcome to E2B!') 
    const proc = await sandbox.process.start({
      cmd: 'cat /home/user/code/hello.txt',
    })
    await proc.wait()
    console.log(proc.output.stdout)
    // output: "Welcome to E2B!"
    
    await sandbox.filesystem.write('../hello.txt', 'We hope you have a great day!') 
    const proc2 = await sandbox.process.start({cmd: 'cat /home/user/hello.txt'})
    await proc2.wait()
    console.log(proc2.output.stdout)
    // output: "We hope you have a great day!"
    
    await sandbox.close()
    

CopyCopied!

[Process](#process)

--------------------

If you set a working directory for the sandbox, all processes will inherit it. You can override it for each process.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      cwd: '/code', 
    })
    
    const sandboxCwd = await sandbox.process.start({cmd: 'pwd'}) 
    await sandboxCwd.wait()
    console.log(sandboxCwd.output.stdout)
    // output: /code
    
    const processCwd = await sandbox.process.start({cmd: 'pwd', cwd: '/home'}) 
    await processCwd.wait()
    console.log(processCwd.output.stdout)
    // output: /home
    
    await sandbox.close()
    

CopyCopied!Logging
=======

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

E2B package logs only warnings & errors to the console by default. Below is an example of how to fully customize the logging levels. Feel free to override the logger with your own implementation with debug, info, warn, and error methods.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const logger = {
      debug: console.debug, // log debug messages, in default logger this is noop
      info: console.info, // log info messages, in default logger this is noop
      // don't forget to also specify warn & error handlers, otherwise they won't be logged when overriding the logger
      warn: console.warn,
      error: console.error,
    }
    
    const sandbox = await Sandbox.create({
      template: 'base',
      apiKey: process.env.E2B_API_KEY,
      logger, 
    })
    

CopyCopied!Download files from the sandbox
===============================

Any file inside the sandbox can be downloaded using the `downloadFile`/`download_file` method.

[Use case for downloading files](#use-case-for-downloading-files)

------------------------------------------------------------------

For example, the download file method is useful for downloading any files produced by LLM. You can let LLM generate and execute code inside the sandbox. This LLM-generated code might produce some files like charts, CSV files, or PDF files that you want to download to your machine.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    import fs from 'node:fs'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    const buffer = await sandbox.downloadFile('path/to/remote/file/inside/sandbox') 
    // Save file to local filesystem
    fs.writeFileSync('path/to/local/file', buffer)
    
    await sandbox.close()
    

CopyCopied!Setting environment variables
=============================

[Global environment variables](#global-environment-variables)

--------------------------------------------------------------

You can set the sandbox's global environment variables when initializing a new sandbox.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      envVars: {FOO: 'Hello'}, 
    })
    
    await sandbox.close()
    

CopyCopied!

[Environment variables per process](#environment-variables-per-process)

------------------------------------------------------------------------

Alternatively, you can set environment variables when starting a new process. These environment variables are accessible only for this process.

Environment variables set when starting a new process have precedence over the environment variables set when initializing the sandbox.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      envVars: {FOO: 'Hello'},
    })
    
    const proc = await sandbox.process.start({
      cmd: 'echo $FOO $BAR!',
      envVars: {BAR: 'World'}, 
    })
    await proc.wait()
    console.log(proc.output.stdout)
    // output: Hello World!
    
    await sandbox.close()
    

CopyCopied![List directory](#list-directory)

----------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
    })
    
    const dirContent = await sandbox.filesystem.list('/') 
    dirContent.forEach((item) => {
      console.log(item.name)
    })
    
    await sandbox.close()
    

CopyCopied!

[Create directory](#create-directory)

--------------------------------------

Create directory and all parent directories.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // Create a new directory '/dir'
    await sandbox.filesystem.makeDir('/dir') 
    
    await sandbox.close()
    

CopyCopied!

[Write to file](#write-to-file)

--------------------------------

When writing to a file that doesn't exist, the file will get created.

When writing to a file that already exists, the file will get overwritten.

When writing to a file that's in a directory that doesn't exist, you'll get an error.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // `filesystem.write()` will:
    // - create the file if it doesn't exist
    // - fail if any directory in the path doesn't exist
    // - overwrite the file if it exists
    
    // Write the content of the file '/hello.txt'
    await sandbox.filesystem.write('/hello.txt', 'Hello World!') 
    
    // The following would fail because '/dir' doesn't exist
    // await sandbox.filesystem.write("/dir/hello.txt", "Hello World!")
    
    await sandbox.close()
    

CopyCopied!

[Read from file](#read-from-file)

----------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    const fileContent = await sandbox.filesystem.read('/etc/hosts') 
    console.log(fileContent)
    
    await sandbox.close()
    

CopyCopied!

[Write bytes](#write-bytes)

----------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // Let's convert string to bytes for testing purposes
    const encoder = new TextEncoder('utf-8')
    const contentInBytes = encoder.encode('Hello World!')
    
    // `writeBytes` accepts a Uint8Array and saves it to a file inside the playground
    await sandbox.filesystem.writeBytes('/file', contentInBytes) 
    
    // We can read the file back to verify the content
    const fileContent = await sandbox.filesystem.read('/file')
    
    // This will print 'Hello World!'
    console.log(fileContent)
    
    await sandbox.close()
    

CopyCopied!

[Read bytes](#read-bytes)

--------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import fs from 'fs'
    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // File bytes will read file's content as bytes
    // `fileBytes` as a Uint8Array
    const fileBytes = await sandbox.filesystem.readBytes('/etc/hosts') 
    
    // The output will look similar to this:
    // <Buffer 31 32 37 2e 30 2e 30 2e 31 09 6c 6f 63 61 6c 68 6f 73  ...
    console.log(fileBytes)
    
    // We can save those bytes to a file locally like this:
    fs.writeFileSync('hosts', fileBytes)
    
    await sandbox.close()
    

CopyCopied!

[Watch directory for changes](#watch-directory-for-changes)

------------------------------------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // Start filesystem watcher for the /home directory
    const watcher = sandbox.filesystem.watchDir('/home') 
    watcher.addEventListener((event) => {
      
      console.log('Filesystem event', event) 
    }) 
    await watcher.start() 
    
    // Create files in the /home directory inside the playground
    // We'll receive notifications for these events through the watcher we created above.
    for (let i = 0; i < 10; i++) {
      console.log('Creating file', i)
      // `filesystem.write()` will trigger two events:
      // 1. 'Create' when the file is created
      // 2. 'Write' when the file is written to
      await sandbox.filesystem.write(`/home/${i}.txt`, `Hello World ${i}!`)
    }
    
    await sandbox.close()
    

CopyCopied![Sandbox metadata](#sandbox-metadata)

--------------------------------------

You can assign metadata to your sandbox. This metadata will be available if you call `Sandbox.list()`. This can be useful in situation where each of your users have dedicated sandbox and the time between the steps of the integration is long. You can use the metadata to store the user id and reconnect to it later.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      metadata: { userID: 'uniqueID' }   
    })
    // Keep the sandbox alive for 60 seconds
    await sandbox.keepAlive(60_000)
    // You can even close the script
    
    // Later, can be even from another process
    // List all running sandboxes
    const runningSandboxes = await Sandbox.list()
    // Find the sandbox by metadata
    const found = runningSandboxes.find(s => s.metadata?.userID === 'uniqueID')
    if (found) {
      // Sandbox found, we can reconnect to it
      const sandbox = await Sandbox.reconnect(found.sandboxID)
    } else {
      // Sandbox not found
    }
    
    await sandbox.close()
    

CopyCopied!Starting process inside a sandbox
=================================

Here are the basic operations you can do with the process inside the sandbox:

*   [Start process](/docs/sandbox/api/process#start-process)
    
*   [Stop process](/docs/sandbox/api/process#stop-process)
    
*   [Stdout](/docs/sandbox/api/process#stream-stdout)
    
*   [Stdin](/docs/sandbox/api/process#send-stdin)
    
*   [Stderr](/docs/sandbox/api/process#stream-stderr)
    
*   [On exit](/docs/sandbox/api/process#on-process-exit)
    

[Start process](#start-process)

--------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    const npmInit = await sandbox.process.start({
      cmd: 'npm init -y', 
    })
    await npmInit.wait()
    
    console.log(npmInit.output.stdout)
    
    await sandbox.close()
    

CopyCopied!

[Stop process](#stop-process)

------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
    })
    
    const npmInit = await sandbox.process.start({
      cmd: 'npm init -y',
    })
    await npmInit.kill() 
    // There will be no output because we immediately kill the `npm_init` process
    console.log(npmInit.output.stdout)
    
    await sandbox.close()
    

CopyCopied!

[Stream stdout](#stream-stdout)

--------------------------------

Set either stdout handler for the whole sandbox level or per process.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      onStdout: (output) => console.log('sandbox', output.line), 
    })
    
    const proc = await sandbox.process.start({
      cmd: 'echo "Hello World!"',
    })
    await proc.wait()
    // output: sandbox Hello World!
    
    const procWithCustomHandler = await sandbox.process.start({
      cmd: 'echo "Hello World!"',
      onStdout: (data) => console.log('process', data.line), 
    })
    await procWithCustomHandler.wait()
    // output: process Hello World!
    
    await sandbox.close()
    

CopyCopied!

[Stream stderr](#stream-stderr)

--------------------------------

Set either stderr handler for the whole sandbox level or per process.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
    })
    
    // This command will fail and output to stderr because Golang isn't installed in the cloud playground
    const golangVersion = await sandbox.process.start({
      cmd: 'go version',
      onStderr: (output) => console.log('sandbox', output.line), 
    })
    await golangVersion.wait()
    // output: [sandbox] /bin/bash: line 1: go: command not found
    
    const procWithCustomHandler = await sandbox.process.start({
      cmd: 'go version',
      onStderr: (data) => console.log('process', data.line), 
    })
    await procWithCustomHandler.wait()
    // output: process /bin/bash: line 1: go: command not found
    
    await sandbox.close()
    

CopyCopied!

[On process exit](#on-process-exit)

------------------------------------

Set either on exit handler for the whole sandbox level or per process.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({
      template: 'base',
      onExit: () => console.log('[sandbox]', 'process ended'), 
    })
    
    const proc = await sandbox.process.start({cmd: 'echo "Hello World!"'})
    await proc.wait()
    // output: [sandbox] process ended
    
    const procWithCustomHandler = await sandbox.process.start({
      cmd: 'echo "Hello World!"',
      onExit: () => console.log('[process]', 'process ended'), 
    })
    await procWithCustomHandler.wait()
    // output: [process] process ended
    
    await sandbox.close()
    

CopyCopied!

[Send stdin](#send-stdin)

--------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // This example will print back the string we send to the process using `sendStdin()`
    
    const proc = await sandbox.process.start({
      cmd: 'while IFS= read -r line; do echo "$line"; sleep 1; done',
      onStdout: (output) => console.log(output),
    })
    await proc.sendStdin('AI Playground\n') 
    await proc.kill()
    
    await sandbox.close()
    

CopyCopied!Connect to running sandbox
==========================

Disconnect and reconnect later to the same sandbox while keeping it alive

[Description](#description)

----------------------------

The sandboxes are by default kept alive only when connected to them. When you disconnect from a sandbox, it will be destroyed.

If you want to keep the sandbox alive even after disconnecting from it, you can explicitly say for how long you want to keep it alive. You can then disconnect from the sandbox and reconnect to it later. This can be useful for example in a **serverless environment** or **chatbot application**.

The duration limit to keep the sandbox alive is 1 hour. If you need more, feel free to [reach out to us](/docs/getting-help)
 with your use.

[Keep sandbox alive](#keep-sandbox-alive)

------------------------------------------

The example below shows how to disconnect from a running sandbox and reconnect to it again while keeping the sandbox alive.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    async function wait(ms) {
      return new Promise(resolve => setTimeout(resolve, ms))
    }
    
    const sandbox = await Sandbox.create({ template: 'base' })
    

CopyCopied!

Call the `keep_alive`/`keepAlive` method on the sandbox instance to keep it alive. You can specify the preferred duration, as a multiple of a default time unit, which is

*   1ms in JS
*   1s in Python.

You then disconnect from the sandbox.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    // Do something in the sandbox
    await sandbox.filesystem.write('hello.txt', 'Hello World!')
    
    // Get the sandbox ID, we'll need it later
    const sandboxID = sandbox.id
    
    // Keep alive the sandbox for 2 minutes
    await sandbox.keepAlive(2 * 60 * 1000) 
    
    // Close the sandbox. Even if we close the sandbox, it will stay alive, because we explicitly called keepAlive().
    await sandbox.close()
    
    // Do something else...
    await wait(60 * 1000)
    

CopyCopied!

You can then reconnect to the sandbox from anywhere.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    // Reconnect to the sandbox
    const sandbox2 = await Sandbox.reconnect(sandboxID) 
    
    // Continue in using the sandbox
    const content = await sandbox2.filesystem.read('hello.txt')
    console.log(content)
    
    // Close the sandbox
    await sandbox2.close()
    

CopyCopied!

[Use sandbox metadata](#use-sandbox-metadata)

----------------------------------------------

Sandbox metadata can be very useful to store information about the sandbox. You can use it to store the user ID or any other information you need to keep track of and then use this info for reconnecting to the sandbox. You can read more about sandbox metadata [here](/docs/sandbox/api/metadata)
.Timeouts
========

The SDK has a number of timeouts that can be configured to control how long the SDK will wait for a response from the E2B servers. **The default is 60 seconds.**

[Timeout creating sandbox](#timeout-creating-sandbox)

------------------------------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    // Timeout 3s for the sandbox to open
    const sandbox = await Sandbox.create({
      template: 'base',
      timeout: 3000, 
    })
    
    await sandbox.close()
    

CopyCopied!

[Timeout process](#timeout-process)

------------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // Timeout 3s for the process to start
    const npmInit = await sandbox.process.start({
      cmd: 'npm init -y',
      timeout: 3000, 
    })
    await npmInit.wait()
    
    await sandbox.close()
    

CopyCopied!

[Timeout filesystem operations](#timeout-filesystem-operations)

----------------------------------------------------------------

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // Timeout 3s for the write operation
    await sandbox.filesystem.write('hello.txt', 'Hello World!', {timeout: 3000}) 
    
    // Timeout 3s for the list operation
    const files = await sandbox.filesystem.list('.', {timeout: 3000}) 
    console.log(files)
    
    // Timeout 3s for the read operation
    const content = await sandbox.filesystem.read('hello.txt', {timeout: 3000}) 
    console.log(content)
    
    await sandbox.close()
    

CopyCopied!Upload files to sandbox
=======================

You can upload any file to the sandbox. This is useful if you want to let the LLM work with your files or files of your users. The file will be uploaded to the user's home directory with the same name. If a file with the same name already exists, it will be overwritten.

[Use case for uploading files](#use-case-for-uploading-files)

--------------------------------------------------------------

A popular workflow is for example to upload a CSV data file and then let the LLM generate and execute Python code that operates with the uploaded CSV file inside the sandbox. This way, you can essentially create your own AI data analyst or code interpreter.

We support uploading files up to 100MB at the moment. If you need to upload larger files, please [reach out to us](/docs/getting-help)
.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    import fs from 'node:fs'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    // If you're in the server environment
    const filename = 'data.csv' 
    const fileBuffer = fs.readFileSync('path/to/local/file') 
    const remotePath = await sandbox.uploadFile(fileBuffer, filename) 
    
    // If you're in the browser environment, you can use the Blob API
    // const filename = 'data.csv'
    // const CSV = [\
    //   '"1","val1","val2","val3","val4"',\
    //   '"2","val1","val2","val3","val4"',\
    //   '"3","val1","val2","val3","val4"'\
    // ].join('\n');
    // const fileBlob = new Blob([csv], { type: 'text/csv' })
    // const remotePath = await sandbox.uploadFile(fileBlob, 'data.csv')
    
    console.log(
      `The file was uploaded to '${remotePath}' path inside the sandbox `,
    )
    
    await sandbox.close()
    

CopyCopied!Sandbox URL
===========

Each sandbox has its own URL that you can use to connect to any service running inside the sandbox.

For example, you can start a server inside the sandbox and connect to it from your browser.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    const url = sandbox.getHostname() 
    console.log('https://' + url)
    
    await sandbox.close()
    

CopyCopied!

If you want to get an URL for a specific port inside the sandbox, pass the port number to the `getHostname()`/`get_hostname()` method.

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create({ template: 'base' })
    
    const openPort = 3000
    const url = sandbox.getHostname(openPort) 
    console.log('https://' + url)
    
    await sandbox.close()
    

CopyCopied!Sandbox compute
===============

Pro customers can customize the sandbox with **any combination** of the CPU and RAM based on the following tables.

Read a dedicated page to [learn more about pricing](/docs/pricing)
.

**By default your sandbox has 2 vCPU and 512 MiB RAM.**

To customize your sandbox compute, you need to build your custom sandbox template using the [E2B CLI](/docs/cli/installation)
. Run [`e2b template build`](/docs/cli/commands#template-build)
 and specify the `--cpu-count` and `--memory-mb` options.

For example, this custom build command gives your sandbox 8 vCPU and 4GiB of RAM

    e2b template build --cput-count 8 --memory-mb 4096
    

CopyCopied!

### CPU

vCPUsPlan

Costs

1

Pro

$0.000014/s

2\[default\]

Hobby / Pro

$0.000028/s

3

Pro

$0.000042/s

4

Pro

$0.000056/s

5

Pro

$0.000070/s

6

Pro

$0.000084/s

7

Pro

$0.000098/s

8

Pro

$0.000112/s

### RAM

RAMPlan

Costs

512 MiB\[default\]

Hobby / Pro

**even** value **between 128 MiB** and **8,192 MiB**Pro

$0.0000045/GiB/s

### Storage

StoragePlan

Costs

1 GiBHobby

Free

5 GiBPro

Free

  

[Let us know](/docs/getting-help)
 if you need more powerful compute.Customizing Sandbox
===================

Custom sandboxes allows you to spawn a sandbox with a pre-defined environment by you and then control it with our SDK.

You can build a custom sandbox by creating the [Sandbox Template](/docs/sandbox/templates/overview)
. Sandbox template is a Dockerfile that describes the environment of your sandbox.

Once you build your custom sandbox template, you can spawn multiple isolated sandboxes from it.

[How it works](#how-it-works)

------------------------------

1.  [Provide the sandbox template file](/docs/sandbox/templates/template-file)
    
2.  [Build a sandbox template from it using our CLI](/docs/guide/custom-sandbox#4-build-custom-sandbox)
    
3.  Get a template ID from the CLI:
    
        # ... truncated CLI output
        ✅ Building sandbox template 3y5bvra6kgq0kaumgztu finished.
        
    
    CopyCopied!
    
4.  Pass the template ID to our SDK like this:
    
    ### Using custom sandbox with SDK
    
    ![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript
    
    ![](/docs/_next/static/media/python.c624d255.svg)Python
    
        import { Sandbox } from 'e2b'
        
        // Create new sandbox
        const sandbox = await Sandbox.create({
          template: '<sandbox-template-id>', // You get sandbox template ID from the CLI after you run `$ e2b build`
        })
        
        // Close sandbox once done
        await sandbox.close()
        
    
    CopyCopied!
    
5.  Run the code and we spawn a sandbox based on the template you built in step 2
    

Now you can do step 4/5 multiple times using the same ID, always creating a separate sandbox instance.

Read more on [Sandbox Templates](/docs/sandbox/templates/overview)
 if you want to create your own custom sandbox.Overview
========

**The E2B's sandboxes are isolated cloud environments made specifcially for AI code interpreting or code execution.**

The E2B sandboxes are an ideal fit as a playground for AI assistants like coding copilots, code interpreters, AI data analysts, AI browser assistants, and other AI-powered apps.

[Features](#features)

----------------------

[Open-source](https://github.com/e2b-dev/e2b)
 sandbox for LLMA full VM environmentNo need for orchestration or infrastructure managementAbility to give each user of your AI app their own isolated environment[Python & Node.js SDK](/docs/getting-started/installation)
 for controling the sandbox's [filesystem](/docs/sandbox/api/filesystem)
, [processes](/docs/sandbox/api/process)
, and more.Support for up to 24h long-running sandbox sessionsAbility to [upload files](/docs/sandbox/api/upload)
 to the sandbox and [download files](/docs/sandbox/api/download)
 from the sandbox,

With more features coming in the future:

*   Out-of-the box working monitoring of what's happening inside the sandbox
*   LLM Access control to data, tools, and any internet requests
*   Statefull sandboxes
*   Resumable workflows (pause sandbox and load it later)
*   Unlimited long-running sandboxed

[Comparison to other services](#comparison-to-other-services)

--------------------------------------------------------------

With LLMs, it's not safe to let the LLM run code and use tools in the same environment where your application is running.

You need to isolate the LLM from the rest of your app and make sure that the LLM can't access your data, tools, and the internet without you knowing about it or giving it explicit access. You need to make sure that the LLM can run untrusted code safely and install libraries on fly. The AI apps also often need to run for a long time, and need to be resumable - for example, when waiting for user's consent to make an internet purchase, you need to be able to pause the AI app and resume it later without losing the whole state.

Additionally, the AI apps present need for a new model:

*   How can every user of your AI app have the environment described above for themselves?
*   How can developers easily manage and orchestrate these environments?
*   How can developers easily debug these environments?
*   How to let LLMs use use the same tools as humans do on their computers (for example browser, code linters, autocomplete, etc)?
*   How can developers easily monitor what's happening inside these environments?
*   How to scale these environments to billions of instances?

![Separate E2B Sandbox for each instance of your AI app](/docs/_next/static/media/ai-app-e2b-sandbox-model.2d1c1c88.png)

E2B Sandboxes are made exactly to solve these challenges. The sandbox is like an isolated runtime or playground for the LLM. **We give you our SDK to spawn and control these sandboxes.**

[How sandboxes work under the hood](#how-sandboxes-work-under-the-hood)

------------------------------------------------------------------------

When you create a new sandbox session, we start a small VM in our cloud. This VM is running a Ubuntu OS and it takes about 400-600ms to start it.

Inside this sandbox, your AI app can [run code and start any programs](/docs/sandbox/api/process)
, access the internet to download or upload data, use the [filesystem](/docs/sandbox/api/filesystem)
, start long running processes such as web servers, and more. You can also [upload](/docs/sandbox/api/upload)
 to sandbox and [download](/docs/sandbox/api/upload)
 from sandbox any file you want.

To start and control the sandbox, use the [E2B SDK](/docs/getting-started/installation)
 for Python or JavaScript.

### Starting Sandbox

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    const sandbox = await Sandbox.create()
    
    await sandbox.close()
    

CopyCopied!

Make sure you have the `E2B_API_KEY` environment variable set with your [API key](/docs/getting-started/api-key)
.Custom Sandbox
==============

Custom sandboxes allow you to spawn a sandbox with an environment predefined by you and then control it with our SDK.

The E2B Sandbox is a secure way to run your AI app. It is a long-running cloud environment where you can let any LLM (GPTs, Claude, local LLMs, etc) use tools exactly like you would do locally.

Read more about E2B Sandboxes [here](/docs/sandbox/overview)
.

[How Custom Sandboxes Work](#how-custom-sandboxes-work)

--------------------------------------------------------

Follow our [guide](/docs/guide/custom-sandbox)
 on how to create a custom sandbox.

1.  You build a custom sandbox by creating the [Sandbox Template](/docs/sandbox/templates/template-file)
     which is a Dockerfile describing the environment of your sandbox.
    
2.  Build a sandbox template from it using our CLI
    
3.  Get a template ID from the CLI:
    
        # ... truncated CLI output
        ✅ Building sandbox template 3y5bvra6kgq0kaumgztu finished.
        
    
    CopyCopied!
    
4.  Pass the template ID to our SDK like this:
    
    ### Using custom sandbox with SDK
    
    ![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript
    
    ![](/docs/_next/static/media/python.c624d255.svg)Python
    
        import { Sandbox } from 'e2b'
        
        // Create new sandbox
        const sandbox = await Sandbox.create({
          // You get sandbox template from the CLI after you run `$ e2b build`
          template: '<sandbox-template>',  
        })
        
        // Close sandbox once done
        await sandbox.close()
        
    
    CopyCopied!
    
5.  Run the code and we spawn a sandbox based on the template you built in step 2
    

Once you build your custom sandbox template, you can spawn multiple isolated sandboxes from it. You can repeat the steps 4, 5 multiple times using the same ID, always creating a separate sandbox instance.

![Graphics explaining how custom sandbox works](/docs/_next/static/media/custom-sandbox.86e0f97b.png)

Follow [our guide](/docs/guide/custom-sandbox)
 on how to create a custom sandbox.Start Command
=============

The start command allows you to specify a command that will be **already running** when you spawn your custom sandbox. This way, you can for example have running servers or seeded databases inside the sandbox that are already fully ready when you spawn the sandbox using the SDK and with zero waiting time for your users during the runtime.

The idea behind the start command feature is to lower the wait times for your users and have everything ready for your users when you spawn your sandbox.

[How to add start command](#how-to-add-start-command)

------------------------------------------------------

When you are building a sandbox template you can specify the start command by using the [`-c`](/docs/cli/commands#build)
 option:

    e2b build -c "<your-start-command>"
    

CopyCopied!

When you spawn the custom sandbox you built, the start command will be already running if there was no error when we tried to execute it.

[How it works](#how-it-works)

------------------------------

Every time you are building a [custom sandbox](/docs/guide/custom-sandbox)
, we create a container based on the [`e2b.Dockerfile`](/docs/sandbox/templates/template-file)
 file you create in the process. We extract the container's filesystem and start a sandbox with this extracted filesystem. We call this sandbox a _template sandbox_.

Then, these steps happen:

1.  We take the running template sandbox.
2.  (Only if you specified the start command, otherwise this step is skipped) **Execute the start command and wait 15 seconds**.
3.  Snapshot the sandbox and make it ready for you to spawn it with the SDK.

Sandbox Snapshot

Snapshots are saved running sandboxes. We serialize and save the whole sandbox's filesystem together with all the running processes in a way that can be loaded later.

This allows us to load the sandbox in a few hundred milliseconds any time later with all the processes already running and the filesystem exactly as it was.

[Limits](#limits)

------------------

*   The network isn't accessible when running the start command.
*   We wait 15 seconds after we execute the start command before we snapshot the sandbox.

[Logs](#logs)

--------------

You can retrieve the start command's logs using the SDK during runtime:

### Check start command logs

![](/docs/_next/static/media/node.ffbff9e8.svg)JavaScript & TypeScript

![](/docs/_next/static/media/python.c624d255.svg)Python

    import { Sandbox } from 'e2b'
    
    // Spawn your custom sandbox
    const sandbox = await Sandbox.create({
      id: 'my-agent-sandbox',
      // If you specify onStderr and onStdout handlers when spawning the sandbox
      // you will see logs from the start command.
      onStderr: output => console.log("stderr", output.line), 
      onStdout: output => console.log("stdout", output.line), 
    })
    
    // Close sandbox once done
    await sandbox.close()
    

CopyCopied!

[Sandbox template config](#sandbox-template-config)

----------------------------------------------------

The start command is specified inside the `e2b.toml` in the same directory where you ran `e2b build -c "<your-start-command>"`.

### e2b.toml

    # This is a config for E2B sandbox template
    template_id = "1wdqsf9le9gk21ztb4mo"
    dockerfile = "e2b.Dockerfile"
    template_name = "my-agent-sandbox"
    start_cmd = "<your-start-command>"  
    

CopyCopied!Template File
=============

The template file is a Dockerfile named `e2b.Dockerfile`. The template file is used to define an environment for your custom sandbox.

Follow our [guide](/docs/guide/custom-sandbox)
 on how to create a custom sandbox.

![Graphics explaining how custom sandbox works](/docs/_next/static/media/custom-sandbox.86e0f97b.png)

[`e2b.Dockerfile`](#e2b-dockerfile)

------------------------------------

The Dockerfile must be Debian based (e.g. Ubuntu). Only the following [Dockerfile commands](https://docs.docker.com/engine/reference/builder/)
 are supported:

*   `FROM`
*   `ADD`
*   `COPY`
*   `RUN`
*   `WORKDIR`

[Example](#example)

--------------------

The following example template file defines a Ubuntu-based sandbox with installed GitHub CLI.

### e2b.Dockerfile

    # You can use most of the Debian-based base images
    FROM ubuntu:22.04
    
    # Install dependencies and customize sandbox
    RUN apt update \
    	&& apt install sudo
    
    # Install GitHub CLI
    RUN type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
    RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    	&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    	&& sudo apt update \
    	&& sudo apt install gh -y
    

CopyCopied!Supported LLMs and AI frameworks
================================

E2B is LLM agnostic - it supports any LLM models and any AI frameworks.

Usually, all you need from the model is just support for tool use. You then use the E2B code interpreter as a tool. If the LLM doesn't support tool use, you can ask the LLM to respond with Markdown or XML and parse the LLM's output on your own. Then just pass the parsed code from code blocks to the code interpreter.

Check out our [cookbook](https://github.com/e2b-dev/e2b-cookbook)
 for examples.