# This file takes in the URL of a website and crawls the pages to save the output in a markdown file.

from firecrawl import FirecrawlApp
import markdownify  # You might need to install this package using pip

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='fc-0cbd51c715084dbdbae4854d5224440b')
print("Initialized FirecrawlApp with provided API key.")

# Scrape a single URL
crawl_url = 'https://python.langchain.com/docs/modules/tools/tools_as_openai_functions/'
# https://python.langchain.com/docs/modules/tools/tools_as_openai_functions/
print(f"Preparing to crawl the URL: {crawl_url}")

params = {
    'crawlerOptions': {
        'excludes': [],
        'includes': ['docs/modules/tools/tools_as_openai_functions/*'],  # specify to include all pages under docs/langgraph/
        'limit': 1000,
    },
    'pageOptions': {
        'onlyMainContent': True
    }
}
print("Crawler parameters set. Starting the crawl...")

crawl_result = app.crawl_url(crawl_url, params=params, wait_until_done=True, timeout=5)

# Assuming each result in crawl_result is a dictionary
for result in crawl_result:    
    # Extract markdown content if available and write to a file
    markdown_content = result.get('markdown', None)
    if markdown_content:
        # Open the file in append mode to avoid overwriting previous content
        with open('tools_openai.md', 'a') as f:
            f.write(markdown_content)
        print("Markdown content saved to langchain_langgraph_documentation.md.")
    else:
        print("No markdown content available for this result.")

