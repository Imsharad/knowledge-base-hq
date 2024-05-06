[Skip to main content](#__docusaurus_skipToContent_fallback)

On this page

🦜🕸️LangGraph
==============

[![Downloads](https://static.pepy.tech/badge/langgraph/month)](https://pepy.tech/project/langgraph)
 [![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraph)](https://github.com/langchain-ai/langgraph/issues)
 [![](https://dcbadge.vercel.app/api/server/6adMQxSpJS?compact=true&style=flat)](https://discord.com/channels/1038097195422978059/1170024642245832774)
 [![Docs](https://img.shields.io/badge/docs-latest-blue)](https://langchain-ai.github.io/langgraph/)

⚡ Building language agents as graphs ⚡

Overview[​](#overview "Direct link to Overview")

-------------------------------------------------

[LangGraph](https://langchain-ai.github.io/langgraph/)
 is a library for building stateful, multi-actor applications with LLMs. It extends the [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
 with the ability to coordinate multiple chains (or actors) across multiple steps of computation in a cyclic manner. It is inspired by [Pregel](https://research.google/pubs/pub37252/)
 and [Apache Beam](https://beam.apache.org/)
. The current interface exposed is one inspired by [NetworkX](https://networkx.org/documentation/latest/)
.

The main use is for adding **cycles** to your LLM application. Crucially, LangGraph is NOT optimized for only **DAG** workflows. If you want to build a DAG, you should just use [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
.

Cycles are important for agent-like behaviors, where you call an LLM in a loop, asking it what action to take next.

Installation[​](#installation "Direct link to Installation")

-------------------------------------------------------------

    pip install langgraph

Quick start[​](#quick-start "Direct link to Quick start")

----------------------------------------------------------

One of the central concepts of LangGraph is state. Each graph execution creates a state that is passed between nodes in the graph as they execute, and each node updates this internal state with its return value after it executes. The way that the graph updates its internal state is defined by either the type of graph chosen or a custom function.

State in LangGraph can be pretty general, but to keep things simpler to start, we'll show off an example where the graph's state is limited to a list of chat messages using the built-in `MessageGraph` class. This is convenient when using LangGraph with LangChain chat models because we can return chat model output directly.

First, install the LangChain OpenAI integration package:

    pip install langchain_openai

We also need to export some environment variables:

    export OPENAI_API_KEY=sk-...

And now we're ready! The graph below contains a single node called `"oracle"` that executes a chat model, then returns the result:

    from langchain_openai import ChatOpenAIfrom langchain_core.messages import HumanMessagefrom langgraph.graph import END, MessageGraphmodel = ChatOpenAI(temperature=0)graph = MessageGraph()graph.add_node("oracle", model)graph.add_edge("oracle", END)graph.set_entry_point("oracle")runnable = graph.compile()

#### API Reference:

*   [ChatOpenAI](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
    
*   [HumanMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.human.HumanMessage.html)
    

Let's run it!

    runnable.invoke(HumanMessage("What is 1 + 1?"))

    [HumanMessage(content='What is 1 + 1?'), AIMessage(content='1 + 1 equals 2.')]

So what did we do here? Let's break it down step by step:

1.  First, we initialize our model and a `MessageGraph`.
2.  Next, we add a single node to the graph, called `"oracle"`, which simply calls the model with the given input.
3.  We add an edge from this `"oracle"` node to the special string `END`. This means that execution will end after current node.
4.  We set `"oracle"` as the entrypoint to the graph.
5.  We compile the graph, ensuring that no more modifications to it can be made.

Then, when we execute the graph:

1.  LangGraph adds the input message to the internal state, then passes the state to the entrypoint node, `"oracle"`.
2.  The `"oracle"` node executes, invoking the chat model.
3.  The chat model returns an `AIMessage`. LangGraph adds this to the state.
4.  Execution progresses to the special `END` value and outputs the final state.

And as a result, we get a list of two chat messages as output.

### Interaction with LCEL[​](#interaction-with-lcel "Direct link to Interaction with LCEL")

As an aside for those already familiar with LangChain - `add_node` actually takes any function or runnable as input. In the above example, the model is used "as-is", but we could also have passed in a function:

    def call_oracle(messages: list):    return model.invoke(messages)graph.add_node("oracle", call_oracle)

Just make sure you are mindful of the fact that the input to the runnable is the **entire current state**. So this will fail:

    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderprompt = ChatPromptTemplate.from_messages([    ("system", "You are a helpful assistant named {name} who always speaks in pirate dialect"),    MessagesPlaceholder(variable_name="messages"),])chain = prompt | modelgraph.add_node("oracle", chain)

#### API Reference:

*   [ChatPromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html)
    
*   [MessagesPlaceholder](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html)
    

Conditional edges[​](#conditional-edges "Direct link to Conditional edges")

----------------------------------------------------------------------------

Now, let's move onto something a little bit less trivial. Because math can be difficult for LLMs, let's allow the LLM to conditionally call a `"multiply"` node using tool calling.

We'll recreate our graph with an additional `"multiply"` that will take the result of the most recent message, if it is a tool call, and calculate the result. We'll also [bind](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html#langchain_openai.chat_models.base.ChatOpenAI.bind_tools)
 the calculator to the OpenAI model as a tool to allow the model to optionally use the tool necessary to respond to the current state:

    from langchain_core.tools import toolfrom langgraph.prebuilt import ToolNode@tooldef multiply(first_number: int, second_number: int):    """Multiplies two numbers together."""    return first_number * second_numbermodel = ChatOpenAI(temperature=0)model_with_tools = model.bind_tools([multiply])graph = MessageGraph()graph.add_node("oracle", model_with_tools)tool_node = ToolNode([multiply])graph.add_node("multiply", tool_node)graph.add_edge("multiply", END)graph.set_entry_point("oracle")

#### API Reference:

*   [tool](https://api.python.langchain.com/en/latest/tools/langchain_core.tools.tool.html)
    

Now let's think - what do we want to have happened?

*   If the `"oracle"` node returns a message expecting a tool call, we want to execute the `"multiply"` node
*   If not, we can just end execution

We can achieve this using **conditional edges**, which routes execution to a node based on the current state using a function.

Here's what that looks like:

    def router(state: List[BaseMessage]):    tool_calls = state[-1].additional_kwargs.get("tool_calls", [])    if len(tool_calls):        return "multiply"    else:        return "end"graph.add_conditional_edges("oracle", router, {    "multiply": "multiply",    "end": END,})

If the model output contains a tool call, we move to the `"multiply"` node. Otherwise, we end.

Great! Now all that's left is to compile the graph and try it out. Math-related questions are routed to the calculator tool:

    runnable = graph.compile()runnable.invoke(HumanMessage("What is 123 * 456?"))

    [HumanMessage(content='What is 123 * 456?'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_OPbdlm8Ih1mNOObGf3tMcNgb', 'function': {'arguments': '{"first_number":123,"second_number":456}', 'name': 'multiply'}, 'type': 'function'}]}), ToolMessage(content='56088', tool_call_id='call_OPbdlm8Ih1mNOObGf3tMcNgb')]

While conversational responses are outputted directly:

    runnable.invoke(HumanMessage("What is your name?"))

    [HumanMessage(content='What is your name?'), AIMessage(content='My name is Assistant. How can I assist you today?')]

Cycles[​](#cycles "Direct link to Cycles")

-------------------------------------------

Now, let's go over a more general example with a cycle. We will recreate the `AgentExecutor` class from LangChain. The agent itself will use chat models and function calling. This agent will represent all its state as a list of messages.

We will need to install some LangChain packages, as well as [Tavily](https://app.tavily.com/sign-in)
 to use as an example tool.

    pip install -U langchain langchain_openai tavily-python

We also need to export some additional environment variables for OpenAI and Tavily API access.

    export OPENAI_API_KEY=sk-...export TAVILY_API_KEY=tvly-...

Optionally, we can set up [LangSmith](https://docs.smith.langchain.com/)
 for best-in-class observability.

    export LANGCHAIN_TRACING_V2="true"export LANGCHAIN_API_KEY=ls__...

### Set up the tools[​](#set-up-the-tools "Direct link to Set up the tools")

As above, we will first define the tools we want to use. For this simple example, we will use a built-in search tool via Tavily. However, it is really easy to create your own tools - see documentation [here](https://python.langchain.com/docs/modules/agents/tools/custom_tools)
 on how to do that.

    from langchain_community.tools.tavily_search import TavilySearchResultstools = [TavilySearchResults(max_results=1)]

#### API Reference:

*   [TavilySearchResults](https://api.python.langchain.com/en/latest/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
    

We can now wrap these tools in a simple LangGraph `ToolExecutor`. This class receives `ToolInvocation` objects, calls that tool, and returns the output. `ToolInvocation` is any class with `tool` and `tool_input` attributes.

    from langgraph.prebuilt import ToolExecutortool_executor = ToolExecutor(tools)

### Set up the model[​](#set-up-the-model "Direct link to Set up the model")

Now we need to load the chat model we want to use. This time, we'll use the older function calling interface. This walkthrough will use OpenAI, but we can choose any model that supports OpenAI function calling.

    from langchain_openai import ChatOpenAImodel = ChatOpenAI(temperature=0, streaming=True)

#### API Reference:

*   [ChatOpenAI](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
    

After we've done this, we should make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI tool calling using the [`bind_tools()`](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html#langchain_openai.chat_models.base.ChatOpenAI.bind_tools)
 method.

    model = model.bind_tools(tools)

### Define the agent state[​](#define-the-agent-state "Direct link to Define the agent state")

This time, we'll use the more general `StateGraph`. This graph is parameterized by a state object that it passes around to each node. Remember that each node then returns operations to update that state. These operations can either SET specific attributes on the state (e.g. overwrite the existing values) or ADD to the existing attribute. Whether to set or add is denoted by annotating the state object you construct the graph with.

For this example, the state we will track will just be a list of messages. We want each node to just add messages to that list. Therefore, we will use a `TypedDict` with one key (`messages`) and annotate it so that the `messages` attribute is always added to with the second parameter (`operator.add`). (Note: the state can be any [type](https://docs.python.org/3/library/stdtypes.html#type-objects)
, including [pydantic BaseModel's](https://docs.pydantic.dev/latest/api/base_model/)
).

    from typing import TypedDict, Annotatedfrom langgraph.graph.message import add_messagesclass AgentState(TypedDict):            messages: Annotated[list, add_messages]

You can think of the `MessageGraph` used in the initial example as a preconfigured version of this graph, where the state is directly an array of messages, and the update step is always to append the returned values of a node to the internal state.

### Define the nodes[​](#define-the-nodes "Direct link to Define the nodes")

We now need to define a few different nodes in our graph. In `langgraph`, a node can be either a function or a [runnable](https://python.langchain.com/docs/expression_language/)
. There are two main nodes we need for this:

1.  The agent: responsible for deciding what (if any) actions to take.
2.  A function to invoke tools: if the agent decides to take an action, this node will then execute that action.

We will also need to define some edges. Some of these edges may be conditional. The reason they are conditional is that based on the output of a node, one of several paths may be taken. The path that is taken is not known until that node is run (the LLM decides).

1.  Conditional Edge: after the agent is called, we should either:
    
    a. If the agent said to take an action, then the function to invoke tools should be called
    
    b. If the agent said that it was finished, then it should finish
    
2.  Normal Edge: after the tools are invoked, it should always go back to the agent to decide what to do next
    

Let's define the nodes, as well as a function to decide how what conditional edge to take.

    from langgraph.prebuilt import ToolInvocationimport jsonfrom langchain_core.messages import FunctionMessagedef should_continue(state):    messages = state['messages']    last_message = messages[-1]        if "function_call" not in last_message.additional_kwargs:        return "end"        else:        return "continue"def call_model(state):    messages = state['messages']    response = model.invoke(messages)        return {"messages": [response]}def call_tool(state):    messages = state['messages']            last_message = messages[-1]        action = ToolInvocation(        tool=last_message.additional_kwargs["function_call"]["name"],        tool_input=json.loads(last_message.additional_kwargs["function_call"]["arguments"]),    )        response = tool_executor.invoke(action)        function_message = FunctionMessage(content=str(response), name=action.tool)        return {"messages": [function_message]}

#### API Reference:

*   [FunctionMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.function.FunctionMessage.html)
    

### Define the graph[​](#define-the-graph "Direct link to Define the graph")

We can now put it all together and define the graph!

    from langgraph.graph import StateGraph, ENDworkflow = StateGraph(AgentState)workflow.add_node("agent", call_model)workflow.add_node("action", call_tool)workflow.set_entry_point("agent")workflow.add_conditional_edges(            "agent",        should_continue,                            {                "continue": "action",                "end": END    })workflow.add_edge('action', 'agent')app = workflow.compile()

### Use it![​](#use-it "Direct link to Use it!")

We can now use it! This now exposes the [same interface](https://python.langchain.com/docs/expression_language/)
 as all other LangChain runnables. This runnable accepts a list of messages.

    from langchain_core.messages import HumanMessageinputs = {"messages": [HumanMessage(content="what is the weather in sf")]}app.invoke(inputs)

#### API Reference:

*   [HumanMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.human.HumanMessage.html)
    

This may take a little bit - it's making a few calls behind the scenes. In order to start seeing some intermediate results as they happen, we can use streaming - see below for more information on that.

Streaming[​](#streaming "Direct link to Streaming")

----------------------------------------------------

LangGraph has support for several different types of streaming.

### Streaming Node Output[​](#streaming-node-output "Direct link to Streaming Node Output")

One of the benefits of using LangGraph is that it is easy to stream output as it's produced by each node.

    inputs = {"messages": [HumanMessage(content="what is the weather in sf")]}for output in app.stream(inputs):        for key, value in output.items():        print(f"Output from node '{key}':")        print("---")        print(value)    print("\n---\n")

    Output from node 'agent':---{'messages': [AIMessage(content='', additional_kwargs={'function_call': {'arguments': '{\n  "query": "weather in San Francisco"\n}', 'name': 'tavily_search_results_json'}})]}---Output from node 'action':---{'messages': [FunctionMessage(content="[{'url': 'https://weatherspark.com/h/m/557/2024/1/Historical-Weather-in-January-2024-in-San-Francisco-California-United-States', 'content': 'January 2024 Weather History in San Francisco California, United States  Daily Precipitation in January 2024 in San Francisco Observed Weather in January 2024 in San Francisco  San Francisco Temperature History January 2024 Hourly Temperature in January 2024 in San Francisco  Hours of Daylight and Twilight in January 2024 in San FranciscoThis report shows the past weather for San Francisco, providing a weather history for January 2024. It features all historical weather data series we have available, including the San Francisco temperature history for January 2024. You can drill down from year to month and even day level reports by clicking on the graphs.'}]", name='tavily_search_results_json')]}---Output from node 'agent':---{'messages': [AIMessage(content="I couldn't find the current weather in San Francisco. However, you can visit [WeatherSpark](https://weatherspark.com/h/m/557/2024/1/Historical-Weather-in-January-2024-in-San-Francisco-California-United-States) to check the historical weather data for January 2024 in San Francisco.")]}---Output from node '__end__':---{'messages': [HumanMessage(content='what is the weather in sf'), AIMessage(content='', additional_kwargs={'function_call': {'arguments': '{\n  "query": "weather in San Francisco"\n}', 'name': 'tavily_search_results_json'}}), FunctionMessage(content="[{'url': 'https://weatherspark.com/h/m/557/2024/1/Historical-Weather-in-January-2024-in-San-Francisco-California-United-States', 'content': 'January 2024 Weather History in San Francisco California, United States  Daily Precipitation in January 2024 in San Francisco Observed Weather in January 2024 in San Francisco  San Francisco Temperature History January 2024 Hourly Temperature in January 2024 in San Francisco  Hours of Daylight and Twilight in January 2024 in San FranciscoThis report shows the past weather for San Francisco, providing a weather history for January 2024. It features all historical weather data series we have available, including the San Francisco temperature history for January 2024. You can drill down from year to month and even day level reports by clicking on the graphs.'}]", name='tavily_search_results_json'), AIMessage(content="I couldn't find the current weather in San Francisco. However, you can visit [WeatherSpark](https://weatherspark.com/h/m/557/2024/1/Historical-Weather-in-January-2024-in-San-Francisco-California-United-States) to check the historical weather data for January 2024 in San Francisco.")]}---

### Streaming LLM Tokens[​](#streaming-llm-tokens "Direct link to Streaming LLM Tokens")

You can also access the LLM tokens as they are produced by each node. In this case only the "agent" node produces LLM tokens. In order for this to work properly, you must be using an LLM that supports streaming as well as have set it when constructing the LLM (e.g. `ChatOpenAI(model="gpt-3.5-turbo-1106", streaming=True)`)

    inputs = {"messages": [HumanMessage(content="what is the weather in sf")]}async for output in app.astream_log(inputs, include_types=["llm"]):        for op in output.ops:        if op["path"] == "/streamed_output/-":                        ...        elif op["path"].startswith("/logs/") and op["path"].endswith(            "/streamed_output/-"        ):                        print(op["value"])

    content='' additional_kwargs={'function_call': {'arguments': '', 'name': 'tavily_search_results_json'}}content='' additional_kwargs={'function_call': {'arguments': '{\n', 'name': ''}}content='' additional_kwargs={'function_call': {'arguments': ' ', 'name': ''}}content='' additional_kwargs={'function_call': {'arguments': ' "', 'name': ''}}content='' additional_kwargs={'function_call': {'arguments': 'query', 'name': ''}}...

When to Use[​](#when-to-use "Direct link to When to Use")

----------------------------------------------------------

When should you use this versus [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
?

If you need cycles.

Langchain Expression Language allows you to easily define chains (DAGs) but does not have a good mechanism for adding in cycles. `langgraph` adds that syntax.

How-to Guides[​](#how-to-guides "Direct link to How-to Guides")

----------------------------------------------------------------

These guides show how to use LangGraph in particular ways.

### Async[​](#async "Direct link to Async")

If you are running LangGraph in async workflows, you may want to create the nodes to be async by default. For a walkthrough on how to do that, see [this documentation](https://github.com/langchain-ai/langgraph/blob/main/examples/async.ipynb)

### Streaming Tokens[​](#streaming-tokens "Direct link to Streaming Tokens")

Sometimes language models take a while to respond and you may want to stream tokens to end users. For a guide on how to do this, see [this documentation](https://github.com/langchain-ai/langgraph/blob/main/examples/streaming-tokens.ipynb)

### Persistence[​](#persistence "Direct link to Persistence")

LangGraph comes with built-in persistence, allowing you to save the state of the graph at point and resume from there. For a walkthrough on how to do that, see [this documentation](https://github.com/langchain-ai/langgraph/blob/main/examples/persistence.ipynb)

### Human-in-the-loop[​](#human-in-the-loop "Direct link to Human-in-the-loop")

LangGraph comes with built-in support for human-in-the-loop workflows. This is useful when you want to have a human review the current state before proceeding to a particular node. For a walkthrough on how to do that, see [this documentation](https://github.com/langchain-ai/langgraph/blob/main/examples/human-in-the-loop.ipynb)

### Visualizing the graph[​](#visualizing-the-graph "Direct link to Visualizing the graph")

Agents you create with LangGraph can be complex. In order to make it easier to understand what is happening under the hood, we've added methods to print out and visualize the graph. This can create both ascii art and pngs. For a walkthrough on how to do that, see [this documentation](https://github.com/langchain-ai/langgraph/blob/main/examples/visualization.ipynb)

### "Time Travel"[​](#time-travel "Direct link to "Time Travel"")

With "time travel" functionality you can jump to any point in the graph execution, modify the state, and rerun from there. This is useful for both debugging workflows, as well as end user-facing workflows to allow them to correct the state. For a walkthrough on how to do that, see [this documentation](https://github.com/langchain-ai/langgraph/blob/main/examples/time-travel.ipynb)

Examples[​](#examples "Direct link to Examples")

-------------------------------------------------

### ChatAgentExecutor: with function calling[​](#chatagentexecutor-with-function-calling "Direct link to ChatAgentExecutor: with function calling")

This agent executor takes a list of messages as input and outputs a list of messages. All agent state is represented as a list of messages. This specifically uses OpenAI function calling. This is recommended agent executor for newer chat based models that support function calling.

*   [Getting Started Notebook](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/base.ipynb)
    : Walks through creating this type of executor from scratch
*   [High Level Entrypoint](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/high-level.ipynb)
    : Walks through how to use the high level entrypoint for the chat agent executor.

**Modifications**

We also have a lot of examples highlighting how to slightly modify the base chat agent executor. These all build off the [getting started notebook](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/base.ipynb)
 so it is recommended you start with that first.

*   [Human-in-the-loop](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/human-in-the-loop.ipynb)
    : How to add a human-in-the-loop component
*   [Force calling a tool first](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/force-calling-a-tool-first.ipynb)
    : How to always call a specific tool first
*   [Respond in a specific format](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/respond-in-format.ipynb)
    : How to force the agent to respond in a specific format
*   [Dynamically returning tool output directly](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/dynamically-returning-directly.ipynb)
    : How to dynamically let the agent choose whether to return the result of a tool directly to the user
*   [Managing agent steps](https://github.com/langchain-ai/langgraph/blob/main/examples/chat_agent_executor_with_function_calling/managing-agent-steps.ipynb)
    : How to more explicitly manage intermediate steps that an agent takes

### AgentExecutor[​](#agentexecutor "Direct link to AgentExecutor")

This agent executor uses existing LangChain agents.

*   [Getting Started Notebook](https://github.com/langchain-ai/langgraph/blob/main/examples/agent_executor/base.ipynb)
    : Walks through creating this type of executor from scratch
*   [High Level Entrypoint](https://github.com/langchain-ai/langgraph/blob/main/examples/agent_executor/high-level.ipynb)
    : Walks through how to use the high level entrypoint for the chat agent executor.

**Modifications**

We also have a lot of examples highlighting how to slightly modify the base chat agent executor. These all build off the [getting started notebook](https://github.com/langchain-ai/langgraph/blob/main/examples/agent_executor/base.ipynb)
 so it is recommended you start with that first.

*   [Human-in-the-loop](https://github.com/langchain-ai/langgraph/blob/main/examples/agent_executor/human-in-the-loop.ipynb)
    : How to add a human-in-the-loop component
*   [Force calling a tool first](https://github.com/langchain-ai/langgraph/blob/main/examples/agent_executor/force-calling-a-tool-first.ipynb)
    : How to always call a specific tool first
*   [Managing agent steps](https://github.com/langchain-ai/langgraph/blob/main/examples/agent_executor/managing-agent-steps.ipynb)
    : How to more explicitly manage intermediate steps that an agent takes

### Planning Agent Examples[​](#planning-agent-examples "Direct link to Planning Agent Examples")

The following notebooks implement agent architectures prototypical of the "plan-and-execute" style, where an LLM planner decomposes a user request into a program, an executor executes the program, and an LLM synthesizes a response (and/or dynamically replans) based on the program outputs.

*   [Plan-and-execute](https://github.com/langchain-ai/langgraph/blob/main/examples/plan-and-execute/plan-and-execute.ipynb)
    : a simple agent with a **planner** that generates a multi-step task list, an **executor** that invokes the tools in the plan, and a **replanner** that responds or generates an updated plan. Based on the [Plan-and-solve](https://arxiv.org/abs/2305.04091)
     paper by Wang, et. al.
*   [Reasoning without Observation](https://github.com/langchain-ai/langgraph/blob/main/examples/rewoo/rewoo.ipynb)
    : planner generates a task list whose observations are saved as **variables**. Variables can be used in subsequent tasks to reduce the need for further re-planning. Based on the [ReWOO](https://arxiv.org/abs/2305.18323)
     paper by Xu, et. al.
*   [LLMCompiler](https://github.com/langchain-ai/langgraph/blob/main/examples/llm-compiler/LLMCompiler.ipynb)
    : planner generates a **DAG** of tasks with variable responses. Tasks are **streamed** and executed eagerly to minimize tool execution runtime. Based on the [paper](https://arxiv.org/abs/2312.04511)
     by Kim, et. al.

### Reflection / Self-Critique[​](#reflection--self-critique "Direct link to Reflection / Self-Critique")

When output quality is a major concern, it's common to incorporate some combination of self-critique or reflection and external validation to refine your system's outputs. The following examples demonstrate research that implement this type of design.

*   [Basic Reflection](https://github.com/langchain-ai/langgraph/tree/main/examples/reflection/reflection.ipynb)
    : add a simple "reflect" step in your graph to prompt your system to revise its outputs.
*   [Reflexion](https://github.com/langchain-ai/langgraph/tree/main/examples/reflexion/reflexion.ipynb)
    : critique missing and superfluous aspects of the agent's response to guide subsequent steps. Based on [Reflexion](https://arxiv.org/abs/2303.11366)
    , by Shinn, et. al.
*   [Language Agent Tree Search](https://github.com/langchain-ai/langgraph/tree/main/examples/lats/lats.ipynb)
    : execute multiple agents in parallel, using reflection and environmental rewards to drive a Monte Carlo Tree Search. Based on [LATS](https://arxiv.org/abs/2310.04406)
    , by Zhou, et. al.

### Multi-agent Examples[​](#multi-agent-examples "Direct link to Multi-agent Examples")

*   [Multi-agent collaboration](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/multi-agent-collaboration.ipynb)
    : how to create two agents that work together to accomplish a task
*   [Multi-agent with supervisor](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/agent_supervisor.ipynb)
    : how to orchestrate individual agents by using an LLM as a "supervisor" to distribute work
*   [Hierarchical agent teams](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/hierarchical_agent_teams.ipynb)
    : how to orchestrate "teams" of agents as nested graphs that can collaborate to solve a problem

### Web Research[​](#web-research "Direct link to Web Research")

*   [STORM](https://github.com/langchain-ai/langgraph/tree/main/examples/storm/storm.ipynb)
    : writing system that generates Wikipedia-style articles on any topic, applying outline generation (planning) + multi-perspective question-answering for added breadth and reliability. Based on [STORM](https://arxiv.org/abs/2402.14207)
     by Shao, et. al.

### Chatbot Evaluation via Simulation[​](#chatbot-evaluation-via-simulation "Direct link to Chatbot Evaluation via Simulation")

It can often be tough to evaluation chat bots in multi-turn situations. One way to do this is with simulations.

*   [Chat bot evaluation as multi-agent simulation](https://github.com/langchain-ai/langgraph/blob/main/examples/chatbot-simulation-evaluation/agent-simulation-evaluation.ipynb)
    : how to simulate a dialogue between a "virtual user" and your chat bot
*   [Evaluating over a dataset](https://github.com/langchain-ai/langgraph/tree/main/examples/chatbot-simulation-evaluation/langsmith-agent-simulation-evaluation.ipynb)
    : benchmark your assistant over a LangSmith dataset, which tasks a simulated customer to red-team your chat bot.

### Multimodal Examples[​](#multimodal-examples "Direct link to Multimodal Examples")

*   [WebVoyager](https://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web_voyager.ipynb)
    : vision-enabled web browsing agent that uses [Set-of-marks](https://som-gpt4v.github.io/)
     prompting to navigate a web browser and execute tasks

### [Chain-of-Table](https://github.com/CYQIQ/MultiCoT)
[​](#chain-of-table "Direct link to chain-of-table")

[Chain of Table](https://arxiv.org/abs/2401.04398)
 is a framework that elicits SOTA performance when answering questions over tabular data. [This implementation](https://github.com/CYQIQ/MultiCoT)
 by Github user [CYQIQ](https://github.com/CYQIQ)
 uses LangGraph to control the flow.

Documentation[​](#documentation "Direct link to Documentation")

----------------------------------------------------------------

There are only a few new APIs to use.

### StateGraph[​](#stategraph "Direct link to StateGraph")

The main entrypoint is `StateGraph`.

    from langgraph.graph import StateGraph

This class is responsible for constructing the graph. It exposes an interface inspired by [NetworkX](https://networkx.org/documentation/latest/)
. This graph is parameterized by a state object that it passes around to each node.

#### `__init__`[​](#__init__ "Direct link to __init__")

        def __init__(self, schema: Type[Any]) -> None:

When constructing the graph, you need to pass in a schema for a state. Each node then returns operations to update that state. These operations can either SET specific attributes on the state (e.g. overwrite the existing values) or ADD to the existing attribute. Whether to set or add is denoted by annotating the state object you construct the graph with.

The recommended way to specify the schema is with a typed dictionary: `from typing import TypedDict`

You can then annotate the different attributes using `from typing import Annotated`. Currently, the only supported annotation is `import operator; operator.add`. This annotation will make it so that any node that returns this attribute ADDS that new result to the existing value.

Let's take a look at an example:

    from typing import TypedDict, Annotated, Unionfrom langchain_core.agents import AgentAction, AgentFinishimport operatorclass AgentState(TypedDict):      input: str         agent_outcome: Union[AgentAction, AgentFinish, None]            intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]

#### API Reference:

*   [AgentAction](https://api.python.langchain.com/en/latest/agents/langchain_core.agents.AgentAction.html)
    
*   [AgentFinish](https://api.python.langchain.com/en/latest/agents/langchain_core.agents.AgentFinish.html)
    

We can then use this like:

    graph = StateGraph(AgentState)...app = graph.compile()inputs = {      "input": "hi"                  }

#### `.add_node`[​](#add_node "Direct link to add_node")

        def add_node(self, key: str, action: RunnableLike) -> None:

This method adds a node to the graph. It takes two arguments:

*   `key`: A string representing the name of the node. This must be unique.
*   `action`: The action to take when this node is called. This should either be a function or a runnable.

#### `.add_edge`[​](#add_edge "Direct link to add_edge")

        def add_edge(self, start_key: str, end_key: str) -> None:

Creates an edge from one node to the next. This means that output of the first node will be passed to the next node. It takes two arguments.

*   `start_key`: A string representing the name of the start node. This key must have already been registered in the graph.
*   `end_key`: A string representing the name of the end node. This key must have already been registered in the graph.

#### `.add_conditional_edges`[​](#add_conditional_edges "Direct link to add_conditional_edges")

        def add_conditional_edges(        self,        start_key: str,        condition: Callable[..., str],        conditional_edge_mapping: Dict[str, str],    ) -> None:

This method adds conditional edges. What this means is that only one of the downstream edges will be taken, and which one that is depends on the results of the start node. This takes three arguments:

*   `start_key`: A string representing the name of the start node. This key must have already been registered in the graph.
*   `condition`: A function to call to decide what to do next. The input will be the output of the start node. It should return a string that is present in `conditional_edge_mapping` and represents the edge to take.
*   `conditional_edge_mapping`: A mapping of string to string. The keys should be strings that may be returned by `condition`. The values should be the downstream node to call if that condition is returned.

#### `.set_entry_point`[​](#set_entry_point "Direct link to set_entry_point")

        def set_entry_point(self, key: str) -> None:

The entrypoint to the graph. This is the node that is first called. It only takes one argument:

*   `key`: The name of the node that should be called first.

#### `.set_conditional_entry_point`[​](#set_conditional_entry_point "Direct link to set_conditional_entry_point")

        def set_conditional_entry_point(        self,        condition: Callable[..., str],        conditional_edge_mapping: Optional[Dict[str, str]] = None,    ) -> None:

This method adds a conditional entry point. What this means is that when the graph is called, it will call the `condition` Callable to decide what node to enter into first.

*   `condition`: A function to call to decide what to do next. The input will be the input to the graph. It should return a string that is present in `conditional_edge_mapping` and represents the edge to take.
*   `conditional_edge_mapping`: A mapping of string to string. The keys should be strings that may be returned by `condition`. The values should be the downstream node to call if that condition is returned.

#### `.set_finish_point`[​](#set_finish_point "Direct link to set_finish_point")

        def set_finish_point(self, key: str) -> None:

This is the exit point of the graph. When this node is called, the results will be the final result from the graph. It only has one argument:

*   `key`: The name of the node that, when called, will return the results of calling it as the final output

Note: This does not need to be called if at any point you previously created an edge (conditional or normal) to `END`

### Graph[​](#graph "Direct link to Graph")

    from langgraph.graph import Graphgraph = Graph()

This has the same interface as `StateGraph` with the exception that it doesn't update a state object over time, and rather relies on passing around the full state from each step. This means that whatever is returned from one node is the input to the next as is.

### `END`[​](#end "Direct link to end")

    from langgraph.graph import END

This is a special node representing the end of the graph. This means that anything passed to this node will be the final output of the graph. It can be used in two places:

*   As the `end_key` in `add_edge`
*   As a value in `conditional_edge_mapping` as passed to `add_conditional_edges`

Prebuilt Examples[​](#prebuilt-examples "Direct link to Prebuilt Examples")

----------------------------------------------------------------------------

There are also a few methods we've added to make it easy to use common, prebuilt graphs and components.

### ToolExecutor[​](#toolexecutor "Direct link to ToolExecutor")

    from langgraph.prebuilt import ToolExecutor

This is a simple helper class to help with calling tools. It is parameterized by a list of tools:

    tools = [...]tool_executor = ToolExecutor(tools)

It then exposes a [runnable interface](https://python.langchain.com/docs/expression_language/interface)
. It can be used to call tools: you can pass in an [AgentAction](https://python.langchain.com/docs/modules/agents/concepts#agentaction)
 and it will look up the relevant tool and call it with the appropriate input.

### chat\_agent\_executor.create\_function\_calling\_executor[​](#chat_agent_executorcreate_function_calling_executor "Direct link to chat_agent_executor.create_function_calling_executor")

    from langgraph.prebuilt import chat_agent_executor

This is a helper function for creating a graph that works with a chat model that utilizes function calling. Can be created by passing in a model and a list of tools. The model must be one that supports OpenAI function calling.

    from langchain_openai import ChatOpenAIfrom langchain_community.tools.tavily_search import TavilySearchResultsfrom langgraph.prebuilt import chat_agent_executorfrom langchain_core.messages import HumanMessagetools = [TavilySearchResults(max_results=1)]model = ChatOpenAI()app = chat_agent_executor.create_function_calling_executor(model, tools)inputs = {"messages": [HumanMessage(content="what is the weather in sf")]}for s in app.stream(inputs):    print(list(s.values())[0])    print("----")

#### API Reference:

*   [ChatOpenAI](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
    
*   [TavilySearchResults](https://api.python.langchain.com/en/latest/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
    
*   [HumanMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.human.HumanMessage.html)
    

### chat\_agent\_executor.create\_tool\_calling\_executor[​](#chat_agent_executorcreate_tool_calling_executor "Direct link to chat_agent_executor.create_tool_calling_executor")

    from langgraph.prebuilt import chat_agent_executor

This is a helper function for creating a graph that works with a chat model that utilizes tool calling. Can be created by passing in a model and a list of tools. The model must be one that supports OpenAI tool calling.

    from langchain_openai import ChatOpenAIfrom langchain_community.tools.tavily_search import TavilySearchResultsfrom langgraph.prebuilt import chat_agent_executorfrom langchain_core.messages import HumanMessagetools = [TavilySearchResults(max_results=1)]model = ChatOpenAI()app = chat_agent_executor.create_tool_calling_executor(model, tools)inputs = {"messages": [HumanMessage(content="what is the weather in sf")]}for s in app.stream(inputs):    print(list(s.values())[0])    print("----")

#### API Reference:

*   [ChatOpenAI](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
    
*   [TavilySearchResults](https://api.python.langchain.com/en/latest/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
    
*   [HumanMessage](https://api.python.langchain.com/en/latest/messages/langchain_core.messages.human.HumanMessage.html)
    

### create\_agent\_executor[​](#create_agent_executor "Direct link to create_agent_executor")

    from langgraph.prebuilt import create_agent_executor

This is a helper function for creating a graph that works with [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
. Can be created by passing in an agent and a list of tools.

    from langgraph.prebuilt import create_agent_executorfrom langchain_openai import ChatOpenAIfrom langchain import hubfrom langchain.agents import create_openai_functions_agentfrom langchain_community.tools.tavily_search import TavilySearchResultstools = [TavilySearchResults(max_results=1)]prompt = hub.pull("hwchase17/openai-functions-agent")llm = ChatOpenAI(model="gpt-3.5-turbo-1106")agent_runnable = create_openai_functions_agent(llm, tools, prompt)app = create_agent_executor(agent_runnable, tools)inputs = {"input": "what is the weather in sf", "chat_history": []}for s in app.stream(inputs):    print(list(s.values())[0])    print("----")

#### API Reference:

*   [ChatOpenAI](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
    
*   [create\_openai\_functions\_agent](https://api.python.langchain.com/en/latest/agents/langchain.agents.openai_functions_agent.base.create_openai_functions_agent.html)
    
*   [TavilySearchResults](https://api.python.langchain.com/en/latest/tools/langchain_community.tools.tavily_search.tool.TavilySearchResults.html)
    

* * *

#### Help us out by providing feedback on this documentation page:

*   [Overview](#overview)
    
*   [Installation](#installation)
    
*   [Quick start](#quick-start)
    *   [Interaction with LCEL](#interaction-with-lcel)
        
*   [Conditional edges](#conditional-edges)
    
*   [Cycles](#cycles)
    *   [Set up the tools](#set-up-the-tools)
        
    *   [Set up the model](#set-up-the-model)
        
    *   [Define the agent state](#define-the-agent-state)
        
    *   [Define the nodes](#define-the-nodes)
        
    *   [Define the graph](#define-the-graph)
        
    *   [Use it!](#use-it)
        
*   [Streaming](#streaming)
    *   [Streaming Node Output](#streaming-node-output)
        
    *   [Streaming LLM Tokens](#streaming-llm-tokens)
        
*   [When to Use](#when-to-use)
    
*   [How-to Guides](#how-to-guides)
    *   [Async](#async)
        
    *   [Streaming Tokens](#streaming-tokens)
        
    *   [Persistence](#persistence)
        
    *   [Human-in-the-loop](#human-in-the-loop)
        
    *   [Visualizing the graph](#visualizing-the-graph)
        
    *   ["Time Travel"](#time-travel)
        
*   [Examples](#examples)
    *   [ChatAgentExecutor: with function calling](#chatagentexecutor-with-function-calling)
        
    *   [AgentExecutor](#agentexecutor)
        
    *   [Planning Agent Examples](#planning-agent-examples)
        
    *   [Reflection / Self-Critique](#reflection--self-critique)
        
    *   [Multi-agent Examples](#multi-agent-examples)
        
    *   [Web Research](#web-research)
        
    *   [Chatbot Evaluation via Simulation](#chatbot-evaluation-via-simulation)
        
    *   [Multimodal Examples](#multimodal-examples)
        
    *   [Chain-of-Table](#chain-of-table)
        
*   [Documentation](#documentation)
    *   [StateGraph](#stategraph)
        
    *   [Graph](#graph)
        
    *   [`END`](#end)
        
*   [Prebuilt Examples](#prebuilt-examples)
    *   [ToolExecutor](#toolexecutor)
        
    *   [chat\_agent\_executor.create\_function\_calling\_executor](#chat_agent_executorcreate_function_calling_executor)
        
    *   [chat\_agent\_executor.create\_tool\_calling\_executor](#chat_agent_executorcreate_tool_calling_executor)
        
    *   [create\_agent\_executor](#create_agent_executor)